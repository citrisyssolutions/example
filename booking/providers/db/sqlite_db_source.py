from dataclasses import dataclass
from . import IDBProvider

@dataclass
class SQLiteDBSource(IDBProvider):
    type: str = "sqlite"
    connection_string: str = "sqlite:////tmp/mydb_3.db"