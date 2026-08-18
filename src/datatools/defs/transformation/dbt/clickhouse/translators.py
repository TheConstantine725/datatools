from dagster_dbt import DagsterDbtTranslator, DagsterDbtTranslatorSettings, DbtProject
from dagster import AssetKey, AssetSpec
from typing import Mapping, Any, Optional


class TpchDagsterDbtTranslator(DagsterDbtTranslator):
    def get_asset_key(self, dbt_resource_props: Mapping[str, Any]) -> AssetKey:
        if dbt_resource_props["resource_type"] == "source":
            return AssetKey(["tpch", dbt_resource_props["name"]])
        return super().get_asset_key(dbt_resource_props)


def custom_dbt_translator(asset_key_prefix: str, group_name: str):

    class _InternalDagsterDbtTranslator(DagsterDbtTranslator):
        def get_asset_key(self, dbt_resource_props: Mapping[str, Any]) -> AssetKey:
            if dbt_resource_props["resource_type"] == "source":
                return AssetKey([asset_key_prefix, dbt_resource_props["name"]])
            return super().get_asset_key(dbt_resource_props)

        def get_group_name(self, dbt_resource_props: Mapping[str, Any]) -> str | None:
            return group_name

    return _InternalDagsterDbtTranslator()
