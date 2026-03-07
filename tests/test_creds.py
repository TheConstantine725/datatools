import dlt
from dlt.destinations.impl.ducklake.configuration import DUCKLAKE_STORAGE_PATTERN
from delta_ingest import hello

from datatools.elt import ducklake_pipeline, rfam_datasource


def main():
    hello()


if __name__ == "__main__":
    main()
