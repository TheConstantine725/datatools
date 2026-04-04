import dlt
from dlt.sources.sql_database import sql_table


@dlt.source(name="rfam_data")
def rfam_datasource():
    creds = dlt.secrets["sources.databases.rfam_database.credentials"]

    family = (
        sql_table(
            credentials=creds,
            table="family",
            backend="pyarrow",
            write_disposition="append",
        )
        .parallelize()
        .apply_hints(table_name="rfam_family", file_format="parquet")
    )

    clan = (
        sql_table(
            credentials=creds,
            table="clan",
            backend="pyarrow",
            write_disposition="append",
        )
        .parallelize()
        .apply_hints(table_name="rfam_clan", file_format="parquet")
    )

    clan_membership = (
        sql_table(
            credentials=creds,
            table="clan_membership",
            backend="pyarrow",
            write_disposition="append",
        )
        .parallelize()
        .apply_hints(table_name="rfam_clan_membership", file_format="parquet")
    )

    full_region = (
        sql_table(
            credentials=creds,
            table="full_region",
            backend="pyarrow",
            write_disposition="append",
        )
        .parallelize()
        .apply_hints(table_name="rfam_full_region", file_format="parquet")
    )

    taxonomy = (
        sql_table(
            credentials=creds,
            table="taxonomy",
            backend="pyarrow",
            write_disposition="append",
        )
        .parallelize()
        .apply_hints(
            table_name="rfam_taxonomy",
            file_format="parquet",
        )
    )

    return (family, clan, clan_membership, taxonomy)
