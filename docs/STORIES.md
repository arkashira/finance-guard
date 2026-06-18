# Stories.md – finance-guard

## Overview
`finance-guard` is a transaction‑monitoring and issue‑resolution platform for financial service providers. The backlog below is organized into epics, ordered to deliver a Minimum Viable Product (MVP) first, then incremental enhancements. Each story follows the **“As a \<role\>, I want \<goal\>, so that \<benefit\>”** format and includes clear acceptance criteria.

---

## Epics

| Epic | Description | MVP Priority |
|------|-------------|--------------|
| **E1 – Core Transaction Monitoring** | Ingest, store, and visualise real‑time transaction streams. | 1 |
| **E2 – Alerting & Notification** | Detect anomalous transactions and notify stakeholders. | 2 |
| **E3 – Issue Management** | Create, track, and resolve issues arising from alerts. | 3 |
| **E4 – Reporting & Analytics** | Generate operational and compliance reports. | 4 |
| **E5 – Integration & Data Connectors** | Connect finance‑guard to existing banking systems and data lakes. | 5 |
| **E6 – Security & Access Control** | Enforce role‑based access, audit logging, and data encryption. | 6 |
| **E7 – Admin & Configuration** | Provide UI for system administrators to configure rules, thresholds, and user roles. | 7 |

---

## MVP Stories (Epics E1‑E3)

### **E1 – Core Transaction Monitoring**

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| **E1‑01** | **As a** Financial Operations Analyst, **I want** a real‑time dashboard that shows incoming transactions, **so that** I can see the current processing volume at a glance. | - Dashboard updates within 5 seconds of new transaction arrival.<br>- Shows total count, success/failure split, and average latency.<br>- Supports pagination & date‑range filtering.<br>- Data is persisted for at least 30 days. |
| **E1‑02** | **As a** System Engineer, **I want** the platform to ingest transaction streams via Kafka and REST, **so that** we can integrate with existing pipelines without code changes. | - Supports Kafka topic subscription (configurable topic & consumer group).<br>- Provides a `/api/v1/transactions` POST endpoint (JSON schema validated).<br>- Guarantees at‑least‑once delivery with idempotent storage.<br>- Logs ingestion errors with correlation IDs. |
| **E1‑03** | **As a** Compliance Officer, **I want** each transaction to be stored with immutable audit metadata, **so that** we can prove data integrity for regulatory audits. | - Stores transaction ID, timestamp, source, and SHA‑256 hash of payload.<br>- Writes to append‑only storage (e.g., PostgreSQL `WAL` or immutable object store).<br>- Provides an API to retrieve raw audit record and hash verification. |
| **E1‑04** | **As a** Business Owner, **I want** the system to scale horizontally to handle peak loads of 2 M transactions per minute, **so that** service availability is never compromised. | - Autoscaling policy triggers when CPU > 70 % or queue lag > 10 seconds.<br>- Load tests (k6) demonstrate 2 M txn/min without > 2 seconds latency.<br>- No single point of failure; uses replicated Kafka and DB clusters. |

### **E2 – Alerting & Notification**

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| **E2‑01** | **As a** Financial Operations Analyst, **I want** to define rule‑based alerts (e.g., “transaction amount > $10 k” or “failure rate > 5 % in 5 min”), **so that** abnormal activity is highlighted automatically. | - UI to create/edit/delete alert rules with logical operators.<br>- Rules evaluated in real‑time (≤ 10 seconds latency).<br>- Supports threshold, rate‑of‑change, and pattern‑matching conditions.<br>- Persisted rule versioning. |
| **E2‑02** | **As a** Customer Support Agent, **I want** to receive push notifications via Slack and email when an alert fires, **so that** I can start investigation immediately. | - Configurable notification channels per alert rule.<br>- Message includes alert name, affected transaction IDs, and link to issue ticket.<br>- Delivery within 15 seconds of rule breach.<br>- Retry logic up to 3 attempts with exponential back‑off. |
| **E2‑03** | **As a** Compliance Officer, **I want** alerts to be logged with immutable timestamps, **so that** we have a tamper‑proof audit trail. | - Each alert event stored with UTC timestamp, rule ID, and triggering transaction IDs.<br>- Log entries are write‑once (append‑only) and searchable via API.<br>- Exportable CSV/JSON for external audit tools. |

### **E3 – Issue Management**

| # | User Story | Acceptance Criteria |
|---|------------|---------------------|
| **E3‑01** | **As a** Customer Support Agent, **I want** an issue ticket to be auto‑created when an alert fires, **so that** I have a structured workflow to resolve the problem. | - Ticket includes alert details, affected transactions, and priority (derived from rule severity).<br>- Ticket status defaults to “Open”.<br>- Ticket ID appears in the alert notification. |
| **E3‑
