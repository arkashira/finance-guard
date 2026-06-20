import json
from dataclasses import dataclass
from typing import List

@dataclass
class Transaction:
    id: int
    amount: float

class BackPressureHandler:
    def __init__(self, max_queue_size: int, max_processing_time: float):
        self.max_queue_size = max_queue_size
        self.max_processing_time = max_processing_time
        self.queue = []

    def add_transaction(self, transaction: Transaction):
        if len(self.queue) < self.max_queue_size:
            self.queue.append(transaction)
            return True
        else:
            return False

    def process_transactions(self):
        processed_transactions = []
        for transaction in self.queue:
            # Simulate processing time
            import time
            time.sleep(self.max_processing_time)
            processed_transactions.append(transaction)
        self.queue = []
        return processed_transactions

class FinanceGuard:
    def __init__(self, back_pressure_handler: BackPressureHandler):
        self.back_pressure_handler = back_pressure_handler

    def handle_transaction(self, transaction: Transaction):
        if self.back_pressure_handler.add_transaction(transaction):
            return True
        else:
            return False

    def process_transactions(self):
        return self.back_pressure_handler.process_transactions()
