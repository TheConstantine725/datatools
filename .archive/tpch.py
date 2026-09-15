import duckdb
import dlt
from dlt.destinations.adapters import clickhouse_adapter


DUCKDB_TPCH = "/mnt/e/.databases/tpch_30.duckdb"


@dlt.resource(
    name="lineitem",
    primary_key=["l_orderkey", "l_partkey", "l_suppkey", "l_linenumber"],
    parallelized=True,
    table_name="line_item",
    write_disposition="append",
    file_format="preferred",
    # columns = {"version":{"dedup_sort":"desc", "nullable":False},
    #     "is_deleted":{"hard_delete": True, "nullable":False}}
)
def line_item():
    with duckdb.connect(DUCKDB_TPCH, read_only=True) as duck:
        for batch in duck.sql("select * from main.lineitem ").to_arrow_reader(500_000):
            yield batch


res_line_item = clickhouse_adapter(
    data=line_item,
    table_engine_type="replacing_merge_tree",
    settings={"clean_deleted_rows": "Always"},
)


@dlt.resource(
    name="orders",
    primary_key=["o_orderkey", "o_custkey"],
    parallelized=True,
    table_name="orders",
    write_disposition="append",
    file_format="preferred",
    # columns = {"version":{"dedup_sort":"desc", "nullable":False},
    #     "is_deleted":{"hard_delete": True, "nullable":False}}
)
def orders():
    with duckdb.connect(DUCKDB_TPCH, read_only=True) as duck:
        for batch in duck.sql("select * from main.orders").to_arrow_reader(500_000):
            yield batch


res_orders = clickhouse_adapter(
    data=orders,
    table_engine_type="replacing_merge_tree",
    settings={"clean_deleted_rows": "Always"},
)


@dlt.source(parallelized=True)
def tpch_datasource():
    return res_line_item, res_orders
