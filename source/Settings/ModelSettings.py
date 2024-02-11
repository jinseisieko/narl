import os

from peewee import *

db_name = "resource/players/guest/settings.db"
DB = SqliteDatabase(db_name)

if not os.path.exists(db_name):
    with open(db_name, "w"):
        pass


class BaseModel(Model):
    class Meta:
        database = DB


class Settings(BaseModel):
    master_volume = DoubleField()
    music_volume = DoubleField()
    sfx_volume = DoubleField()
    max_fps = DoubleField()
    controls = CharField()


if not Settings.table_exists():
    DB.create_tables([Settings])


def set_settings_db(name):
    global DB, db_name
    db_name = name + "/settings.db"
    DB = SqliteDatabase(db_name)

    if not os.path.exists(db_name):
        with open(db_name, "w"):
            pass

    BaseModel._meta.database = DB
    Settings._meta.database = DB

    if not Settings.table_exists():
        DB.create_tables([Settings])
