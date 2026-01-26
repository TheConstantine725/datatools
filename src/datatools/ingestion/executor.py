import dlt


def execute_pipeline(pipeline: dlt.Pipeline, dlt_source: dlt.sources.DltSource):
    print(pipeline.extract(dlt_source), "\n")
    print(pipeline.normalize(), "\n")
    print(pipeline.load(), "\n")
