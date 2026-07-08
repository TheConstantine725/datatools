# from .resources.rfam import rfam_datasource
from .resources.tpch import tpch_datasource
from .destinations.ducklake_pipeline import ducklake_pipeline
from .destinations.clickhouse_pipeline import clickhouse_pipeline

__all__ = [
    "ducklake_pipeline",
    # "rfam_datasource",
    "tpch_datasource",
    "clickhouse_pipeline",
]
