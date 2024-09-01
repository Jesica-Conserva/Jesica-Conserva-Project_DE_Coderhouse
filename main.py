from dotenv import load_dotenv
import sys
from modules import database_connector, api_connector, persist_data

def main() -> int:
    load_dotenv()
    data = api_connector.get_api_data()
    engine = database_connector.get_database_connection()
    persist_data.persist(data, engine)
    return 0

if __name__ == '__main__':
    sys.exit(main())