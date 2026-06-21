from finance_guard import FinanceGuard, Transaction
import json
from datetime import datetime

def test_process_transaction():
    finance_guard = FinanceGuard()
    transaction = Transaction(1, 100.0, datetime.now())
    finance_guard.process_transaction(transaction)
    assert len(finance_guard.log) == 1
    assert finance_guard.log[0]["transaction"]["id"] == 1
    assert finance_guard.log[0]["transaction"]["amount"] == 100.0

def test_replay():
    finance_guard = FinanceGuard()
    transaction1 = Transaction(1, 100.0, datetime.now())
    transaction2 = Transaction(2, 200.0, datetime.now())
    finance_guard.process_transaction(transaction1)
    finance_guard.process_transaction(transaction2)
    replay_log = finance_guard.replay(1)
    assert len(replay_log) == 1
    assert replay_log[0]["transaction"]["id"] == 1

def test_export_audit_log():
    finance_guard = FinanceGuard()
    transaction = Transaction(1, 100.0, datetime.now())
    finance_guard.process_transaction(transaction)
    audit_log = finance_guard.export_audit_log()
    assert json.loads(audit_log)[0]["transaction"]["id"] == 1

def test_replay_empty_log():
    finance_guard = FinanceGuard()
    replay_log = finance_guard.replay(1)
    assert replay_log == []

def test_export_empty_log():
    finance_guard = FinanceGuard()
    audit_log = finance_guard.export_audit_log()
    assert audit_log == "[]"
