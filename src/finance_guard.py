import json
import hashlib
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Transaction:
    id: int
    amount: float
    timestamp: str

class FinanceGuard:
    def __init__(self):
        self.log = []

    def process_transaction(self, transaction: Transaction):
        transaction_hash = self._calculate_hash(transaction)
        self.log.append({
            'transaction': transaction.__dict__,
            'hash': transaction_hash,
            'timestamp': datetime.now().isoformat()
        })

    def _calculate_hash(self, transaction: Transaction):
        transaction_str = json.dumps(transaction.__dict__, sort_keys=True)
        return hashlib.sha256(transaction_str.encode()).hexdigest()

    def replay(self, batch_id: int):
        batch_log = [entry for entry in self.log if entry['transaction']['id'] == batch_id]
        return batch_log

    def export_log(self):
        return json.dumps(self.log, indent=4)

def main():
    finance_guard = FinanceGuard()
    transaction = Transaction(1, 100.0, '2022-01-01T12:00:00')
    finance_guard.process_transaction(transaction)
    print(finance_guard.replay(1))
    print(finance_guard.export_log())

if __name__ == '__main__':
    main()
