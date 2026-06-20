import pytest
from finance_guard import FinanceGuard, Transaction, BackPressureError
from datetime import datetime
import threading

def test_submit_batch():
    finance_guard = FinanceGuard()
    transactions = [Transaction(i, 10.0, datetime.now()) for i in range(100)]
    result = finance_guard.submit_batch(transactions)
    assert result["status"] == "success"

def test_submit_batch_too_many_transactions():
    finance_guard = FinanceGuard()
    transactions = [Transaction(i, 10.0, datetime.now()) for i in range(1001)]
    with pytest.raises(BackPressureError):
        finance_guard.submit_batch(transactions)

def test_submit_batch_timeout():
    finance_guard = FinanceGuard()
    transactions = [Transaction(i, 10.0, datetime.now()) for i in range(100)]
    thread = threading.Thread(target=finance_guard.slow_operation)
    thread.start()
    with pytest.raises(BackPressureError):
        finance_guard.submit_batch(transactions)

def test_back_pressure_error():
    error = BackPressureError("Test error")
    assert str(error) == "Test error"
