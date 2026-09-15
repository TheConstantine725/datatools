from dagster_dbt import DbtCliResource, DbtProject, dbt_assets
from dagster import AssetExecutionContext
from pathlib import Path

DBT_MANIFEST_PATH = Path.cwd().joinpath(".dbt/manifests")

if not DBT_MANIFEST_PATH.exists():
    DBT_MANIFEST_PATH.mkdir(parents=True)


@dbt_assets(manifest=DBT_MANIFEST_PATH)
def build_staging(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()
