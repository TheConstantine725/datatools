from datatools.ingestor import generate_data_paths, DataPathResult
import duckdb

def connect_to_ducklake(duck: duckdb.DuckDBPyConnection):
    duck.install_extension("postgres")
    duck.install_extension("ducklake")
    try:
        duck.sql("attach if not exists 'ducklake:pypelake' as pypelake;")
    except Exception as error:
        print("Failed at attaching ducklake")
        print(error)
        exit()

def load_to_ducklake(table: DataPathResult, duck: duckdb.DuckDBPyConnection):
    try:
        duck.sql("create schema if not exists pypelake.bronze;")
        duck.sql(f"create table if not exists pypelake.bronze.{table.table_name} as (select * from read_csv('{table.full_path}'));")
    except Exception as error:
        print(f"Failed at loading {table.table_name}")
        print(error)
        duck.rollback()
    else:
        print(f"Loaded table {table.table_name}")
        duck.commit()
    
def main():
    with duckdb.connect() as duck:
        # connect_to_ducklake(duck)
        # duck.begin()
        # for _, table in enumerate(generate_data_paths()):
        #     load_to_ducklake(table, duck)
        _left = duck.sql("select main: string_split(secret_string, ';') from duckdb_secrets() where 1 = 1 and type = 'ducklake';").fetchall()
        for i in _left[0][0]:
            print(i)


if __name__ == "__main__":
    main()