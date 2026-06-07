import marimo

__generated_with = "0.23.6"
app = marimo.App(width="full")


@app.cell
def _():
    return


@app.cell
def _():
    import clickhouse_connect

    engine = clickhouse_connect.get_client(
        host="localhost",
        user="ch_admin",
        secure=False,
        port=8123,
    )
    return (engine,)


@app.cell
def _():
    return


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM data_landing.mainar
        """,
        engine=engine,
    )
    return


@app.cell
def _(engine, mo):
    _df = mo.sql(
        f"""
        SELECT * FROM data_landing.mainar LIMIT 100
        """,
        engine=engine,
    )
    return


if __name__ == "__main__":
    app.run()
