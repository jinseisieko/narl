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
    player = CharField()
    id = CharField()
    name = CharField()
    description = CharField()
    renewal_plus = CharField()
    renewal_multiply = CharField()
    renewal_super = CharField()
    code = CharField()
    blocked = BooleanField()


if not ItemsRank1.table_exists():
    DB.create_tables([ItemsRank1])

if not ItemsRank2.table_exists():
    DB.create_tables([ItemsRank2])

if not ItemsRank3.table_exists():
    DB.create_tables([ItemsRank3])

if not ItemsBlocked.table_exists():
    DB.create_tables([ItemsBlocked])


def init(name):
    with DB.atomic():
        print(len(ItemsBlocked.select().where(ItemsBlocked.player == name)), len(
                ItemsBlocked.select().where(ItemsBlocked.player == "nan")))
        if len(ItemsBlocked.select().where(ItemsBlocked.player == name)) < len(
                ItemsBlocked.select().where(ItemsBlocked.player == "nan")):
            #
            # for s in ItemsBlocked.select().where(ItemsBlocked.player == name):
            #     s.delete_instance()
            for s in ItemsBlocked.select().where(ItemsBlocked.player == "nan"):
                ItemsBlocked.create(player=name, id=s.id,
                                    name=s.name,
                                    description=s.description,
                                    renewal_plus=s.renewal_plus,
                                    renewal_multiply=s.renewal_multiply,
                                    renewal_super=s.renewal_super,
                                    code=s.code,
                                    blocked=True)
