import marimo

__generated_with = "0.22.4"
app = marimo.App(width="full")


@app.cell
def _():
    from pyspark.sql import SparkSession

    return (SparkSession,)


@app.cell
def _(SparkSession):
    spark = SparkSession.builder.getOrCreate()
    return (spark,)


@app.cell
def _(spark):
    spark.sql(""" select 1 as  one """)
    return


@app.cell
def _():
    import marimo as mo

    return


if __name__ == "__main__":
    app.run()
