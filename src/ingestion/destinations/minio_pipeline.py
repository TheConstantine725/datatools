from pathlib import Path
from dlt import secrets
from dlt.destinations import filesystem
import dlt

dlt_output = Path.cwd().joinpath(".dlt/output")


def filesystem_pipeline(pipeline_name: str = __name__):
    pipeline = dlt.pipeline(
        dataset_name="dlt_landing",
        destination=filesystem(**secrets["destination.s3"]),
        pipelines_dir=dlt_output.joinpath("pipelines_dir").as_posix(),
        export_schema_path=dlt_output.joinpath("exp_schema").as_posix(),
        import_schema_path=dlt_output.joinpath("imp_schema").as_posix(),
        pipeline_name=pipeline_name,
        progress="log",
    )

    return pipeline
