import os

from peewee import *

db_name = "resource/db/main_game_mode.db"
DB = SqliteDatabase(db_name)

if not os.path.exists(db_name):
    with open(db_name, "w"):
        pass


class BaseModel(Model):
    class Meta:
        database = DB


class Save(BaseModel):
    player = CharField()
    data = CharField()
    sets = CharField()
    items = CharField()


if not Save.table_exists():
    DB.create_tables([Save])
