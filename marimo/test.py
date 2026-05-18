import marimo

__generated_with = "0.22.4"
app = marimo.App(width="full")


@app.cell
def _():
    from pyspark.sql import SparkSession
    from time import time

    spark = SparkSession.builder.master("local[*]").appName(f"Test 2").getOrCreate()
    return (spark,)


@app.cell
def _(spark):
    df = spark.read.csv(path="/mnt/e/.datalake/data.csv")
    df.createOrReplaceTempView(name="kaggle_data")
    return


@app.cell
def _(spark):
    import ibis

    spark_ibis = ibis.pyspark.connect(session=spark)
    return (spark_ibis,)


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(kaggle_data, mo, spark_ibis):
    _df = mo.sql(
        f"""
        SELECT * FROM kaggle_data
        """,
        engine=spark_ibis
    )
    return


if __name__ == "__main__":
    app.run()
