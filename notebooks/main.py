import marimo

__generated_with = "0.18.4"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import deltalake
    import polars as pl
    from pathlib import Path
    import dotenv
    return Path, mo


@app.cell
def _(mo):
    order_products = mo.sql(
        f"""
        select * from read_csv('/mnt/d/datalake/bucket/groceries/order_products__train.csv');
        """
    )
    return (order_products,)


@app.cell
def _(Path, order_products):
    def load_to_deltalake(provide_table_path: str):
        bucket_path = Path("../.temp/deltalake")
        return bucket_path.joinpath(provide_table_path).absolute()


    order_products.head()
    return (load_to_deltalake,)


@app.cell
def _(load_to_deltalake, order_products):
    order_products.write_delta(
        target=load_to_deltalake("order_products"), mode="overwrite"
    )
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
