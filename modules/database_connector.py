import os
from sqlalchemy import create_engine

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