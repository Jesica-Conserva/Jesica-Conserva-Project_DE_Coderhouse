import requests
import os
from dotenv import load_dotenv
from io import StringIO
import pandas as pd
from sqlalchemy import create_engine

def check_tables(engine):
    with engine.begin() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS jess_conserva_coderhouse.fireballs (
            date TIMESTAMP WITHOUT TIME ZONE,
            energy REAL,
            impact_e REAL,
            lat NUMERIC(10, 1),
            lat_dir CHAR(1),
            lon NUMERIC(10, 1),
            lon_dir CHAR(1),
            alt NUMERIC(10, 1),
            vel REAL
            );"""
        )
    

def persist_data(data, engine):
    check_tables(engine)
    schema:str = "jess_conserva_coderhouse"
    table:str = "fireballs"
    data.to_sql(
                name=table,
                con=engine,
                schema=schema,
                if_exists='append',
                index=False
    )
    engine.dispose()

def get_api_data():
    url = "https://ssd-api.jpl.nasa.gov/fireball.api"

    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if data:
                engine = get_database_connection()
                cols:list[str] = ["date","energy","impact_e","lat","lat_dir","lon","lon_dir","alt","vel"]
                data_api:pd.DataFrame = pd.DataFrame(data["data"], columns=cols)
                data = data_api[cols]
                try:
                    data = pd.DataFrame(data)
                    data = data.fillna(0)
                    buffer = StringIO()
                    data.info(buf=buffer)
                    persist_data(data, engine)

        
                except Exception as e:
                    print(f"Not able to import the data from the api\n{e}")
            else:
                print('falló')
        else:
            print(f"Error al realizar la petición: {response.status_code}")
    except Exception as e:
        print(f"Ocurrió un error al realizar la petición: {e}")


def get_database_connection():
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    connection_url = f"postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    print(connection_url)
    try:
        db_engine = create_engine(connection_url)
        return db_engine

    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")

load_dotenv()
get_api_data()