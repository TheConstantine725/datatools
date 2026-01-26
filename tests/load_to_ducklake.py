from datatools.ingestion.executor import execute_pipeline
from datatools.ingestion.pipelines.ducklake_pipeline import ducklake_pipeline
from datatools.ingestion.sources.rfam import rfam_datasource


def main():
    pipeline = ducklake_pipeline("dlt_rfam_data")
    print(pipeline.extract(rfam_datasource))
    print(pipeline.normalize())
    print(pipeline.load())


if __name__ == "__main__":
    main()
