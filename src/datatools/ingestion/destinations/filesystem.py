# def filesystem():
#     import dlt
#     from dlt.destinations import filesystem

#     from datatools import TEMP_DLT_OUTPUT

#     secret = dlt.secrets["destination.fs.credentials"]

#     fs = filesystem(**secret)
#     pipeline = dlt.pipeline(
#         destination=fs,
#         pipelines_dir=TEMP_DLT_OUTPUT.joinpath("pipelines_dir").absolute().as_posix(),
#         export_schema_path=TEMP_DLT_OUTPUT.joinpath("exported_schemas")
#         .absolute()
#         .as_posix(),
#         progress="log",
#     )
#     return pipeline
