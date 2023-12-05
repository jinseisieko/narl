from Field import Field
from Player import Player

player = Player(Field(), 0, {0, 0})

from Constants import *
import math

c1 = abs(DEFAULT_PLAYER_SPEED - player.max_speed) / DEFAULT_PLAYER_SPEED
c2 = abs(DEFAULT_PROJECTILE_RANGE - player.projectile_range) / DEFAULT_PROJECTILE_RANGE
c3 = abs(DEFAULT_PROJECTILE_SPEED - player.projectile_speed) / DEFAULT_PROJECTILE_SPEED
c4 = abs(DEFAULT_PROJECTILE_SIZE - player.projectile_size) / DEFAULT_PROJECTILE_SIZE
c5 = abs(DEFAULT_PROJECTILE_DAMAGE - player.projectile_damage) / DEFAULT_PROJECTILE_DAMAGE
c = [c1, c2, c3, c4, c5].index(min([c1, c2, c3, c4, c5]))
if c == 0:
    player.max_speed *= 2
elif c == 1:
    player.projectile_range *= 2
elif c == 2:
    player.projectile_speed *= 2
elif c == 3:
    player.projectile_size *= 2
elif c == 4:
    player.projectile_damage *= 2

print(player.max_speed, player.period, player.projectile_range, player.projectile_speed, player.projectile_size,
      player.projectile_damage)
