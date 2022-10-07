from dataclasses import dataclass
from . import IDBProvider

@dataclass
class SQLiteDBSource(IDBProvider):
    connection_string: str = None
    type: str = "sqlite"
    