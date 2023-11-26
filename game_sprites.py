import math
import random

import pygame

from consts import *


class MoveBody:
    def __init__(self, speed):
        self.dx = 0
        self.dy = 0
        self.speed = speed
        self.trajectory = None
        self.smoothness = SMOOTHNESS

    def update_dx_dy(self, x1, x2, y1, y2):
        key_pressed_x = False
        key_pressed_y = False
        if y1:
            key_pressed_y = True
            self.dy -= self.speed / self.smoothness
            if self.dy < -self.speed:
                self.dy = -self.speed
        if y2:
            key_pressed_y = True
            self.dy += self.speed / self.smoothness
            if self.dy > self.speed:
                self.dy = self.speed
        if x1:
            key_pressed_x = True
            self.dx -= self.speed / self.smoothness
            if self.dx < -self.speed:
                self.dx = -self.speed
        if x2:
            key_pressed_x = True
            self.dx += self.speed / self.smoothness
            if self.dx > self.speed:
                self.dx = self.speed

        if not key_pressed_x:
            self.dx /= 1 + 1 / self.smoothness
            if abs(self.dx) <= self.speed / 4:
                self.dx = 0

        if not key_pressed_y:
            self.dy /= 1 + 1 / self.smoothness
            if abs(self.dy) <= self.speed / 4:
                self.dy = 0


class Player(pygame.sprite.Sprite, MoveBody):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"image\player50x50.png")
        self.rect = self.image.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        self.color_projectile = PROJECTILE_COLOR

        self.default_speed = PLAYER_SPEED
        self.speed = self.default_speed
        self.default_max_hp = PLAYER_MAX_HP
        self.max_hp = self.default_max_hp
        self.default_period = PROJECTILE_PERIOD
        self.period = self.default_period
        self.default_range_projectile = PROJECTILE_RANGE
        self.range_projectile = self.default_range_projectile
        self.default_speed_projectile = PROJECTILE_SPEED
        self.speed_projectile = self.default_speed_projectile
        self.default_damage = DAMAGE_PROJECTILE
        self.damage = self.default_damage
        self.default_size_projectile = PROJECTILE_SIZE
        self.size_projectile = self.default_size_projectile

        self.hp = PLAYER_MAX_HP
        self.atoms = 0
        self.dx = 0
        self.dy = 0
        self.smoothness = SMOOTHNESS
        self.ticks = math.ceil(self.range_projectile / self.speed_projectile) + 2

        self.improvements = []
        self.shot_improvements = []

        self.all_improvements = []

    def add_improvement(self, improvement):
        if improvement is None:
            return
        self.all_improvements.append(improvement)
        if improvement.parent == "ShotImprovement":
            self.shot_improvements.append(improvement)
        elif improvement.parent == "Improvement":
            self.improvements.append(improvement)
        self.update_characteristics()

    def update(self):
        keys = pygame.key.get_pressed()
        self.update_dx_dy(keys[pygame.K_a], keys[pygame.K_d], keys[pygame.K_w], keys[pygame.K_s])

        self.rect.x += self.dx
        self.rect.y += self.dy

        self.rect.x = max(R // 2, min(self.rect.x, WIDTH - PLAYER_SIZE + R // 2))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - PLAYER_SIZE))

    def update_characteristics(self):
        self.speed = self.default_speed
        self.period = self.default_period
        self.max_hp = self.default_max_hp
        self.atoms = 0
        self.damage = self.default_damage
        self.speed_projectile = self.default_speed_projectile
        self.range_projectile = self.default_range_projectile
        self.size_projectile = self.default_size_projectile
        self.color_projectile = PROJECTILE_COLOR

        for improvement in self.improvements:
            improvement.start(self)

        self.period = int(self.period)
        if self.period < 1:
            self.period = 1

        self.ticks = math.ceil(self.range_projectile / self.speed_projectile) + 2
        trajectory = [0] * self.ticks

        for shot_improvement in self.shot_improvements:

            if shot_improvement.name == "Boomerang":
                ticks_ageing = round(self.ticks * shot_improvement.get_ageing_factor())
                ticks_forward = self.ticks - ticks_ageing
                for i in range(ticks_forward - 1):
                    trajectory[i] += 0
                trajectory[ticks_forward - 1] += math.pi
                for j in range(ticks_ageing - 1):
                    trajectory[ticks_forward + j] += 0

            if shot_improvement.name == "Atom":
                self.atoms += 1

        self.trajectory = trajectory

    def shot(self):
        parent = Projectile(self.rect.centerx,
                            self.rect.centery,
                            *pygame.mouse.get_pos(),
                            speed=self.speed_projectile,
                            range_=self.range_projectile,
                            trajectory=self.trajectory,
                            damage=self.damage,
                            size=self.size_projectile,
                            color=self.color_projectile)

        projectiles = [parent]

        if self.atoms > 0:
            atom_damage = self.default_damage / 2
            angle_x_projectile = math.pi * 2 / self.atoms
            radios_projectile = self.size_projectile[0] + 4 * self.atoms

            for i in range(self.atoms):
                projectiles.append(
                    AtomProjectile(self.rect.centerx,
                                   self.rect.centery - radios_projectile,
                                   ticks=self.ticks,
                                   parent=parent,
                                   speed=self.speed // 5 + 2,
                                   angle=angle_x_projectile * (i + 1),
                                   radius=radios_projectile,
                                   damage=atom_damage,
                                   size=self.size_projectile,
                                   color=self.color_projectile))

        return projectiles


class Projectile(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, target_x, target_y, speed=PROJECTILE_SPEED, range_=PROJECTILE_RANGE,
                 size=(15, 15), color=PROJECTILE_COLOR, trajectory=None, damage=DAMAGE_PROJECTILE):
        super().__init__()
        self.color = color
        self.size = size
        self.image = pygame.Surface(size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = start_x - (size[0] // 2)
        self.rect.y = start_y - (size[1] // 2)

        self.range = range_
        self.distant = 0
        self.speed = speed
        self.trajectory = trajectory
        self.damage = damage

        self.angle = math.atan2(target_y - start_y, target_x - start_x)

        self.index_trajectory = None
        if self.trajectory:
            self.index_trajectory = 0

        self.dx = self.speed * math.cos(self.angle)
        self.dy = self.speed * math.sin(self.angle)

    def update(self):
        if self.trajectory:
            t = self.trajectory[self.index_trajectory]
            self.angle = ((self.angle + math.pi + t) % (2 * math.pi)) - math.pi
            self.index_trajectory += 1
            if self.index_trajectory >= len(self.trajectory):
                self.index_trajectory = 0

        self.dx = self.speed * math.cos(self.angle)
        self.dy = self.speed * math.sin(self.angle)

        if self.distant > self.range:
            self.kill()

        self.rect.x += self.dx
        self.rect.y += self.dy

        self.distant += self.speed

        if self.rect.x <= R // 2:
            self.kill()
        if self.rect.x >= WIDTH + R // 2:
            self.kill()


class AtomProjectile(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, size=(15, 15), color=PROJECTILE_COLOR, ticks=None, parent=None, speed=4,
                 radius=20, angle=0., damage=DAMAGE_PROJECTILE):
        super().__init__()
        self.size = size
        self.color = color
        self.parent = parent
        self.radius = radius
        self.image = pygame.Surface(size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = start_x
        self.rect.y = start_y
        self.distant = 0
        self.speed = speed
        self.trajectory = [angle] + [speed / radius] * ticks
        self.damage = damage

        self.angle = 0

        self.index_trajectory = None
        if self.trajectory:
            self.index_trajectory = 0

    def update(self):
        if self.trajectory:
            t = self.trajectory[self.index_trajectory]

            self.angle = ((self.angle + math.pi + t) % (2 * math.pi)) - math.pi

            self.index_trajectory += 1
            if self.index_trajectory >= len(self.trajectory):
                self.index_trajectory = 0

        if not self.parent.alive():
            self.kill()
        self.rect.x = self.parent.rect.x + self.radius * math.cos(self.angle)
        self.rect.y = self.parent.rect.y + self.radius * math.sin(self.angle)
        self.distant += PROJECTILE_SPEED

        if self.rect.x <= R // 2:
            self.kill()
        if self.rect.x >= WIDTH + R // 2:
            self.kill()


class LittleBlueSquareEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.size = LITTLE_BLUE_SQUARE_SIZE
        self.color = LITTLE_BLUE_SQUARE_COLOR
        self.image = pygame.Surface((LITTLE_BLUE_SQUARE_SIZE, LITTLE_BLUE_SQUARE_SIZE))
        self.image.fill(LITTLE_BLUE_SQUARE_COLOR)
        self.rect = self.image.get_rect(center=(x, y))

        self.hp = LITTLE_BLUE_SQUARE_HP
        self.speed = LITTLE_BLUE_SQUARE_SPEED
        self.damage = LITTLE_BLUE_SQUARE_DAMAGE

        self.angle = random.randint(-3140000, 3140000) / 100000
        self.index = 0

        self.dx = 0
        self.dy = 0
        self.trajectory = None
        self.smoothness = SMOOTHNESS

    def step_back(self, player):
        self.angle = math.atan2(self.rect.centery - player.rect.centery, self.rect.centerx - player.rect.centerx)

    def update(self):
        self.index = (self.index + 1) % 30
        if self.index > 28:
            self.angle += random.randint(-31400, 31400) / 30000
        else:
            self.angle += random.randint(-31400, 31400) / 1000000

        dx = self.speed * math.cos(self.angle)
        dy = self.speed * math.sin(self.angle)

        self.rect.x += dx
        self.rect.y += dy

        if self.rect.x >= (WIDTH - LITTLE_BLUE_SQUARE_SIZE + R // 2):
            self.angle = ((self.angle + 2 * math.pi) % math.pi) - (random.randint(8, 14) / 10) * math.pi

        if self.rect.x <= R // 2:
            self.angle = ((self.angle + 2 * math.pi) % math.pi) - (random.randint(8, 14) / 10) * math.pi

        if self.rect.y >= (HEIGHT - LITTLE_BLUE_SQUARE_SIZE):
            self.angle = ((self.angle + 2 * math.pi) % math.pi) - (random.randint(8, 14) / 10) * math.pi

        if self.rect.y <= 0:
            self.angle = ((self.angle + 2 * math.pi) % math.pi) - (random.randint(8, 14) / 10) * math.pi

        self.rect.x = max(R // 2, min(self.rect.x, WIDTH - LITTLE_BLUE_SQUARE_SIZE + R // 2))
        self.rect.y = max(0, min(self.rect.y, HEIGHT - LITTLE_BLUE_SQUARE_SIZE))
