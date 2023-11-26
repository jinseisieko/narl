import random
from consts import *
from game_sprites import LittleBlueSquareEnemy


class Room:
    def __init__(self, number_room):
        self.number_room = number_room
        self.enemies_number = number_room // random.randint(5, 11) + random.randint(1, 2)
        # self.enemies_number = 1000
        self.enemies = self.generate_enemies()

    def generate_enemies(self):
        enemies_ = []
        for _ in range(self.enemies_number):
            enemies_.append(LittleBlueSquareEnemy(WIDTH // 2, HEIGHT // 2))
        return enemies_

    def add(self, all_, enm):
        for en in self.enemies:
            all_.add(en)
            enm.add(en)
