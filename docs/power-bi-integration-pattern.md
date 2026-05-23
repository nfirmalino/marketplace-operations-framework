# Power BI Integration Pattern

## Recommended Flow

```text
Amazon SP-API
→ Python / scheduled extractor
→ CSV or Parquet export
→ SharePoint / OneDrive / Data Lake
→ Power BI
```

## Why Avoid Direct API Calls from Power BI?

Direct API calls can create issues with:

- OAuth complexity
- AWS SigV4 signing
- refresh instability
- token rotation
- rate limits
- report refresh failures

## Suggested Data Model

A marketplace reporting model typically maps well to a star schema:

- `dim_date`
- `dim_sku`
- `dim_marketplace`
- `fact_orders`
- `fact_inventory`
- `fact_advertising`
- `fact_fees`
- `fact_returns`

## Refresh Strategy

Use a `latest/` folder for production refreshes and a dated archive for snapshots.

Example:

```text
exports/
├── latest/
│   ├── seller_orders.csv
│   ├── seller_inventory.csv
│   └── vendor_orders.csv
└── archive/
    └── 2026-04-12/
```
