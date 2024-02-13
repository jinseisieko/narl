import os

from peewee import *

db_name = "resource/db/settings.db"
DB = SqliteDatabase(db_name)

if not os.path.exists(db_name):
    with open(db_name, "w"):
        pass


class BaseModel(Model):
    class Meta:
        database = DB


class Settings(BaseModel):
    player = CharField()
    master_volume = DoubleField()
    music_volume = DoubleField()
    sfx_volume = DoubleField()
    max_fps = DoubleField()
    controls = CharField()


if not Settings.table_exists():
    DB.create_tables([Settings])

