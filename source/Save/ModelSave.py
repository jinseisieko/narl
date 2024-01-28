from peewee import *

db_name = "pw.sqlite.db"
DB = SqliteDatabase(db_name)


class BaseModel(Model):
    class Meta:
        database = DB


class Save(BaseModel):
    player_tb = CharField()
