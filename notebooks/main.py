import marimo

__generated_with = "0.18.4"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import deltalake
    import polars as pl
    from pathlib import Path
    return Path, deltalake, mo


@app.cell
def _(mo):
    order_products = mo.sql(
        f"""
        select * from read_csv('/mnt/d/datalake/bucket/groceries/order_products__train.csv');
        """
    )
    return (order_products,)


@app.cell
def _(Path):
    def load_to_deltalake(provide_table_path: str):
        bucket_path = Path("/mnt/d/datalake/bucket/deltalake")
        return bucket_path.joinpath(provide_table_path).absolute().as_uri()
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
