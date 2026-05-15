import marimo

__generated_with = "0.22.4"
app = marimo.App(width="full")


@app.cell
def _():
    from pyspark.sql import SparkSession
    # from pyspark.sql.types import StructType

    session = SparkSession.builder.remote("sc://localhost:15002").appName(
        "Testing Pyspark"
    )

    # df = session.sql("select 1").show()
    return


if __name__ == "__main__":
    app.run()
