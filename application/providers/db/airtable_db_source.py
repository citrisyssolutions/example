from dataclasses import dataclass
from . import IDBProvider

@dataclass
class AirtableDBSource(IDBProvider):
    connection_string: str = None
    type: str = "sqlite"
    