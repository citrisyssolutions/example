from sqlalchemy.engine import create_engine
from sqlalchemy.orm import relationship, backref, sessionmaker, registry, declarative_base

from sqlalchemy import Text, Column, Integer, String, ForeignKey, Table, create_engine, MetaData
metadata = MetaData()
mapper_registry = registry()
from dataclasses import dataclass

@dataclass
class User:
    Name: str
    Price: str
    Description: str

users = Table(
    "users",
    metadata,
    Column("Name", String(255), primary_key=True),
    Column("Price", String(255)),
    Column("Description", String(255))
)

# Base = declarative_base()

# class MyTable(Base):
#     __tablename__ = 'users'
#     id = Column(Integer, primary_key=True)
#     Name = Column(String(500))
#     Price = Column(String(500))
#     Description = Column(String(500))

#     def __init__(self, Name, Price, Description):
#         id = Column(Integer, primary_key=True)
#         self.Name = Name
#         self.Price = Price
#         self.Description = Description


engine = create_engine(
    'airtable://:keyvFVTECSngawPxK@appeGrlit5GKyPLX0'
)

# print(engine.table_names())
session = sessionmaker(bind=engine)()
mapper_registry.map_imperatively(User, users)
# res = session.execute("select * from users")
# for re in res:
#     print(re)

new = User(
    "muthu",
    "pandian",
    "description"
)

product = session.query(User).all()
for p in product:
    print(p.Name)

session.add(new)
session.commit()
    