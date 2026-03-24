"""SQLite-backed runtime store for restart-safe paper trading."""

from __future__ import annotations

import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from mytradingbot.core.models import (
    BrokerBracketState,
    BrokerOrder,
    FillEvent,
    PositionSnapshot,
)
from mytradingbot.core.settings import AppSettings
from mytradingbot.runtime.models import (
    DecisionAuditRecord,
    FillLifecycleRecord,
    ObservedOrderRecord,
    ObservedPositionRecord,
    OrderLifecycleRecord,
    PaperTradingSessionReport,
    RuntimeIncidentRecord,
    RuntimeSessionContext,
)


class RuntimeStateStore:
    """Persist runtime entities and session ledgers under repo-local SQLite."""

    def __init__(
        self,
        settings: AppSettings | None = None,
        *,
        database_path: Path | None = None,
    ) -> None:
        self.settings = settings or AppSettings()
        self.settings.ensure_runtime_directories()
        self.database_path = database_path or (
            self.settings.paths.state_dir / self.settings.runtime_safety.sqlite_filename
        )
        self.database_path.parent.mkdir(parents=True, exist_ok=True)
        self._ensure_schema()

    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.database_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _ensure_schema(self) -> None:
        with self._connect() as connection:
            connection.executescript(
                """
                CREATE TABLE IF NOT EXISTS sessions (
                    session_id TEXT PRIMARY KEY,
                    run_id TEXT NOT NULL,
                    strategy TEXT NOT NULL,
                    mode TEXT NOT NULL,
                    started_at TEXT NOT NULL,
                    completed_at TEXT,
                    status TEXT,
                    payload_json TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS decision_audits (
                    event_id TEXT PRIMARY KEY,
                    session_id TEXT NOT NULL,
                    run_id TEXT NOT NULL,
                    symbol TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    final_status TEXT NOT NULL,
                    rejection_code TEXT,
                    payload_json TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS orders (
                    order_id TEXT PRIMARY KEY,
                    session_id TEXT NOT NULL,
                    run_id TEXT NOT NULL,
                    symbol TEXT NOT NULL,
                    client_order_id TEXT,
                    status TEXT NOT NULL,
                    submitted_at TEXT NOT NULL,
                    payload_json TEXT NOT NULL
                );
                CREATE UNIQUE INDEX IF NOT EXISTS idx_orders_client_order_id ON orders(client_order_id);
                CREATE TABLE IF NOT EXISTS fills (
                    fill_id TEXT PRIMARY KEY,
                    order_id TEXT NOT NULL,
                    session_id TEXT NOT NULL,
                    run_id TEXT NOT NULL,
                    symbol TEXT NOT NULL,
                    filled_at TEXT NOT NULL,
                    payload_json TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS positions (
                    symbol TEXT PRIMARY KEY,
                    quantity REAL NOT NULL,
                    updated_at TEXT NOT NULL,
                    payload_json TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS brackets (
                    entry_order_id TEXT PRIMARY KEY,
                    symbol TEXT NOT NULL,
                    status TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    payload_json TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS cooldowns (
                    symbol TEXT NOT NULL,
                    strategy TEXT NOT NULL,
                    expires_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    PRIMARY KEY (symbol, strategy)
                );
                CREATE TABLE IF NOT EXISTS incidents (
                    incident_id TEXT PRIMARY KEY,
                    session_id TEXT,
                    run_id TEXT,
                    code TEXT NOT NULL,
                    severity TEXT NOT NULL,
                    timestamp TEXT NOT NULL,
                    payload_json TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS session_reports (
                    session_id TEXT PRIMARY KEY,
                    run_id TEXT NOT NULL,
                    completed_at TEXT NOT NULL,
                    payload_json TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS observed_orders (
                    order_id TEXT PRIMARY KEY,
                    symbol TEXT NOT NULL,
                    ownership_class TEXT NOT NULL,
                    observed_at TEXT NOT NULL,
                    payload_json TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS observed_positions (
                    symbol TEXT PRIMARY KEY,
                    ownership_class TEXT NOT NULL,
                    observed_at TEXT NOT NULL,
                    payload_json TEXT NOT NULL
                );
                """
            )

    def record_session_start(self, context: RuntimeSessionContext) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                INSERT OR REPLACE INTO sessions (session_id, run_id, strategy, mode, started_at, status, payload_json)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    context.session_id,
                    context.run_id,
                    context.strategy,
                    context.mode.value,
                    context.started_at.isoformat(),
                    "running",
                    context.model_dump_json(),
                ),
            )

    def record_session_complete(self, report: PaperTradingSessionReport) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                UPDATE sessions
                SET completed_at = ?, status = ?, payload_json = ?
                WHERE session_id = ?
                """,
                (
                    report.completed_at.isoformat(),
                    "completed",
                    report.model_dump_json(),
                    report.session_id,
                ),
            )
            connection.execute(
                """
                INSERT OR REPLACE INTO session_reports (session_id, run_id, completed_at, payload_json)
                VALUES (?, ?, ?, ?)
                """,
                (
                    report.session_id,
                    report.run_id,
                    report.completed_at.isoformat(),
                    report.model_dump_json(),
                ),
            )

    def record_decision(self, record: DecisionAuditRecord) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                INSERT OR REPLACE INTO decision_audits
                (event_id, session_id, run_id, symbol, timestamp, final_status, rejection_code, payload_json)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    record.event_id,
                    record.session_id,
                    record.run_id,
                    record.symbol,
                    record.timestamp.isoformat(),
                    record.final_decision_status,
                    record.final_rejection_reason_code,
                    record.model_dump_json(),
                ),
            )

    def record_order(self, record: OrderLifecycleRecord) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                INSERT OR REPLACE INTO orders
                (order_id, session_id, run_id, symbol, client_order_id, status, submitted_at, payload_json)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    record.order_id,
                    record.session_id,
                    record.run_id,
                    record.symbol,
                    record.client_order_id,
                    record.status,
                    record.submitted_at.isoformat(),
                    record.model_dump_json(),
                ),
            )

    def record_fill(self, record: FillLifecycleRecord) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                INSERT OR REPLACE INTO fills
                (fill_id, order_id, session_id, run_id, symbol, filled_at, payload_json)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    record.fill_id,
                    record.order_id,
                    record.session_id,
                    record.run_id,
                    record.symbol,
                    record.filled_at.isoformat(),
                    record.model_dump_json(),
                ),
            )

    def record_position(self, position: PositionSnapshot) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                INSERT OR REPLACE INTO positions (symbol, quantity, updated_at, payload_json)
                VALUES (?, ?, ?, ?)
                """,
                (
                    position.symbol,
                    position.quantity,
                    datetime.now(timezone.utc).isoformat(),
                    position.model_dump_json(),
                ),
            )

    def replace_positions(self, positions: list[PositionSnapshot | dict]) -> None:
        normalized = [
            position if isinstance(position, PositionSnapshot) else PositionSnapshot.model_validate(position)
            for position in positions
        ]
        with self._connect() as connection:
            connection.execute("DELETE FROM positions")
            for position in normalized:
                connection.execute(
                    """
                    INSERT OR REPLACE INTO positions (symbol, quantity, updated_at, payload_json)
                    VALUES (?, ?, ?, ?)
                    """,
                    (
                        position.symbol,
                        position.quantity,
                        datetime.now(timezone.utc).isoformat(),
                        position.model_dump_json(),
                    ),
                )

    def record_bracket(self, bracket: BrokerBracketState) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                INSERT OR REPLACE INTO brackets (entry_order_id, symbol, status, updated_at, payload_json)
                VALUES (?, ?, ?, ?, ?)
                """,
                (
                    bracket.entry_order_id,
                    bracket.symbol,
                    bracket.status,
                    datetime.now(timezone.utc).isoformat(),
                    bracket.model_dump_json(),
                ),
            )

    def set_cooldown(self, *, symbol: str, strategy: str, expires_at: datetime) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                INSERT OR REPLACE INTO cooldowns (symbol, strategy, expires_at, updated_at)
                VALUES (?, ?, ?, ?)
                """,
                (
                    symbol,
                    strategy,
                    expires_at.isoformat(),
                    datetime.now(timezone.utc).isoformat(),
                ),
            )

    def active_cooldowns(self, *, strategy: str, now: datetime) -> set[str]:
        with self._connect() as connection:
            rows = connection.execute(
                """
                SELECT symbol FROM cooldowns
                WHERE strategy = ? AND expires_at > ?
                """,
                (strategy, now.isoformat()),
            ).fetchall()
        return {str(row["symbol"]) for row in rows}

    def record_incident(self, record: RuntimeIncidentRecord) -> None:
        with self._connect() as connection:
            connection.execute(
                """
                INSERT OR REPLACE INTO incidents
                (incident_id, session_id, run_id, code, severity, timestamp, payload_json)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    record.incident_id,
                    record.session_id,
                    record.run_id,
                    record.code,
                    record.severity,
                    record.timestamp.isoformat(),
                    record.model_dump_json(),
                ),
            )

    def replace_observed_orders(self, records: list[ObservedOrderRecord | dict]) -> None:
        normalized = [
            record if isinstance(record, ObservedOrderRecord) else ObservedOrderRecord.model_validate(record)
            for record in records
        ]
        with self._connect() as connection:
            connection.execute("DELETE FROM observed_orders")
            for record in normalized:
                connection.execute(
                    """
                    INSERT OR REPLACE INTO observed_orders
                    (order_id, symbol, ownership_class, observed_at, payload_json)
                    VALUES (?, ?, ?, ?, ?)
                    """,
                    (
                        record.order_id,
                        record.symbol,
                        record.ownership_class,
                        record.observed_at.isoformat(),
                        record.model_dump_json(),
                    ),
                )

    def replace_observed_positions(self, records: list[ObservedPositionRecord | dict]) -> None:
        normalized = [
            record if isinstance(record, ObservedPositionRecord) else ObservedPositionRecord.model_validate(record)
            for record in records
        ]
        with self._connect() as connection:
            connection.execute("DELETE FROM observed_positions")
            for record in normalized:
                connection.execute(
                    """
                    INSERT OR REPLACE INTO observed_positions
                    (symbol, ownership_class, observed_at, payload_json)
                    VALUES (?, ?, ?, ?)
                    """,
                    (
                        record.symbol,
                        record.ownership_class,
                        record.observed_at.isoformat(),
                        record.model_dump_json(),
                    ),
                )

    def list_orders(self) -> list[BrokerOrder]:
        orders: list[BrokerOrder] = []
        for record in self.list_order_records():
            orders.append(
                BrokerOrder(
                    order_id=record.order_id,
                    symbol=record.symbol,
                    side=record.side,  # type: ignore[arg-type]
                    quantity=record.quantity,
                    mode=record.mode,
                    client_order_id=record.client_order_id,
                    status=_normalize_broker_order_status(record.status),
                    submitted_at=record.submitted_at,
                    avg_fill_price=record.avg_fill_price,
                    metadata=record.metadata,
                )
            )
        return orders

    def list_order_records(self) -> list[OrderLifecycleRecord]:
        with self._connect() as connection:
            rows = connection.execute("SELECT payload_json FROM orders ORDER BY submitted_at").fetchall()
        return [OrderLifecycleRecord.model_validate_json(row["payload_json"]) for row in rows]

    def list_fills(self) -> list[FillEvent]:
        with self._connect() as connection:
            rows = connection.execute("SELECT payload_json FROM fills ORDER BY filled_at").fetchall()
        return [FillEvent.model_validate_json(row["payload_json"]) for row in rows]

    def list_fill_records(self) -> list[FillLifecycleRecord]:
        with self._connect() as connection:
            rows = connection.execute("SELECT payload_json FROM fills ORDER BY filled_at").fetchall()
        return [FillLifecycleRecord.model_validate_json(row["payload_json"]) for row in rows]

    def list_positions(self) -> list[PositionSnapshot]:
        with self._connect() as connection:
            rows = connection.execute("SELECT payload_json FROM positions ORDER BY symbol").fetchall()
        return [PositionSnapshot.model_validate_json(row["payload_json"]) for row in rows]

    def list_brackets(self) -> list[BrokerBracketState]:
        with self._connect() as connection:
            rows = connection.execute("SELECT payload_json FROM brackets ORDER BY symbol").fetchall()
        return [BrokerBracketState.model_validate_json(row["payload_json"]) for row in rows]

    def list_decisions(self) -> list[DecisionAuditRecord]:
        with self._connect() as connection:
            rows = connection.execute("SELECT payload_json FROM decision_audits ORDER BY timestamp").fetchall()
        return [DecisionAuditRecord.model_validate_json(row["payload_json"]) for row in rows]

    def list_session_reports(self) -> list[PaperTradingSessionReport]:
        with self._connect() as connection:
            rows = connection.execute("SELECT payload_json FROM session_reports ORDER BY completed_at").fetchall()
        return [PaperTradingSessionReport.model_validate_json(row["payload_json"]) for row in rows]

    def list_observed_orders(self) -> list[ObservedOrderRecord]:
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT payload_json FROM observed_orders ORDER BY observed_at"
            ).fetchall()
        return [ObservedOrderRecord.model_validate_json(row["payload_json"]) for row in rows]

    def list_observed_positions(self) -> list[ObservedPositionRecord]:
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT payload_json FROM observed_positions ORDER BY symbol"
            ).fetchall()
        return [ObservedPositionRecord.model_validate_json(row["payload_json"]) for row in rows]

    def has_client_order_id(self, client_order_id: str) -> bool:
        with self._connect() as connection:
            row = connection.execute(
                "SELECT 1 FROM orders WHERE client_order_id = ? LIMIT 1",
                (client_order_id,),
            ).fetchone()
        return row is not None

    def active_position_symbols(self) -> set[str]:
        return {
            position.symbol
            for position in self.list_positions()
            if abs(position.quantity) > 0
        }

    def foreign_position_symbols(self) -> set[str]:
        return {
            position.symbol
            for position in self.list_observed_positions()
            if position.ownership_class in {"foreign", "unknown"} and abs(position.quantity) > 0
        }

    def consecutive_incident_count(self, *, codes: set[str]) -> int:
        with self._connect() as connection:
            rows = connection.execute(
                "SELECT payload_json FROM incidents ORDER BY timestamp DESC LIMIT 20"
            ).fetchall()
        count = 0
        for row in rows:
            incident = RuntimeIncidentRecord.model_validate_json(row["payload_json"])
            if incident.code in codes:
                count += 1
                continue
            break
        return count


def _normalize_broker_order_status(status: str) -> str:
    normalized = status.lower()
    if normalized == "filled":
        return "filled"
    if normalized in {"rejected", "canceled", "cancelled", "expired", "failed"}:
        return "rejected"
    return "accepted"
