# Finance Guard

Finance Guard is a Python project that provides a deterministic replay and auditing system for financial transactions.

## Usage

1. Run the project using `python -m finance_guard`.
2. Use the `replay` method to reprocess a specified batch of transactions.
3. Use the `export_log` method to export the audit log in JSON format.

## Testing

1. Run the tests using `pytest`.
2. The tests cover the happy path and edge cases for the `process_transaction`, `replay`, and `export_log` methods.
