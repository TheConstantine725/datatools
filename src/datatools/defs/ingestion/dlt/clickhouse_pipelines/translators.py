from typing import Iterable, Any

from dagster_dlt import DagsterDltTranslator
from dagster_dlt.translator import DltResourceTranslatorData
from dagster import AssetKey, AssetSpec
from dlt.sources import DltResource


class TpchDagsterDltTranslator(DagsterDltTranslator):
    def get_asset_key(self, resource: DltResource) -> AssetKey:
        return AssetKey(["tpch", str(resource.name)])


def callable_dlt_translator(
    key_prefix: str, group_name: str | None = None, deps: Iterable | None = None
):
    class _InnerDagsterDltTranslator(DagsterDltTranslator):
        def get_asset_spec(self, data: DltResourceTranslatorData) -> AssetSpec:
            base_spec = super().get_asset_spec(data)
            replaced: dict[str, Any] = {"key": AssetKey([key_prefix, str(data.resource.name)])}

            if group_name:
                replaced["group_name"] = group_name
            if deps:
                replaced["deps"] = deps
            return base_spec.replace_attributes(**replaced)

    return _InnerDagsterDltTranslator()
