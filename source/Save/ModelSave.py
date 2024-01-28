from peewee import *

db_name = "../resource/db/saves/db.db"
DB = SqliteDatabase(db_name)


class BaseModel(Model):
    class Meta:
        database = DB


class Save(BaseModel):
    data = CharField()
    sets = CharField()


if not Save.table_exists():
    DB.create_tables([Save])
