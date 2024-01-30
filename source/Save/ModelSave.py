import os

from peewee import *

db_name = "resource/db/saves/db.db"
DB = SqliteDatabase(db_name)

if not os.path.exists("resource/db/saves/db.db"):
    with open("resource/db/saves/db.db", "w"):
        pass


class BaseModel(Model):
    class Meta:
        database = DB


class Save(BaseModel):
    data = CharField()
    sets = CharField()
    items = CharField()


if not Save.table_exists():
    DB.create_tables([Save])
