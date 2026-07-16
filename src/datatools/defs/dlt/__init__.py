# from .resources.rfam import rfam_datasource
from .ducklake_pipelines import ducklake_pipeline
from .clickhouse_pipelines import clickhouse_pipeline
from pathlib import Path


DLT_OUTPUT = Path.cwd().joinpath(".dlt/output")

__all__ = [
    "ducklake_pipeline",
    "clickhouse_pipeline",
]
