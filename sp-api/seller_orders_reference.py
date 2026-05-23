"""
Amazon Seller Central Orders API reference pattern.

This file is intentionally non-production and excludes authentication details.
Use it as a structural example for separating API extraction from reporting.
"""

from __future__ import annotations


def build_orders_request_params(created_after: str, marketplace_id: str) -> dict[str, str]:
    """Build sanitized request parameters for an orders extraction pattern."""
    return {
        "CreatedAfter": created_after,
        "MarketplaceIds": marketplace_id,
    }


def normalize_order_record(raw_order: dict) -> dict:
    """Normalize a raw order payload into reporting-friendly fields."""
    return {
        "order_id": raw_order.get("AmazonOrderId"),
        "purchase_date": raw_order.get("PurchaseDate"),
        "order_status": raw_order.get("OrderStatus"),
        "marketplace_id": raw_order.get("MarketplaceId"),
        "fulfillment_channel": raw_order.get("FulfillmentChannel"),
    }
