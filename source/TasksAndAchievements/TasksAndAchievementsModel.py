import os

from peewee import *

from source.TasksAndAchievements.Achievements import achievements
from source.TasksAndAchievements.Tasks import tasks

db_name = "resource/db/tasksAndAchievements/tasksAndAchievements.db"
DB = SqliteDatabase(db_name)

if not os.path.exists("resource/db/tasksAndAchievements/tasksAndAchievements.db"):
    with open("resource/db/tasksAndAchievements/tasksAndAchievements.db", "w"):
        pass


class BaseModel(Model):
    class Meta:
        database = DB


class Tasks(BaseModel):
    id = CharField(unique=True)
    name = CharField()
    description = CharField()
    data = CharField()
    fulfillment = BooleanField()


class Achievements(BaseModel):
    id = CharField(unique=True)
    name = CharField()
    description = CharField()
    data = CharField()
    fulfillment = BooleanField()


if not Tasks.table_exists():
    DB.create_tables([Tasks])

if not Achievements.table_exists():
    DB.create_tables([Achievements])


def init():
    with DB.atomic():
        select_ = Tasks.select()
        if len(select_) < len(tasks):
            for select in select_:
                select.delete_instance()

            for task in tasks:
                Tasks.create(id=task["id"], name=task["name"], description=task["description"], data=task["data"],
                             fulfillment=task["fulfillment"])

        select_ = Achievements.select()
        if len(select_) < len(achievements):
            for select in select_:
                select.delete_instance()

            for achievement in achievements:
                Achievements.create(id=achievement["id"], name=achievement["name"],
                                    description=achievement["description"], data=achievement["data"],
                                    fulfillment=achievement["fulfillment"])
