import random

from source.Calculations.Calculations import *
from source.Calculations.Data import *
from source.Field.Field import Field
from source.Functions.Functions import set_direction
from source.Image.InitializationForGame import get_images_for_game
from source.Levels.Level import Level1
from source.Movable_objects.Obstacles import *
from source.Save.Save import load
from source.Sounds.Sound import *
from source.States.InterfaceData import Data
from source.States.InterfaceState import InterfaceState
from source.States.Pause import Pause

n = 0


class RedactorMode(InterfaceState, Data):
    def start(self):
        self.pause = False
        pg.mouse.set_visible(False)
        self.main_window.fps = MAX_FPS[0]

    def __init__(self, screen, main_window, level=Level1()) -> None:
        super().__init__(screen, main_window)
        self.type = "RedactorMode"
        self.level = level
        self.field: Field = ...
        self.start_level(level)
        self.screen: pg.Surface = screen
        self.obstacle_set: set = set()
        self.time_passed: np.float_ = np.float_(0)

        self.pos = []

        self.pause: bool = True

        self.last_screen = self.screen.copy()

        self.begin()

    def begin(self):
        self.pause = False
        self.make_borders()

    def start_level(self, level):
        self.field: Field = Field(field, level.background)

    def save(self):
        ...

    def load(self):
        if load(self):
            for x in set(range(4, MAX_OBSTACLES)) - obstacles_ids:
                self.obstacle_set.add(Obstacle(obstacles, x, "red", obstacles_ids))
        else:
            clear_data()

        self.make_borders()

    def make_borders(self):
        obstacles[0] = np.array([FIELD_WIDTH / 2, - 100, FIELD_WIDTH, 100])
        obstacles[1] = np.array([FIELD_WIDTH / 2, FIELD_HEIGHT + 100, FIELD_WIDTH, 100])
        obstacles[2] = np.array([- 100, FIELD_HEIGHT / 2, 100, FIELD_HEIGHT])
        obstacles[3] = np.array([FIELD_WIDTH + 100, FIELD_HEIGHT / 2, 100, FIELD_HEIGHT])
        self.obstacle_set.add(
            Obstacle(obstacles, 0, "red", obstacles_ids))
        self.obstacle_set.add(
            Obstacle(obstacles, 1, "red", obstacles_ids))
        self.obstacle_set.add(
            Obstacle(obstacles, 2, "red", obstacles_ids))
        self.obstacle_set.add(
            Obstacle(obstacles, 3, "red", obstacles_ids))
        obstacles_ids.discard(0)
        obstacles_ids.discard(1)
        obstacles_ids.discard(2)
        obstacles_ids.discard(3)

    def create_obstacles(self):
        self.obstacle_set |= set(
            [Obstacle(obstacles, obstacles_ids.pop(), "black", obstacles_ids,
                      data=np.array([0 + 100 * i, 0 + 200 * i, 200, 600]))
             for i in range(10)])

    def build(self):
        if len(self.pos) == 2:
            ID = np.int_(obstacles_ids.pop())
            obstacles[ID] = np.array([
                np.abs(self.pos[0][0] + self.pos[1][0]) // 2, np.abs(self.pos[0][1] + self.pos[1][1]) // 2,
                np.abs(self.pos[0][0] - self.pos[1][0]) // 2, np.abs(self.pos[0][1] - self.pos[1][1]) // 2
            ])
            self.obstacle_set.add(Obstacle(obstacles, ID, [random.randint(0, 255) for _ in range(3)], obstacles_ids))
            self.pos = []

    def delete(self):
        ID = calc_obstacle_delete(
            np.array(pg.mouse.get_pos()) + np.array((field[0] - field[8] / 2, field[1] - field[9] / 2)), obstacles)
        if ID > 3:
            obstacles[ID] = default_obstacle
            for x in set(self.obstacle_set):
                if x.Id == ID:
                    x.kill()

    def check_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.pos.append(
                    np.array(pg.mouse.get_pos()) + np.array((field[0] - field[8] / 2, field[1] - field[9] / 2)))
            if event.button == 3:
                if len(self.pos) == 1:
                    self.pos = []
                if len(self.pos) == 0:
                    self.delete()
        if event.type == pg.KEYDOWN:
            if event.key == CONTROLS["MENU"]:
                self.pause = True
                self.main_window.set_state(Pause(self.screen, self.main_window, self, self.last_screen))

    def calc_calculations(self):
        if not self.pause:
            calc_player_movement(player, set_direction(self.main_window.key_pressed), self.main_window.dt)

            calc_cameraman(player, field, self.main_window.dt)

    def draw_or_kill(self):
        for x in self.obstacle_set:
            x.draw(self.field.field)

    def draw(self):
        self.screen.fill(0)
        self.field.draw()
        self.draw_or_kill()
        field_screen_centre_x, field_screen_centre_y = self.field.data[0:2] - self.field.data[8:10] / 2
        self.update_blueprint()
        self.screen.blit(self.field.field, (0, 0), (field_screen_centre_x, field_screen_centre_y, WIDTH, HEIGHT))

    def draw_cursor(self):
        self.last_screen = self.screen.copy()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.screen.blit(get_images_for_game()['cursor'],
                         (mouse_x - 16, mouse_y - 16))

    def update_blueprint(self):
        self.build()
        if len(self.pos) == 1:
            m_pos = np.array(pg.mouse.get_pos()) + np.array((field[0] - field[8] / 2, field[1] - field[9] / 2))
            rect_data = (min(self.pos[0][0], m_pos[0]), min(self.pos[0][1], m_pos[1]), abs(m_pos[0] - self.pos[0][0]),
                         abs(m_pos[1] - self.pos[0][1]))
            pg.draw.rect(self.field.field, "#137ABB", rect_data)
            pg.draw.rect(self.field.field, "#282B4E", rect_data, 5)

    def update(self):
        global n

        self.calc_calculations()
        self.draw()
        self.draw_cursor()

        n += 1
