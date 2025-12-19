from typing import NamedTuple
from pathlib import Path
import duckdb

class DataPathResult(NamedTuple):
    full_path: str
    table_name: str
    file_extension: str


def generate_data_paths():
    for _path in Path("/mnt/e/datalake/nba_data/csv").iterdir():
        full_path = _path
        table_name = (split_of_path:=_path.name.split(".", 1))[0]
        file_extension = split_of_path[1]
        yield DataPathResult(full_path.as_posix(), table_name, file_extension)