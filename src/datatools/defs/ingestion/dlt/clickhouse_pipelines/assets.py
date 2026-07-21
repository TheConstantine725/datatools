from dagster import AssetExecutionContext
from dagster_dlt import dlt_assets, DagsterDltResource

from .pipeline import clickhouse_pipeline
from .data_sources.tpch import collect_tpch_datasource
from .resources import DAGSTER_DLT_RESOURCE
from .translators import TpchDagsterDltTranslator

CLICKHOUSE_INGESTION_GROUP = "clickhouse_ingestion"

@dlt_assets(
    dlt_pipeline=clickhouse_pipeline(pipeline_name="tpch", dataset_prefix="tpch"),
    dlt_source=collect_tpch_datasource(),
    name = "tpch_ingestion",
    group_name = CLICKHOUSE_INGESTION_GROUP,
    dagster_dlt_translator=TpchDagsterDltTranslator()
)
def tpch_ingestion(context: AssetExecutionContext, dlt: DagsterDltResource = DAGSTER_DLT_RESOURCE):
    yield from dlt.run(context=context)
