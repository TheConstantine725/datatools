from dagster import AssetExecutionContext, AssetKey
from dagster_dlt import dlt_assets, DagsterDltResource

from .pipeline import clickhouse_pipeline
from .data_sources.tpch import collect_tpch_datasource
from .resources import DAGSTER_DLT_RESOURCE
from .translators import TpchDagsterDltTranslator, callable_dlt_translator
CLICKHOUSE_INGESTION_GROUP = "clickhouse_ingestion"


@dlt_assets(
    dlt_pipeline=clickhouse_pipeline(
        pipeline_name="tpch_ingestion", dataset_prefix="tpch"
    ),
    dlt_source=collect_tpch_datasource(),
    name="tpch_ingestion",
    dagster_dlt_translator=callable_dlt_translator(key_prefix="tpch",
        deps = [AssetKey("initialize_clickhouse")],
        ),
)
def tpch_ingestion(
    context: AssetExecutionContext, dlt: DagsterDltResource = DAGSTER_DLT_RESOURCE
):
    yield from dlt.run(context=context)
