import os

from peewee import *





db_name = "resource/db/players.db"
DB = SqliteDatabase(db_name)

if not os.path.exists(db_name):
    with open(db_name, "w"):
        pass


class BaseModel(Model):
    class Meta:
        database = DB


class Player(BaseModel):
    name = CharField(unique=True)
    password = CharField()


if not Player.table_exists():
    DB.create_tables([Player])


class MetaPlayer:
    def __init__(self) -> None:
        super().__init__()
        self.name = "guest"

    def init_db(self):
        ...

    def set(self, name, password):
        with DB.atomic():
            select = Player.select().where(Player.name == name)
            if select:
                if select[0].password == password:
                    self.name = name
                    self.init_db()

    def register(self, name, password):
        with DB.atomic():
            select = Player.select().where(Player.name == name)
            if not select:
                Player.create(name=name, password=password)
                self.set(name, password)
