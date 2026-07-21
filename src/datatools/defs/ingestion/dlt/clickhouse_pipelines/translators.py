from dagster_dlt import DagsterDltTranslator
from dagster import AssetKey
from dlt.sources import DltResource

class TpchDagsterDltTranslator(DagsterDltTranslator):
    def get_asset_key(self, resource: DltResource) -> AssetKey:
        return AssetKey(["tpch", str(resource.name)])
