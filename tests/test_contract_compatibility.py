from __future__ import annotations

import dataclasses
import inspect

from trading_sdk import AccountSnapshot, BaseStrategy, OrderResult, OrderSignal


def test_public_exports_are_available() -> None:
    assert BaseStrategy is not None
    assert OrderSignal is not None
    assert OrderResult is not None
    assert AccountSnapshot is not None


def test_base_strategy_next_signal_signature_is_stable() -> None:
    params = list(inspect.signature(BaseStrategy.next_signal).parameters)
    assert params == ["self", "market_data", "account_data"]


def test_order_signal_required_fields_are_stable() -> None:
    fields = {field.name for field in dataclasses.fields(OrderSignal)}
    assert {"action", "quantity", "type", "reasoning", "params"}.issubset(fields)


def test_account_snapshot_from_dict_is_supported() -> None:
    snapshot = AccountSnapshot.from_account_data({"balance": "1000", "cash": 900})
    assert snapshot.balance == 1000.0
    assert snapshot.cash == 900.0
