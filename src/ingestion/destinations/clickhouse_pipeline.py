from pathlib import Path
from dlt.destinations import clickhouse
import dlt

DLT_OUTPUT = Path.cwd().joinpath(".dlt/output")


def clickhouse_pipeline(pipeline_name: str, credential_alias: str = "test"):
    dest_cred = dlt.secrets[f"destination.clickhouse.{credential_alias}"]
    pipeline = dlt.pipeline(
        pipeline_name=pipeline_name,
        export_schema_path=DLT_OUTPUT.joinpath("exported_schema").as_posix(),
        pipelines_dir=DLT_OUTPUT.joinpath("pipeline_dir").as_posix(),
        progress="log",
        destination=clickhouse(**dest_cred),
        dataset_name="",
    )

    return pipeline
