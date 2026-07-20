from dagster import AssetExecutionContext
from dagster_dlt import DagsterDltResource, dlt_assets
from .pipe import clickhouse_pipeline
from .resources.taxi_trips import collect_tpch_datasource

dlt_resource = DagsterDltResource()


@dlt_assets(
    dlt_source= collect_tpch_datasource(),
    dlt_pipeline=clickhouse_pipeline("tpch_ingestion", dataset_prefix="tpch"),
    name="tpch_datasource",
    group_name="ingestion_clickhouse",
)
def tpch_ingestion(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context=context)
