from typing import Generator, Literal
from sqlalchemy import create_engine, Connection, Engine
import pyarrow as pa


class MergeSpec:
    pass


class Table:
    def __init__(
        self,
        table_name: str,
        ingestion_strategy: Literal["replace", "append", "merge"] = "append",
        merge_spec: MergeSpec | None = None,
    ):
        self.table_name = table_name
        self.ingestion_strategy = None
        if ingestion_strategy == "merge" and not isinstance(merge_spec, MergeSpec):
            raise ValueError(
                "If ingestion strategy is set on merge, then a MergeSpec has to be defined"
            )
        else:
            self.ingestion_strategy = ingestion_strategy
        self.data_generator = None
        self.schema = None

    def attach_data_generator(
        self, data_generator: Generator[pa.Table | pa.RecordBatch, None, None]
    ):
        self.data_generator = data_generator
        return self

    def override_schema(self, schema: pa.Schema):
        self.schema = schema
        return self
