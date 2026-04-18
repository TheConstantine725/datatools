from dbt.cli.main import dbtRunner, dbtRunnerResult
from pathlib import Path


def main():
    TARGET = "dev"
    _path = Path.cwd().joinpath(".dbt").absolute().as_posix()

    debug_args = [
        "debug",
        # "--select",
        # "@kaggle_retails",
        "--target",
        TARGET,
        "--project-dir",
        "src/datatools/transformation",
        "--profiles-dir",
        f"{_path}",
        "--log-level",
        "info",
    ]

    run_args = [
        "run",
        "--target",
        TARGET,
        "--project-dir",
        "src/datatools/transformation",
        "--profiles-dir",
        f"{_path}",
        "--log-level",
        "info",
    ]

    generic_runner = dbtRunner()

    debug_run_result: dbtRunnerResult = generic_runner.invoke(debug_args)
    generic_runner.invoke(run_args)


if __name__ == "__main__":
    main()
