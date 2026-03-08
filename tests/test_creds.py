from datatools.elt.ingestion.datasources.rfam import rfam_datasource
from datatools.elt.ingestion.destinations.filesystem import filesystem


def main():
    pipe = filesystem()

    pipe.dataset_name = rfam_datasource.ref.name
    try:
        print(pipe.run(rfam_datasource))
    except Exception as error:
        print(error)


if __name__ == "__main__":
    main()
