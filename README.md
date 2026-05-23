# Marketplace Operations Framework

**Author:** Nikki Firmalino  
**Focus:** Marketplace operations, Amazon SP-API reference patterns, operational reporting, Power BI data workflows, and ecommerce systems architecture.

This repository contains sanitized reference assets for building marketplace operations data workflows across Amazon Seller Central, Vendor Central, and downstream analytics tools such as Power BI.

The goal is not to provide production-ready credentials or proprietary business logic. The goal is to document reusable patterns for extracting marketplace data, staging operational exports, and preparing ecommerce datasets for reporting, forecasting, and performance management.

---

## Repository Purpose

This repo supports an operational ecommerce systems approach:

- Extract marketplace data through API or report workflows
- Stage data in clean export folders
- Prepare Power BI-friendly datasets
- Support marketplace performance reporting
- Improve operational visibility across sales, inventory, advertising, and fulfillment
- Document scalable patterns for ecommerce analytics infrastructure

---

## Core Use Cases

### Seller Central
Typical datasets include:

- Orders
- Order items
- FBA inventory summaries
- Listings and catalog data
- Financial events and settlements
- Returns and reimbursements where available

### Vendor Central
Availability depends on vendor authorization and API enrollment. Typical datasets include:

- Purchase orders
- Shipments
- Invoices
- Direct fulfillment workflows
- Fill rate and lead time reporting

---

## Recommended Analytics Flow

Direct SP-API connections from Power BI are usually not ideal because authentication, AWS SigV4 signing, refresh schedules, and credential rotation can become unstable.

A more scalable pattern is:

```text
Amazon SP-API
→ Scheduled Extractor Script
→ CSV / Parquet Export Layer
→ SharePoint / OneDrive / Data Lake
→ Power BI Semantic Model
→ Executive & Operational Dashboards
```

Use a `latest/` export pattern so Power BI refreshes remain stable while historical snapshots are preserved separately.

---

## Folder Structure

```text
marketplace-operations-framework/
├── docs/        Documentation, architecture notes, and implementation guidance
├── exports/     Placeholder export folders for latest and historical data
├── powerbi/     Power BI modeling notes and sample schema guidance
├── scripts/     Utility scripts and reusable operational patterns
├── sp-api/      Amazon SP-API reference patterns and endpoint notes
└── examples/    Sample sanitized datasets and workflow examples
```

---

## Important Security Notes

Do not store credentials, refresh tokens, client secrets, IAM keys, or production configuration files in source control.

This repository intentionally excludes:

- Production credentials
- Proprietary SQL
- Internal schemas
- Company-specific business logic
- Customer data
- Vendor pricing agreements
- Confidential operational workflows

---

## Positioning

This project reflects an ecommerce operational systems approach, connecting marketplace operations, reporting infrastructure, automation workflows, and business intelligence into scalable decision-support patterns.

