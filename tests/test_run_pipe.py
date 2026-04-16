from datatools.ingestion import ducklake_pipeline, rfam_datasource
from dlt import secrets

def main():
    try:
        result = ducklake_pipeline().run(rfam_datasource())
    except Exception as error:
        print(error)
    else:
        print(result)

if __name__ == "__main__":
    # print(secrets["destination.ducklake.ingestion.credentials"])
    main()
