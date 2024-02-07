import os

from peewee import *

db_name = "resource/players/guest/main_game_mode.db"
DB = SqliteDatabase(db_name)

if not os.path.exists(db_name):
    with open(db_name, "w"):
        pass


def get_db():
    global DB
    return DB


class BaseModel(Model):
    class Meta:
        database = get_db()


class Save(BaseModel):
    data = CharField()
    sets = CharField()
    items = CharField()


if not Save.table_exists():
    DB.create_tables([Save])


def set_save_db(name):
    global DB, db_name
    db_name = name + "/main_game_mode.db"
    DB = SqliteDatabase(db_name)

    if not os.path.exists(db_name):
        with open(db_name, "w"):
            pass

    BaseModel._meta.database = DB
    Save._meta.database = DB

    if not Save.table_exists():
        DB.create_tables([Save])
