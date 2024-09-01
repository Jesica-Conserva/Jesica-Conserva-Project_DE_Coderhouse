import pandas as pd
from io import StringIO

def check_tables(engine):
    with engine.begin() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS public.fireballs (
            date TIMESTAMP WITHOUT TIME ZONE,
            energy REAL,
            impact_e REAL,
            lat NUMERIC(10, 1),
            lat_dir CHAR(1),
            lon NUMERIC(10, 1),
            lon_dir CHAR(1),
            alt NUMERIC(10, 1),
            vel REAL,
            created_at TIMESTAMP WITHOUT TIME ZONE
            );"""
            #SORTKEY(date, lat, lon);"""
        )
        
def persist(data, engine):
    try:
        data = pd.DataFrame(data)
        data = data.fillna(0)
        buffer = StringIO()
        data.info(buf=buffer)
        
    except Exception as e:
        print(f"Not able to import the data from the api\n{e}")

    check_tables(engine)
    schema:str = "public"
    table:str = "fireballs"
    data.to_sql(
                name=table,
                con=engine,
                schema=schema,
                if_exists='replace',
                index=False
    )
    engine.dispose()