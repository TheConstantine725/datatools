import dlt
from duckdb import DuckDBPyConnection

from datatools import TEMP_DLT_OUTPUT


def ducklake_pipeline(pipeline_name: str):
    from dlt.destinations import ducklake
    from dlt.destinations.impl.ducklake.configuration import DuckLakeCredentials

    credentials = DuckLakeCredentials(
        **dlt.secrets["destination.local_ducklake.credentials"]
    )

    pipeline = dlt.pipeline(
        pipeline_name=pipeline_name,
        destination=ducklake(credentials, staging_dataset_name_layout="_dlt_staging"),
        pipelines_dir=TEMP_DLT_OUTPUT.joinpath("pipelines_dir").absolute().as_posix(),
        export_schema_path=TEMP_DLT_OUTPUT.joinpath("exported_schema")
        .absolute()
        .as_posix(),
        dataset_name="dlt_landing",
        progress="log",
    )

    with pipeline.sql_client() as client:
        conn: DuckDBPyConnection = client.native_connection
        conn.sql("call local_ducklake.set_option('parquet_compression', 'zstd');")
        conn.sql("call local_ducklake.set_option('parquet_compression_level', 16);")
        conn.sql("call local_ducklake.set_option('parquet_version', 2);")
        conn.sql("call local_ducklake.set_option('rewrite_delete_threshold', 0.60);")
        conn.sql("call local_ducklake.set_option('delete_older_than', '7 days');")
        conn.sql("call local_ducklake.set_option('expire_older_than', '7 days');")

    return pipeline
