import json
import hashlib
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Transaction:
    id: int
    amount: float
    timestamp: datetime

class FinanceGuard:
    def __init__(self):
        self.log = []

    def process_transaction(self, transaction: Transaction):
        transaction_dict = transaction.__dict__.copy()
        transaction_dict['timestamp'] = transaction_dict['timestamp'].isoformat()
        transaction_hash = hashlib.sha256(json.dumps(transaction_dict).encode()).hexdigest()
        self.log.append({"transaction": transaction_dict, "hash": transaction_hash})

    def replay(self, batch_id: int):
        batch_log = [entry for entry in self.log if entry["transaction"]["id"] == batch_id]
        return batch_log

    def export_audit_log(self):
        return json.dumps(self.log, default=str)

    def main(self):
        finance_guard = FinanceGuard()
        transaction = Transaction(1, 100.0, datetime.now())
        finance_guard.process_transaction(transaction)
        print(finance_guard.replay(1))
        print(finance_guard.export_audit_log())

if __name__ == "__main__":
    finance_guard = FinanceGuard()
    finance_guard.main()
