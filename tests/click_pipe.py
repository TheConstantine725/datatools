from  ingestion import rfam_datasource, clickhouse_pipeline
from traceback import format_exc

def main():
    try:
        info = clickhouse_pipeline(credential_alias="test", pipeline_name="rfam_datasource").run(rfam_datasource,
            loader_file_format="jsonl", )
    except Exception:
        print("There was an error")
        print(format_exc())
    else:
        return info

if __name__ == "__main__":
    result = main()
    print(result)
