from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class IDBProvider(ABC):
    type: str
    connection_string: str