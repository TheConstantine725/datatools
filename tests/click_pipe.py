from ingestion import rfam_datasource, clickhouse_pipeline
from traceback import format_exc
import dlt
import polars as pl
from dlt.destinations.adapters import clickhouse_adapter
from dlt.destinations import clickhouse
from pathlib import Path


@dlt.resource(
    name="order_products",
    table_name="order_products",
    primary_key=["order_id", "product_id"],
    write_disposition="append",
)
def data_file():
    path = r"/mnt/e/.datalake/orders.parquet"
    for batch in pl.read_parquet(source=path).iter_slices(8_000):
        yield batch.to_pandas()


def main():
    dest_cred = dlt.secrets[f"destination.clickhouse.test"]
    DLT_OUTPUT = Path.cwd().joinpath(".dlt/output")
    pipeline = dlt.pipeline(
        pipeline_name="order_products",
        export_schema_path=DLT_OUTPUT.joinpath("exported_schema").as_posix(),
        pipelines_dir=DLT_OUTPUT.joinpath("pipeline_dir").as_posix(),
        progress="log",
        destination=clickhouse(**dest_cred),
        dataset_name="stg",
    )
    try:
        clickhouse_adapter(data = data_file, table_engine_type="replacing_merge_tree")
        info = pipeline.run(data_file(), loader_file_format="jsonl",)
    except Exception:
        print("There was an error")
        print(format_exc())
    else:
        return info


if __name__ == "__main__":
    result = main()
    print(result)
