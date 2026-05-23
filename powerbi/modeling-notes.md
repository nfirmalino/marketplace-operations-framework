# Power BI Modeling Notes

## Suggested Tables

### Dimensions
- Date
- SKU / Product
- Marketplace
- Channel
- Fulfillment Method

### Facts
- Orders
- Order Items
- Inventory Snapshots
- Advertising Performance
- Fees and Settlements
- Returns

## Example Measures

```DAX
Net Sales = SUM(fact_orders[net_sales])

Units Sold = SUM(fact_orders[units])

YoY Net Sales =
CALCULATE(
    [Net Sales],
    SAMEPERIODLASTYEAR(dim_date[date])
)

YoY Growth % =
DIVIDE([Net Sales] - [YoY Net Sales], [YoY Net Sales])
```

## Reporting Concepts

- Executive KPI summary
- Marketplace comparison
- SKU/product performance lookup
- Inventory health dashboard
- Forecasting and replenishment view
- Profitability and fee visibility
