"""
Sanitized export pattern for marketplace operations reporting.

This is a reference pattern only. It does not include production credentials,
proprietary endpoints, or internal business logic.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from datetime import datetime, timezone
import csv


@dataclass(frozen=True)
class ExportConfig:
    export_root: Path = Path("exports")
    dataset_name: str = "seller_orders"


def get_sample_rows() -> list[dict[str, object]]:
    """Return sanitized demo rows for a marketplace export."""
    return [
        {"order_id": "ORDER-001", "sku": "SKU-001", "marketplace": "Marketplace A", "net_sales": 125.50, "units": 2},
        {"order_id": "ORDER-002", "sku": "SKU-002", "marketplace": "Marketplace B", "net_sales": 89.99, "units": 1},
    ]


def write_csv(rows: list[dict[str, object]], path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        raise ValueError("No rows supplied for export.")

    with path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def run_export(config: ExportConfig) -> None:
    rows = get_sample_rows()
    date_key = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    latest_path = config.export_root / "latest" / f"{config.dataset_name}.csv"
    archive_path = config.export_root / "archive" / date_key / f"{config.dataset_name}.csv"

    write_csv(rows, latest_path)
    write_csv(rows, archive_path)

    print(f"Exported {len(rows)} rows to {latest_path} and {archive_path}")


if __name__ == "__main__":
    run_export(ExportConfig())
