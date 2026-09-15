from pathlib import Path
from dagster import AssetExecutionContext
from dagster_dbt import dbt_assets, DbtCliResource
from .resources import CLICKHOUSE_DBT_PROJECT
from .translators import TpchDagsterDbtTranslator, custom_dbt_translator


@dbt_assets(
    manifest=CLICKHOUSE_DBT_PROJECT.manifest_path,
    project=CLICKHOUSE_DBT_PROJECT,
    dagster_dbt_translator=custom_dbt_translator(
        "tpch",
        group_name="clickhouse_tranformation_staging",
    ),
    name="tpch_dbt",
)
def clickhouse_dbt_transformation(
    context: AssetExecutionContext, ch_dbt: DbtCliResource
):
    yield from ch_dbt.cli(["build"], context=context).stream()
