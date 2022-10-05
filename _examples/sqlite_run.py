from dataclasses import dataclass
from typing import List

# import cattr
from sqlalchemy.orm import (
    relationship,
    sessionmaker,
    registry,
)
from sqlalchemy import Table, Column, ForeignKey, create_engine, MetaData
from sqlalchemy.sql.sqltypes import Integer, String

# commented this out for the example
# from src.vlep.domain.model import Patient

mapper_registry = registry()

@dataclass
class ClassRoom:
    room_name: str


@dataclass
class Child:

    name: str


@dataclass
class Parent:

    name: str
    children: List[Child]


metadata_obj = MetaData()

parent = Table(
    "parent",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255)),
)

child = Table(
    "child",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255)),
    Column("parent_id", ForeignKey("parent.id", ondelete="SET NULL")),
)

class_room = Table(
    "classRoom",
    metadata_obj,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("room_name", String(255))
)


def start_mappers():
    mapper_registry.map_imperatively(
        Parent,
        parent,
        properties={"children": relationship(Child, backref="parent")},
    )
    mapper_registry.map_imperatively(Child, child)
    mapper_registry.map_imperatively(ClassRoom, class_room)


if __name__ == "__main__":

    engine = create_engine("sqlite:///mydb.db")
    metadata_obj.create_all(engine)
    start_mappers()
    session = sessionmaker(bind=engine)()

    c1 = Child("Uguinho")
    c2 = Child("Luizinho")
    p = Parent("Fulano", [c1, c2])

    cr = ClassRoom("My room")
    session.add(cr)

    session.add(p)
    session.commit()

    # try:
    #     # This works
    #     d = cattr.unstructure(p, Child)
    #     p2 = cattr.structure(d, Child)
    #     d2 = cattr.unstructure(p2, Child)
    #     print(d2)
    # finally:
    #     # This now works
    #     d = cattr.unstructure(p, Parent)
    #     p2 = cattr.structure(d, Parent)
    #     d2 = cattr.unstructure(p2, Parent)
    #     print(d2)