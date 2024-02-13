import json
import os

from peewee import *

from source.TasksAndAchievements.Achievements import achievements
from source.TasksAndAchievements.Tasks import tasks

db_name = "resource/db/tasksAndAchievements.db"
DB = SqliteDatabase(db_name)

if not os.path.exists(db_name):
    with open(db_name, "w"):
        pass


class BaseModel(Model):
    class Meta:
        database = DB


class Tasks(BaseModel):
    player = CharField()
    id = CharField()
    name = CharField()
    description = CharField()
    data = CharField()
    fulfillment = BooleanField()


class Achievements(BaseModel):
    player = CharField()
    id = CharField()
    name = CharField()
    description = CharField()
    data = CharField()
    fulfillment = BooleanField()


if not Tasks.table_exists():
    DB.create_tables([Tasks])

if not Achievements.table_exists():
    DB.create_tables([Achievements])


def save(tasks, achievements, name):
    with DB.atomic():
        for task in tasks.values():
            s = Tasks.update(
                {Tasks.data: json.dumps(task["data"])}).where((
                                                                      Tasks.player == name) & (
                                                                      Tasks.id == task["id"]))
            s.execute()

        for achievement in achievements.values():
            s = Achievements.update(
                {Achievements.data: json.dumps(achievement["data"])}).where((
                                                                                    Achievements.player == name) & (
                                                                                    Achievements.id ==
                                                                                    achievement[
                                                                                        "id"]))
            s.execute()


def init_achievements(achievements, name):
    with DB.atomic():
        for achievement_select in Achievements.select().where(Achievements.player == name):
            achievements[achievement_select.id] = {
                'id': achievement_select.id,
                'name': achievement_select.name,
                'description': achievement_select.description,
                'data': json.loads(achievement_select.data),
                'fulfillment': achievement_select.fulfillment
            }


def init(name):
    with DB.atomic():
        select_ = Tasks.select().where(Tasks.player == name)
        if len(select_) < len(tasks):
            for select in select_:
                select.delete_instance()

            for task in tasks:
                Tasks.create(player=name, id=task["id"], name=task["name"], description=task["description"],
                             data=task["data"],
                             fulfillment=task["fulfillment"])

        select_ = Achievements.select().where(Achievements.player == name)
        if len(select_) < len(achievements):
            for select in select_:
                select.delete_instance()

            for achievement in achievements:
                Achievements.create(player=name, id=achievement["id"], name=achievement["name"],
                                    description=achievement["description"], data=achievement["data"],
                                    fulfillment=achievement["fulfillment"])


def init_tasks(tasks, name):
    with DB.atomic():
        for task_select in Tasks.select().where(Tasks.player == name):
            tasks[task_select.id] = {
                'id': task_select.id,
                'name': task_select.name,
                'description': task_select.description,
                'data': json.loads(task_select.data),
                'fulfillment': task_select.fulfillment
            }
