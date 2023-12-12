"""classes Waves and additional functions"""
import random

from Constants import *
from Enemies import Enemy


class Wave:
    def __init__(self, enemies, player, chunks) -> None:
        self.number_wave: int = 1
        self.killed: int = 0
        self.enemies = enemies
        self.player = player
        self.chunks = chunks
        self.need_to_kill: int = 50
        self.add_need_to_kill: int = 50
        self.delay_spawn_bot: float = 0
        self.delay_wave: float = 0

    def new_wave(self):
        self.number_wave += 1
        self.killed = 0
        self.need_to_kill = self.need_to_kill + self.add_need_to_kill

    def spawn(self, screen_center):
        direction = random.randint(0, 3)
        if direction == 0:
            t = screen_center[1] - HEIGHT // 2 - 30
            if t <= 0:
                return self.spawn(screen_center)
            t1 = screen_center[0] - WIDTH // 2 - 30
            t2 = screen_center[0] + WIDTH // 2 + 30
            coordinate = random.randint(int(max(10, t1)), int(min(FIELD_WIDTH - 10, t2)))

            self.enemies.add(Enemy(self.player, coordinate, t + 10, self.chunks))
            return

        if direction == 1:
            t = screen_center[0] + WIDTH // 2 + 30
            if t >= FIELD_WIDTH:
                return self.spawn(screen_center)
            t1 = screen_center[1] - HEIGHT // 2 - 30
            t2 = screen_center[1] + HEIGHT // 2 + 30
            coordinate = random.randint(int(max(10, t1)), int(min(FIELD_HEIGHT - 10, t2)))

            self.enemies.add(Enemy(self.player, t + 10, coordinate, self.chunks))
            return

        if direction == 2:
            t = screen_center[1] + HEIGHT // 2 + 30
            if t >= FIELD_HEIGHT:
                return self.spawn(screen_center)
            t1 = screen_center[0] - WIDTH // 2 - 30
            t2 = screen_center[0] + WIDTH // 2 + 30
            coordinate = random.randint(int(max(10, t1)), int(min(FIELD_WIDTH - 10, t2)))

            self.enemies.add(Enemy(self.player, coordinate, t + 10, self.chunks))
            return

        if direction == 3:
            t = screen_center[0] - WIDTH // 2 - 30
            if t <= 0:
                return self.spawn(screen_center)
            t1 = screen_center[1] - HEIGHT // 2 - 30
            t2 = screen_center[1] + HEIGHT // 2 + 30
            coordinate = random.randint(int(max(10, t1)), int(min(FIELD_HEIGHT - 10, t2)))

            self.enemies.add(Enemy(self.player, t + 10, coordinate, self.chunks))
            return

    def update(self, screen_center):
        if self.killed > self.need_to_kill:
            self.new_wave()
            return

        if len(self.enemies) < MAX_ENEMIES and len(self.enemies) < self.need_to_kill:
            if self.delay_spawn_bot == 0:
                self.delay_spawn_bot = 0.2
                self.spawn(screen_center)
        if CLOCK.get_fps() != 0:
            self.delay_spawn_bot = max(0, self.delay_spawn_bot - (1 / (CLOCK.get_fps())))
