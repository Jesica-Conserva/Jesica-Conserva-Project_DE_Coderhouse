import requests
from datetime import datetime
import pandas as pd

def get_api_data():
    url = "https://ssd-api.jpl.nasa.gov/fireball.api"

    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            if data:
                #engine = get_database_connection()
                cols:list[str] = ["date","energy","impact_e","lat","lat_dir","lon","lon_dir","alt","vel"]
                data_api:pd.DataFrame = pd.DataFrame(data["data"], columns=cols)
                data = data_api[cols]
                data['created_at'] = datetime.now()
                return data
            else:
                print('falló')
        else:
            print(f"Error al realizar la petición: {response.status_code}")
    except Exception as e:
        print(f"Ocurrió un error al realizar la petición: {e}")