import dlt
from dlt.destinations.impl.ducklake.configuration import DUCKLAKE_STORAGE_PATTERN

from datatools.elt import ducklake_pipeline, rfam_datasource


def main():
    pipe = ducklake_pipeline(pipeline_name="testing_rfam_locally")
    print(pipe.run(rfam_datasource), "\n")


if __name__ == "__main__":
    main()
