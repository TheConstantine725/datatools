from pathlib import Path
from datafusion import SessionContext


def main():
    ctx = SessionContext()

    df = ctx.read_csv("/mnt/e/.datalake/data.csv")

    print(df.collect())


if __name__ == "__main__":
    main()
