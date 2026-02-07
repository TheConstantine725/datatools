import dlt
from datatools import TEMP_DLT_OUTPUT
from dlt.destinations.impl import ducklake


def ducklake_pipeline(pipeline_name: str):
    pipeline_result = dlt.pipeline(
        pipeline_name=pipeline_name,
        destination="ducklake",
        pipelines_dir=TEMP_DLT_OUTPUT.joinpath("pipelines_dir").absolute().as_posix(),
        export_schema_path=TEMP_DLT_OUTPUT.joinpath("exported_schema").absolute().as_posix(),
        dataset_name="dlt_landing",
        progress="log",
    )
    return pipeline_result
