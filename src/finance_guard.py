import json
from dataclasses import dataclass
from datetime import datetime, timedelta
import hashlib
import hmac
import time

@dataclass
class Receipt:
    transaction_id: str
    status: str

class FinanceGuard:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.jwt_token = None
        self.jwt_expires_at = 0

    def _fetch_jwt_token(self):
        payload = {
            "client_id": self.client_id,
            "client_secret": self.client_secret,
            "expires_in": 3600  # 1 hour
        }
        headers = {"Content-Type": "application/json"}
        # Simulate fetching JWT token from Transit auth service
        # In a real implementation, this would be a network request
        self.jwt_token = "mock-jwt-token"
        self.jwt_expires_at = int(time.time()) + 3600

    def _sign_request(self, payload):
        if not self.jwt_token or int(time.time()) > self.jwt_expires_at:
            self._fetch_jwt_token()
        signature = hmac.new(self.jwt_token.encode(), json.dumps(payload).encode(), hashlib.sha256).hexdigest()
        return signature

    def submit_transaction(self, ctx, payload):
        signature = self._sign_request(payload)
        # Simulate submitting transaction to server
        # In a real implementation, this would be a network request
        receipt = Receipt(transaction_id="mock-transaction-id", status="success")
        return receipt
