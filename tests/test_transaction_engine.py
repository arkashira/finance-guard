import pytest
from src.transaction_engine import Transaction, TransactionEngine
from datetime import datetime

@pytest.fixture
def transaction_engine():
    return TransactionEngine()

def test_process_transaction(transaction_engine):
    transaction = Transaction(1, 1, 1, "2022-01-01 12:00:00")
    transaction_engine.process_transaction(transaction)
    assert transaction_engine.transactions[1].id == 1

def test_replay(transaction_engine):
    transaction = Transaction(1, 1, 1, "2022-01-01 12:00:00")
    transaction_engine.process_transaction(transaction)
    result = transaction_engine.replay(1)
    assert result == "Replay of sequence number 1 completed"

def test_replay_log(transaction_engine):
    transaction = Transaction(1, 1, 1, "2022-01-01 12:00:00")
    transaction_engine.process_transaction(transaction)
    transaction_engine.replay(1)
    replay_log = transaction_engine.get_replay_log(1)
    assert len(replay_log) == 1

def test_replay_idempotent(transaction_engine):
    transaction = Transaction(1, 1, 1, "2022-01-01 12:00:00")
    transaction_engine.process_transaction(transaction)
    transaction_engine.replay(1)
    result = transaction_engine.replay(1)
    assert result == "Replay of sequence number 1 already completed"

def test_replay_performance(transaction_engine):
    transactions = [Transaction(i, 1, 1, "2022-01-01 12:00:00") for i in range(1000)]
    for transaction in transactions:
        transaction_engine.process_transaction(transaction)
    import time
    start_time = time.time()
    transaction_engine.replay(1)
    end_time = time.time()
    assert end_time - start_time < 0.1
