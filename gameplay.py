import random
from consts import *
from game_sprites import Enemy


class Room:
    def __init__(self, number_room, player):
        self.player = player
        self.number_room = number_room
        self.enemies_number = number_room // random.randint(5, 11) + random.randint(1, 2)
        # self.enemies_number = 1000
        self.enemies_speed = 5.


        self.enemies = self.generate_enemies()


    def generate_enemies(self):
        enemies_ = []
        for _ in range(self.enemies_number):
            enemies_.append(Enemy(random.randint(R + 10, R + WIDTH - 10), random.randint(10, HEIGHT - 10), self.player,
                                  speed=self.enemies_speed + random.uniform(-self.enemies_speed/3, self.enemies_speed/3)))
        return enemies_

    def add(self, all_, enm):
        for en in self.enemies:
            all_.add(en)
            enm.add(en)
