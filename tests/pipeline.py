from ingestion.resources.tpch import res_line_item, res_orders, tpch_datasource
from ingestion.destinations.clickhouse_pipeline import clickhouse_pipeline




def load_pipeline():
    pipeline = clickhouse_pipeline(
        credential_alias="test", dataset_prefix="tcph",pipeline_name="tpch_pipeline"
    )

    return pipeline.run(tpch_datasource(), loader_file_format="parquet")


def main():
    result = load_pipeline()
    print(result)


if __name__ == "__main__":
    main()
