from dagster_clickhouse import ClickhouseResource
from dagster import asset, AssetExecutionContext


@asset(name = "initialize_clickhouse", group_name="admin_tasks", kinds={"clickhouse"})
def initialize_clickhouse(context: AssetExecutionContext, clickhouse: ClickhouseResource):
    with clickhouse.get_connection() as conn:
        conn.execute(query = """
create database if not exists data_landing;
            """)
        context.log.info("Creating database for dlt's data_landing")

CLICKHOUSE_RESOURCE = ClickhouseResource(database = "default",host="localhost", port = 9000, user = "admin", password = "admin")
