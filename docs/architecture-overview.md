# Architecture Overview

## Marketplace Operations Data Flow

```text
Marketplace APIs / Reports
        ↓
Scheduled Extractor Layer
        ↓
Raw Export Files
        ↓
Data Cleaning & Standardization
        ↓
Power BI Semantic Model
        ↓
Operational Dashboards
        ↓
Business Decisions
```

## Design Principles

- Keep API extraction separate from reporting tools
- Store clean exports in predictable folder paths
- Preserve historical snapshots where possible
- Maintain a stable `latest/` dataset for Power BI refreshes
- Validate API data against marketplace UI reports
- Avoid embedding credentials in scripts or dashboards

## Operational Reporting Domains

- Sales performance
- Unit velocity
- Inventory health
- Fulfillment performance
- Advertising efficiency
- Fees and profitability
- Returns and reimbursements
- Vendor and supplier operations
