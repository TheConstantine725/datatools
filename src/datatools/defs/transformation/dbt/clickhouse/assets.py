from pathlib import Path
from dagster import AssetExecutionContext
from dagster_dbt import dbt_assets, DbtCliResource
from .resources import CLICKHOUSE_DBT_RESOURCE, CLICKHOUSE_DBT_PROJECT
from .translators import TpchDagsterDbtTranslator

@dbt_assets(
    manifest=CLICKHOUSE_DBT_PROJECT.manifest_path,
    project=CLICKHOUSE_DBT_PROJECT,
    dagster_dbt_translator=TpchDagsterDbtTranslator(),
    name = "tpch_dbt",
)
def clickhouse_dbt_transformation(context: AssetExecutionContext, ch_dbt:DbtCliResource = CLICKHOUSE_DBT_RESOURCE):
    yield from ch_dbt.cli(["build"], context=context).stream()
