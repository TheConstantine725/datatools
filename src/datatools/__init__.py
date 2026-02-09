from pathlib import Path

TEMP_DLT_OUTPUT = Path.cwd().joinpath(".temp").joinpath("dlt_outputs")
DATABASE = Path.home().joinpath("projects/databases")
DATALAKE = Path.home().joinpath("projects/datalake")


def setup():
    for _ in (DATABASE, DATALAKE):
        if not _.exists():
            _.mkdir(parents=True, exist_ok=True)


setup()
