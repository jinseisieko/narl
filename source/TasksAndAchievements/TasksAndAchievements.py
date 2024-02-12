import json

from source.TasksAndAchievements.TasksAndAchievementsModel import DB, Tasks, Achievements


class TasksAndAchievements:
    def __init__(self) -> None:
        super().__init__()
        self.tasks: dict[str] = {}
        self.achievements: dict[str] = {}

        self.init_tasks()
        self.init_achievements()

        print(self.tasks)
        print(self.achievements)

    def init_tasks(self):
        with DB.atomic():
            for task_select in Tasks.select():
                self.tasks[task_select.id] = {
                    'id': task_select.id,
                    'name': task_select.name,
                    'description': task_select.description,
                    'data': json.loads(task_select.data),
                    'fulfillment': task_select.fulfillment
                }

    def init_achievements(self):
        with DB.atomic():
            for achievement_select in Achievements.select():
                self.achievements[achievement_select.id] = {
                    'id': achievement_select.id,
                    'name': achievement_select.name,
                    'description': achievement_select.description,
                    'data': json.loads(achievement_select.data),
                    'fulfillment': achievement_select.fulfillment
                }

    def kill_100_enemies(self, count):  # при убийстве врага/врагов
        self.tasks['kill_100_enemies']['data']['count'] += count

        if self.tasks['kill_100_enemies']['data']['count'] >= 100:
            self.tasks['kill_100_enemies']["fulfillment"] = True
            ...

    def kill_1000_enemies(self, count):
        self.achievements['kill_1000_enemies']['data']['count'] += count

        if self.achievements['kill_1000_enemies']['data']['count'] >= 1000:
            self.achievements['kill_1000_enemies']["fulfillment"] = True
            ...

    def save(self):
        select_tasks = Tasks.select()
        for task in select_tasks:
            task.data = json.dumps(self.tasks[task.id]["data"])
            task.fulfillment = self.tasks[task.id]["fulfillment"]
            task.save()

        select_achievements = Achievements.select()
        for achievement in select_achievements:
            achievement.data = json.dumps(self.achievements[achievement.id]["data"])
            achievement.fulfillment = self.achievements[achievement.id]["fulfillment"]
            achievement.save()
