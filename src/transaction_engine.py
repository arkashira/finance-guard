import json
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

@dataclass
class Transaction:
    id: int
    sequence_number: int
    user_id: int
    timestamp: str

class TransactionEngine:
    def __init__(self):
        self.transactions = {}
        self.replay_log = {}

    def process_transaction(self, transaction: Transaction):
        self.transactions[transaction.id] = transaction

    def replay(self, sequence_number: int):
        if sequence_number in [t.sequence_number for t in self.replay_log.values() if isinstance(t, Transaction)]:
            return f"Replay of sequence number {sequence_number} already completed"
        transactions_to_replay = [t for t in self.transactions.values() if t.sequence_number == sequence_number]
        for transaction in transactions_to_replay:
            self.replay_log[transaction.id] = transaction
        return f"Replay of sequence number {sequence_number} completed"

    def get_replay_log(self, sequence_number: int):
        return {k: v for k, v in self.replay_log.items() if v.sequence_number == sequence_number}

def create_transaction_engine():
    return TransactionEngine()
