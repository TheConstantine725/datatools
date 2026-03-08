<<<<<<< HEAD
from datatools.elt.ingestion.datasources.rfam import rfam_datasource
from datatools.elt.ingestion.destinations.filesystem import filesystem


def main():
    pipe = filesystem()

    pipe.dataset_name = rfam_datasource.ref.name
    try:
        print(pipe.run(rfam_datasource))
    except Exception as error:
        print(error)
=======
import dlt
from dlt.destinations.impl.ducklake.configuration import DUCKLAKE_STORAGE_PATTERN
from delta_ingest import hello

from datatools.elt import ducklake_pipeline, rfam_datasource


def main():
    hello()
>>>>>>> a67a7f6e81461fa1adfda4fd178e91a223c4ffdd


if __name__ == "__main__":
    main()
