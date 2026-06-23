import time
from finance_guard import FinanceGuard, Receipt

def test_submit_transaction():
    finance_guard = FinanceGuard("mock-client-id", "mock-client-secret")
    payload = {"amount": 10.99, "description": "Test transaction"}
    receipt = finance_guard.submit_transaction(None, payload)
    assert receipt.transaction_id == "mock-transaction-id"
    assert receipt.status == "success"

def test_submit_transaction_with_expired_jwt():
    finance_guard = FinanceGuard("mock-client-id", "mock-client-secret")
    finance_guard.jwt_token = "mock-jwt-token"
    finance_guard.jwt_expires_at = int(time.time()) - 3600  # Expired JWT token
    payload = {"amount": 10.99, "description": "Test transaction"}
    receipt = finance_guard.submit_transaction(None, payload)
    assert receipt.transaction_id == "mock-transaction-id"
    assert receipt.status == "success"

def test_submit_transaction_with_invalid_jwt():
    finance_guard = FinanceGuard("mock-client-id", "mock-client-secret")
    finance_guard.jwt_token = None
    payload = {"amount": 10.99, "description": "Test transaction"}
    receipt = finance_guard.submit_transaction(None, payload)
    assert receipt.transaction_id == "mock-transaction-id"
    assert receipt.status == "success"
