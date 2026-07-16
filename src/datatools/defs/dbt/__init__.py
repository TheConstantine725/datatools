from time import sleep
from typing import Literal

from dbt.cli.main import dbtRunner
from psutil import cpu_count

DBT_STREAM_DIRECTION = {
    "upstream": "+{select_node}",
    "downstream": "{select_node}+",
    "full": "+{select_node}+",
}
DBT_STREAMS = Literal["upstream", "downstream", "full"]


class DbtInvoker:
    from os import environ, name
    from pathlib import Path, WindowsPath

    from dotenv import load_dotenv

    _PATH = None
    if name == "nt":
        _PATH = WindowsPath
    else:
        _PATH = Path

    load_dotenv("./.env")

    DBT_PROFILE = _PATH(environ["custom_dbt_profile"]).absolute().as_posix()
    DBT_PROJECT = _PATH(environ["custom_dbt_project"]).absolute().as_posix()

    def __init__(self, target: str = "dev", log_level: str = "info"):
        self.target = target.lower()
        self.log_level = log_level

    def _custom_message(self, message: str, perifix: str = " "):
        msg = message.upper()
        length = int(50 - len(msg) - 1)
        _fix = perifix * length
        print(_fix, msg, _fix)

    def _check_cpu_count(self, threads_inputted: int):
        if cpu_count() < threads_inputted:
            vall = cpu_count() - 2
            print(
                f"Inputted threads more than available, returned available logical processors minus 2: {vall}"
            )
            return cpu_count() - 2
        else:
            return threads_inputted

    def _load_seed(self):
        pass

    def _load_snapshots(self):
        pass

    def _debug_models(self):
        args = [
            "debug",
            "--target",
            self.target,
            "--project-dir",
            self.DBT_PROJECT,
            "--profiles-dir",
            self.DBT_PROFILE,
            "--log-level",
            self.log_level,
        ]
        try:
            self._custom_message("DEBUGGING DBT", "*")
            dbtRunner().invoke(args)
        except Exception as error:
            print()
            self._custom_message("ERROR WHEN DEBUGGING DBT", "_")
            print(error)
            self._custom_message("END OF ERROR WHEN DEBUGGING DBT", "_")
            print()
            return False
        else:
            self._custom_message("DEBUGGING DBT success", "*")
            return True
        finally:
            sleep(1)

    def _run_models(
        self,
        select: str | None = None,
        dag_direction: DBT_STREAMS = "upstream",
        is_full_refresh: bool = False,
        threads: int | None = None,
    ):

        args = [
            "run",
            "--target",
            self.target,
            "--project-dir",
            self.DBT_PROJECT,
            "--profiles-dir",
            self.DBT_PROFILE,
            "--log-level",
            self.log_level,
        ]
        if select is not None:
            args.append("--select")
            args.append(DBT_STREAM_DIRECTION[dag_direction].format(select_node=select))

        if is_full_refresh:
            args.append("--full-refresh")

        if threads is not None:
            _thr = self._check_cpu_count(threads)
            args.append("--threads")
            args.append(f"{_thr}")

        try:
            self._custom_message("running dbt", "*")
            dbtRunner().invoke(args)
        except Exception as error:
            print()
            self._custom_message("error when running dbt", "_")
            print(error)
            self._custom_message("end of error when running dbt", "_")
            print()
        else:
            self._custom_message("running dbt success", "*")
        finally:
            sleep(1)

    def execute(
        self,
        select: str | None = None,
        dag_direction: DBT_STREAMS = "upstream",
        is_full_refresh: bool = False,
        threads: int | None = None,
    ):
        print("=" * 100)
        if self._debug_models():
            self._load_seed()
            self._load_snapshots()
            self._run_models(select, dag_direction, is_full_refresh, threads)
            print("=" * 100)
