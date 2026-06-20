import json
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import List
import time
from threading import Thread

@dataclass
class Transaction:
    id: int
    amount: float
    timestamp: datetime

class FinanceGuard:
    def __init__(self):
        self.transactions = []
        self.lock = False

    def submit_batch(self, transactions: List[Transaction]):
        if len(transactions) > 1000:
            raise BackPressureError("Too many transactions")
        start_time = datetime.now()
        for transaction in transactions:
            if self.lock:
                raise BackPressureError("Timeout")
            self.transactions.append(transaction)
        end_time = datetime.now()
        if (end_time - start_time).total_seconds() > 0.1:
            raise BackPressureError("Timeout")
        return {"status": "success"}

    def slow_operation(self):
        self.lock = True
        time.sleep(0.2)
        self.lock = False

class BackPressureError(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

def main():
    finance_guard = FinanceGuard()
    transactions = [Transaction(i, 10.0, datetime.now()) for i in range(100)]
    try:
        result = finance_guard.submit_batch(transactions)
        print(result)
    except BackPressureError as e:
        print(e)

if __name__ == "__main__":
    main()
