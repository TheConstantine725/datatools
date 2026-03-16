import marimo

__generated_with = "0.20.4"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import deltalake
    import polars as pl
    from pathlib import Path

    return Path, deltalake, mo


@app.cell
def _(Path):
    base = Path("/run/media/kostas/HDD 1/.data")
    databases = base.joinpath("databases")
    datalake = base.joinpath("datalake")
    print(databases)
    print(datalake)

    for _ in databases.iterdir():
        print(_)
    return (datalake,)


@app.cell(hide_code=True)
def _(mo):
    _df = mo.sql(
        f"""
        attach '/run/media/kostas/HDD 1/.data/databases/tpch.duckdb' as tpch;
        use tpch;
        """
    )
    return


@app.cell(hide_code=True)
def _(mo):
    _df = mo.sql(
        f"""
        select * from main.lineitem;
        """
    )
    return


@app.cell
def _(datalake):
    def load_to_deltalake(provide_table_path: str):
        bucket_path = datalake.joinpath("deltalake")
        return bucket_path.joinpath(provide_table_path).absolute()

    return (load_to_deltalake,)


@app.cell
def _(deltalake, load_to_deltalake, order_products):
    order_products.write_delta(
        target=load_to_deltalake("order_products"),
        mode="overwrite",
        delta_write_options={
            "writer_properties": deltalake.WriterProperties(
                compression="zstd", compression_level=14
            )
        },
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
