import os

from peewee import *

db_name = "resource/db/saves/main_game_mode.db"
DB = SqliteDatabase(db_name)

if not os.path.exists("resource/db/saves/main_game_mode.db"):
    with open("resource/db/saves/main_game_mode.db", "w"):
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
