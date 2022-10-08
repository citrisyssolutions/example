import os
from application.providers.db.sqlite_db_source import SQLiteDBSource
from application.providers.db.sqlite_db_source import SQLiteDBSource

class Config:
    # DB_CONNECTION_STRING = os.environ.get("DB_CONNECTION_STRING", "sqlite:////tmp/mydb_3.db")
    # DB_SOURCE = SQLiteDBSource(connection_string=DB_CONNECTION_STRING)
    DB_CONNECTION_STRING = os.environ.get("DB_CONNECTION_STRING", "airtable://:keyvFVTECSngawPxK@appeGrlit5GKyPLX0")
    DB_SOURCE = SQLiteDBSource(connection_string=DB_CONNECTION_STRING)
    
    