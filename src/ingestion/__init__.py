from .datasources.rfam import rfam_datasource
from .destinations.ducklake_pipeline import ducklake_pipeline
from .destinations.clickhouse_pipeline import clickhouse_pipeline
from .destinations.minio_pipeline import filesystem_pipeline

__all__ = [
    "ducklake_pipeline",
    "rfam_datasource",
    "clickhouse_pipeline",
    "filesystem_pipeline",
]
