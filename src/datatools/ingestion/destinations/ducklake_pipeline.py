import dlt
from dlt.destinations.impl.ducklake.factory import ducklake
from duckdb import DuckDBPyConnection


def test_if_setup(duck: DuckDBPyConnection, ducklake_name: str):
    print(f"Testing if Ducklake {ducklake_name} is setup")
    try:
        result = duck.sql(
            f"select is_ducklake_setup from {ducklake_name}.metadata.setup_indicator;"
        )
    except Exception as error:
        print(error)
        return False
    else:
        print(f"Ducklake ({ducklake_name}) is Setup", result.fetchall()[0][0])
        return True


def config_ducklake(duck: DuckDBPyConnection, ducklake_name: str):
    configs = dlt.secrets[f"destination.ducklake.ingestion.config"]
    result = None
    for key, value in configs.items():
        try:
            duck.sql(
                query=f"call {ducklake_name}.set_option($key, $value); ",
                params={"key": key, "value": value},
            )
        except Exception as error:
            print(error)
            print(
                f"Error in the implementation of the following global config => {key=}{value=}"
            )
            result = False
            break
        else:
            print(
                f"Ducklake ({ducklake_name}) Global Configuration Completed Gracefully "
            )
            result = True
    return result


def create_setup_indicator_in_target_system(
    duck: DuckDBPyConnection, ducklake_name: str
):

    duck.begin()
    try:
        print(f"Marking Ducklake ({ducklake_name=}) Setup Indicator")
        duck.sql(f"""
            create schema if not exists {ducklake_name}.metadata;
            create table if not exists {ducklake_name}.metadata.setup_indicator
            as
            select
                is_ducklake_setup: true,
                ducklake_setup_datetime: now()
            ;
            """)
    except Exception as error:
        print(error)
        duck.rollback()
    else:
        duck.commit()


def ducklake_pipeline():
    from pathlib import Path
    from re import match, sub

    import dlt
    from dlt.destinations.impl.ducklake.configuration import DuckLakeCredentials
    from duckdb import DuckDBPyConnection

    dlt_output = Path.cwd().joinpath(".dlt/output")

    dest_creds = dlt.secrets[f"destination.ducklake.ingestion.credentials"]
    ducklake_name = dest_creds["ducklake_name"]

    ducklake_credentials = DuckLakeCredentials(
        **dlt.secrets[f"destination.ducklake.ingestion.credentials"]
    )

    pipeline = dlt.pipeline(
        pipelines_dir=dlt_output.joinpath("pipelines_dir").as_posix(),
        export_schema_path=dlt_output.joinpath("exp_schema").as_posix(),
        import_schema_path=dlt_output.joinpath("imp_schema").as_posix(),
        dataset_name="dlt_landing",
        destination=ducklake(
            ducklake_credentials,
        ),
        progress="log",
    )
    with pipeline.sql_client() as conn:
        cursor: DuckDBPyConnection = conn.native_connection
        if not test_if_setup(cursor, ducklake_name):
            config_ducklake(cursor, ducklake_name)
            create_setup_indicator_in_target_system(cursor, ducklake_name)
        cursor.sql(f"from {ducklake_credentials.ducklake_name}.options(); ").show()
    return pipeline
