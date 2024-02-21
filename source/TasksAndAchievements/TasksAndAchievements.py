from source.Inventory.Items.ItemModel import DB, ItemsBlocked
from source.TasksAndAchievements.TasksAndAchievementsModel import init_tasks, save, \
    init_achievements, init


class TasksAndAchievements:
    def __init__(self, main_window) -> None:
        super().__init__()
        self.main_window = main_window
        self.tasks: dict[str] = {}
        self.achievements: dict[str] = {}

    def init(self):
        init(self.main_window.meta_player.name)
        init_achievements(self.achievements, self.main_window.meta_player.name)
        init_tasks(self.tasks, self.main_window.meta_player.name)

        print(self.main_window.meta_player.name)
        print(self.tasks)
        print(self.achievements)

    def kill_100_enemies(self, count):  # при убийстве врага/врагов
        # with DB.atomic():
        #     s = ItemsBlocked.update({ItemsBlocked.blocked: False}).where(
        #         ItemsBlocked.player == self.main_window.meta_player.name and ItemsBlocked.id == "1")
        #     s.execute()


        self.tasks['kill_100_enemies']['data']['count'] += count

        if self.tasks['kill_100_enemies']['data']['count'] >= 100:
            self.tasks['kill_100_enemies']["fulfillment"] = True
            with DB.atomic():
                s = ItemsBlocked.update({ItemsBlocked.blocked: False}).where(
                    ItemsBlocked.player == self.main_window.meta_player.name and ItemsBlocked.id == "shotgun")
                s.execute()
    def kill_1000_enemies(self, count):
        self.achievements['kill_1000_enemies']['data']['count'] += count

        if self.achievements['kill_1000_enemies']['data']['count'] >= 1000:
            self.achievements['kill_1000_enemies']["fulfillment"] = True
            ...

    def save(self):
        save(self.tasks, self.achievements, self.main_window.meta_player.name)
