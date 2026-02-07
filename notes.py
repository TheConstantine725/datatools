import marimo

__generated_with = "0.18.4"
app = marimo.App(width="full")


@app.cell
def _():
    return


@app.cell
def _():
    import duckdb

    DATABASE_URL = "/mnt/e/.databases/tpch.duckdb"
    tpch = duckdb.connect(DATABASE_URL, read_only=True)
    return (tpch,)


@app.cell
def _(mo, tpch):
    _df = mo.sql(
        f"""
        select * from main.customer;
        """,
        engine=tpch
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
