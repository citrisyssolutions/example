from sqlalchemy import Text, Column, Integer, String, ForeignKey, Table, create_engine, MetaData
metadata = MetaData()

room = Table(
    "room",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("room_name", String(255)),
    Column("room_type", String(255))
)
