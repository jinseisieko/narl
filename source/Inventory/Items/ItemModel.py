import os

from peewee import *

db_name = "resource/db/original.db"
DB = SqliteDatabase(db_name)

if not os.path.exists(db_name):
    with open(db_name, "w"):
        pass


class BaseModel(Model):
    class Meta:
        database = DB


class ItemsRank1(BaseModel):
    id = CharField(unique=True)
    name = CharField()
    description = CharField()
    renewal_plus = CharField()
    renewal_multiply = CharField()
    renewal_super = CharField()
    code = CharField()


class ItemsRank2(BaseModel):
    id = CharField(unique=True)
    name = CharField()
    description = CharField()
    renewal_plus = CharField()
    renewal_multiply = CharField()
    renewal_super = CharField()
    code = CharField()


class ItemsRank3(BaseModel):
    id = CharField(unique=True)
    name = CharField()
    description = CharField()
    renewal_plus = CharField()
    renewal_multiply = CharField()
    renewal_super = CharField()
    code = CharField()


class ItemsBlocked(BaseModel):
    id = CharField(unique=True)
    name = CharField()
    description = CharField()
    renewal_plus = CharField()
    renewal_multiply = CharField()
    renewal_super = CharField()
    code = CharField()
    blocking = BooleanField()


if not ItemsRank1.table_exists():
    DB.create_tables([ItemsRank1])

if not ItemsRank2.table_exists():
    DB.create_tables([ItemsRank2])

if not ItemsRank3.table_exists():
    DB.create_tables([ItemsRank3])

if not ItemsBlocked.table_exists():
    DB.create_tables([ItemsBlocked])
