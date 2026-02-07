from datatools.ingestion.pipelines.ducklake_pipeline import ducklake_pipeline
from datatools.ingestion.sources.rfam import rfam_datasource
import shutil


def ingestion():
    pipeline = ducklake_pipeline("dlt_rfam_data")
    
    print(pipeline.run(rfam_datasource))

def transform():
    from dbt.cli.main import dbtRunner, dbtRunnerResult
    from pathlib import Path
    dbt_profile_path = Path.cwd().joinpath(".dbt").absolute().as_posix()
    cli_args = [
            "run",
            "--select", "@tpch",
            # "--target", "dev",
            "--project-dir",
            "src/datatools/transformation",
            # "--profiles-dir", ".dbt",
            "--profiles-dir",
            f"{dbt_profile_path}",
            # "--profile", "transformations",
            "--log-level",
            "info",
        ]
    runner = dbtRunner()
    dbt_result: dbtRunnerResult = runner.invoke(cli_args)
    print(dbt_result)

def main():
    # ingestion()
    transform()
    
if __name__ == "__main__":
    main()
