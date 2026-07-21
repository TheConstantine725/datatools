from dagster_dbt import DagsterDbtTranslator, DagsterDbtTranslatorSettings
from dagster import AssetKey
from typing import Mapping, Any

class TpchDagsterDbtTranslator(DagsterDbtTranslator):
    def get_asset_key(self, dbt_resource_props: Mapping[str, Any]) -> AssetKey:
        if dbt_resource_props["resource_type"] == "source":
            return AssetKey(["tpch", dbt_resource_props["name"]])
        return super().get_asset_key(dbt_resource_props)
