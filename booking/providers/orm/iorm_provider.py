from abc import ABC, abstractclassmethod
from booking.providers.db import IDBProvider


class IOrmProvider(ABC):
    def __init__(self, provider: IDBProvider):
        self.provider = provider
        self.connection_string = provider.connection_string

    @abstractclassmethod
    def initialize(self):
        pass
