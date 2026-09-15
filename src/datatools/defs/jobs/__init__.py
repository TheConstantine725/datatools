from dagster import AssetSelection, define_asset_job

clickhouse_elt_job = define_asset_job(
    name="clickhouse_elt_job", selection=AssetSelection.groups("clickhouse_elt")
)
