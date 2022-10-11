key = 'airtable://:keyvFVTECSngawPxK@appeGrlit5GKyPLX0'
from airtable_orm import AirtableORM
from dataclasses import dataclass

orm = AirtableORM(key)
session = orm.get_session()

@dataclass
class Room:
    id: int
    room_name: str
    room_type: str

new_entity = Room(2, "My name", "Dev")
session.add(new_entity)
session.commit()

d = session.query(Room).all()
for _ in d:
    print(_.room_name)