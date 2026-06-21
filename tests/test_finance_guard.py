from finance_guard import FinanceGuard, Transaction
import json
import pytest

def test_process_transaction():
    finance_guard = FinanceGuard()
    transaction = Transaction(1, 100.0, '2022-01-01T12:00:00')
    finance_guard.process_transaction(transaction)
    assert len(finance_guard.log) == 1
    assert finance_guard.log[0]['transaction']['id'] == 1
    assert finance_guard.log[0]['transaction']['amount'] == 100.0

def test_replay():
    finance_guard = FinanceGuard()
    transaction1 = Transaction(1, 100.0, '2022-01-01T12:00:00')
    transaction2 = Transaction(2, 200.0, '2022-01-01T12:00:00')
    finance_guard.process_transaction(transaction1)
    finance_guard.process_transaction(transaction2)
    replay_log = finance_guard.replay(1)
    assert len(replay_log) == 1
    assert replay_log[0]['transaction']['id'] == 1

def test_export_log():
    finance_guard = FinanceGuard()
    transaction = Transaction(1, 100.0, '2022-01-01T12:00:00')
    finance_guard.process_transaction(transaction)
    export_log = finance_guard.export_log()
    assert json.loads(export_log)[0]['transaction']['id'] == 1

def test_replay_empty_log():
    finance_guard = FinanceGuard()
    replay_log = finance_guard.replay(1)
    assert replay_log == []

def test_export_empty_log():
    finance_guard = FinanceGuard()
    export_log = finance_guard.export_log()
    assert json.loads(export_log) == []
