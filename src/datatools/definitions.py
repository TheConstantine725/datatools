import dagster
from dagster import Definitions, load_assets_from_modules, load_assets_from_package_module
from .defs.dlt import clickhouse_pipelines

from dagster_dlt import DagsterDltResource

clickhouse_ingestion_assets = load_assets_from_package_module(package_module=clickhouse_pipelines)


defs = Definitions(
    assets=[*clickhouse_ingestion_assets],
    resources={"dlt": DagsterDltResource()}
)
