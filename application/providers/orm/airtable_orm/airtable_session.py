from dataclasses import asdict, dataclass
import requests, json

@dataclass
class IBase:
    pass


class AirtableSession:
    def __init__(self, api_key, app_key, table_name = None):
        self.api_key = api_key
        self.app_key = app_key
        self.table_name = table_name
        self.data = []

    def __get_api_url(self, table_name):
        self.headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
        return f"https://api.airtable.com/v0/{self.app_key}/{table_name}"

    def add(self, entity: IBase):
        self.table_name = entity.__class__.__name__.lower()
        print(f"Writing to table: {self.table_name}")
        entity.id = 1
        self.data.append(
            {"fields": asdict(entity)})

    def commit(self):
        print(self.__get_api_url(self.table_name))
        print({"records": self.data})
        res = requests.post(
            self.__get_api_url(self.table_name),
            data=json.dumps({"records": self.data}),
            headers=self.headers
        )
        print(res)

    def flush(self):
        print("Returning")