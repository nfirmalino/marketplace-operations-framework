# Amazon SP-API Reference Notes

Amazon Selling Partner API supports Seller Central and Vendor Central workflows, depending on authorization.

## Seller Central API Groups

- Orders API
- Reports API
- Catalog Items API
- Listings Items API
- FBA Inventory API
- Finances API

## Vendor Central API Groups

- Vendor Orders API
- Vendor Shipments API
- Vendor Invoices API
- Vendor Direct Fulfillment APIs

## Authentication Layers

Amazon SP-API generally requires:

1. Login with Amazon authorization
2. AWS IAM permissions
3. SP-API application registration
4. Request signing with AWS SigV4

This repo does not include credentials or production authentication logic.
