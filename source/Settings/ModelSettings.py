import os

from peewee import *

db_name = "resource/players/guest/tasksAndAchievements.db"
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
    controls = ...

