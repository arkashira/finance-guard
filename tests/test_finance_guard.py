import pytest
from finance_guard import FinanceGuard, BackPressureHandler, Transaction

@pytest.fixture
def back_pressure_handler():
    return BackPressureHandler(max_queue_size=10, max_processing_time=0.1)

@pytest.fixture
def finance_guard(back_pressure_handler):
    return FinanceGuard(back_pressure_handler)

def test_add_transaction(back_pressure_handler):
    transaction = Transaction(id=1, amount=10.0)
    assert back_pressure_handler.add_transaction(transaction) == True
    assert len(back_pressure_handler.queue) == 1

def test_add_transaction_max_queue_size(back_pressure_handler):
    for i in range(10):
        transaction = Transaction(id=i, amount=10.0)
        back_pressure_handler.add_transaction(transaction)
    transaction = Transaction(id=11, amount=10.0)
    assert back_pressure_handler.add_transaction(transaction) == False
    assert len(back_pressure_handler.queue) == 10

def test_process_transactions(back_pressure_handler):
    for i in range(5):
        transaction = Transaction(id=i, amount=10.0)
        back_pressure_handler.add_transaction(transaction)
    processed_transactions = back_pressure_handler.process_transactions()
    assert len(processed_transactions) == 5
    assert len(back_pressure_handler.queue) == 0

def test_handle_transaction(finance_guard):
    transaction = Transaction(id=1, amount=10.0)
    assert finance_guard.handle_transaction(transaction) == True

def test_handle_transaction_max_queue_size(finance_guard):
    for i in range(10):
        transaction = Transaction(id=i, amount=10.0)
        finance_guard.handle_transaction(transaction)
    transaction = Transaction(id=11, amount=10.0)
    assert finance_guard.handle_transaction(transaction) == False
