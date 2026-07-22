import dagster
from dagster import (
    Definitions,
    load_assets_from_modules,
)
from .defs.transformation.dbt.clickhouse.resources import CLICKHOUSE_DBT_RESOURCE
from .defs.ingestion.dlt.clickhouse_pipelines import assets as clickhouse_dlt_assets
from .defs.ingestion.dlt.clickhouse_pipelines.resources import DAGSTER_DLT_RESOURCE
from .defs.transformation.dbt.clickhouse import assets as clickhouse_dbt_assets
from .defs.admin_assets import CLICKHOUSE_RESOURCE
from .defs import admin_assets

clickhouse_admin_assets = load_assets_from_modules([admin_assets])
clickhouse_ingestion_assets = load_assets_from_modules([clickhouse_dlt_assets])
clickhouse_transformation_assets = load_assets_from_modules([clickhouse_dbt_assets])


defs = Definitions(
    assets=[*clickhouse_ingestion_assets, *clickhouse_transformation_assets, *clickhouse_admin_assets],
    resources={"dlt": DAGSTER_DLT_RESOURCE, "ch_dbt": CLICKHOUSE_DBT_RESOURCE, "clickhouse": CLICKHOUSE_RESOURCE},
)
