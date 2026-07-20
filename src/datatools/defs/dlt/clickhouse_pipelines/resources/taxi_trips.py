import dlt
import duckdb
import pendulum
from dlt.destinations.impl.clickhouse.clickhouse_adapter import clickhouse_adapter

DUCKDB_DB = "/mnt/e/.databases/tpch.duckdb"



@dlt.source(name = "tpch_datasource", parallelized = True)
def collect_tpch_datasource():

    @dlt.resource(name = "line_items",
        table_name = "line_items",
        write_disposition="append",
        primary_key = ["l_orderkey", "l_linenumber"],
        file_format="parquet",
        schema_contract="evolve",
        columns = {"_extraction_timestamp":{"dedup_sort":"desc","nullable":False}},
        parallelized = True,
    )
    def collect_line_items():
        with duckdb.connect(DUCKDB_DB) as duck:
            query = duck.sql(f"""
                select
                *,
                now() as _extraction_timestamp
                from main.lineitem;
                """)
            for batch in query.to_arrow_reader(50_000):
                yield batch


    @dlt.resource(name = "customers",
        table_name = "customers",
        primary_key = ["c_custkey"],
        file_format="parquet",
        schema_contract="evolve",
        columns = {"_extraction_timestamp":{"dedup_sort":"desc","nullable":False}},
        parallelized = True,
    )
    def collect_customers():
        with duckdb.connect(DUCKDB_DB) as duck:
            query = duck.sql(f"""
                select
                *,
                now() as _extraction_timestamp
                from customer;
                """)
            for batch in query.to_arrow_reader(50_000):
                yield batch

    @dlt.resource(name = "nation",
        table_name = "nation",
        primary_key = ["n_nationkey"],
        file_format="parquet",
        schema_contract="evolve",
        columns = {"_extraction_timestamp":{"dedup_sort":"desc","nullable":False}},
        parallelized = True,
    )
    def collect_nation():
        with duckdb.connect(DUCKDB_DB) as duck:
            query = duck.sql(f"""
                select
                *,
                now() as _extraction_timestamp
                from nation;
                """)
            for batch in query.to_arrow_reader(50_000):
                yield batch


    @dlt.resource(name = "orders",
        table_name = "orders",
        primary_key = ["o_orderkey", "o_custkey"],
        file_format = "parquet",
        schema_contract= "evolve",
        columns = {"_extraction_timestamp":{"dedup_sort":"desc","nullable":False}},
        parallelized = True,
    )
    def collect_orders():
        with duckdb.connect(DUCKDB_DB) as duck:
            query = duck.sql("""
                select
                *,
                now() as _extraction_timestamp
                from orders
                """)
            for batch in query.to_arrow_reader(50_000):
                yield batch

    line_items = clickhouse_adapter(
        collect_line_items(),
        table_engine_type="replacing_merge_tree",
        partition="toYYYYMM(l_shipdate)",
        # sort= "_extraction_timestamp"
    )


    return (line_items, collect_customers(), collect_orders(), collect_nation())
