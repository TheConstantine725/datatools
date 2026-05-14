import traceback
from ingestion.datasources.rfam import rfam_datasource
from ingestion.destinations.minio_pipeline import filesystem_pipeline as pipe


def main():
    try:
        pipeline = pipe("tester").run(data=rfam_datasource, table_format="delta")
    except Exception:
        print(traceback.format_exc())
    else:
        print(pipeline)

if __name__ == "__main__":
    main()
