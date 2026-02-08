from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, Literal, Optional

Action = Literal["BUY", "SELL", "WAIT", "CANCEL"]
OrderType = Literal["LIMIT", "MARKET"]
TimeInForce = Literal["GTC", "IOC", "FOK"]
OrderStatus = Literal["OPEN", "FILLED", "CANCELED", "REJECTED"]


def _coerce_float(value: Any) -> float:
    try:
        if value is None:
            return 0.0
        return float(value)
    except (TypeError, ValueError):
        return 0.0


@dataclass
class AccountSnapshot:
    balance: float = 0.0
    equity: float = 0.0
    cash: float = 0.0
    position_qty: float = 0.0
    position_avg_price: float = 0.0

    @classmethod
    def from_account_data(cls, data: Any) -> "AccountSnapshot":
        if isinstance(data, cls):
            return data
        if isinstance(data, dict):
            return cls(
                balance=_coerce_float(data.get("balance")),
                equity=_coerce_float(data.get("equity")),
                cash=_coerce_float(data.get("cash")),
                position_qty=_coerce_float(data.get("position_qty")),
                position_avg_price=_coerce_float(data.get("position_avg_price")),
            )
        return cls(
            balance=_coerce_float(getattr(data, "balance", None)),
            equity=_coerce_float(getattr(data, "equity", None)),
            cash=_coerce_float(getattr(data, "cash", None)),
            position_qty=_coerce_float(getattr(data, "position_qty", None)),
            position_avg_price=_coerce_float(getattr(data, "position_avg_price", None)),
        )


AccountData = AccountSnapshot | Dict[str, Any]


@dataclass
class OrderSignal:
    action: Action
    quantity: float
    type: OrderType = "MARKET"
    price: Optional[float] = None
    sl: Optional[float] = None
    tp: Optional[float] = None
    time_in_force: TimeInForce = "GTC"
    order_id: Optional[str] = None
    reasoning: str = ""
    params: Dict[str, Any] = field(default_factory=dict)


@dataclass
class OrderResult:
    order_id: Optional[str]
    status: OrderStatus
    average_price: float = 0.0
    filled_quantity: float = 0.0
    timestamp: int = 0
    error_message: str = ""
