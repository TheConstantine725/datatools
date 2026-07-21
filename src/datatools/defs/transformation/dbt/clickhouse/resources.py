from dagster_dbt import DbtCliResource, DbtProject
from pathlib import Path

PROJECT_DIR = Path.cwd().joinpath("dbt/clickhouse-project")
PROFILE_DIR = Path.cwd().joinpath(".dbt/clickhouse-project")

CLICKHOUSE_DBT_PROJECT = DbtProject(profiles_dir=PROFILE_DIR, project_dir=PROJECT_DIR)
CLICKHOUSE_DBT_PROJECT.prepare_if_dev()
CLICKHOUSE_DBT_RESOURCE = DbtCliResource(CLICKHOUSE_DBT_PROJECT)
