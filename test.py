from Field import Field
from Player import Player

player = Player(Field(), 0, {0, 0})

import random
c = random.randint(0, 6)
if c == 0:
    player.max_speed += random.uniform(-player.max_speed / 2, player.max_speed / 2)
elif c == 1:
    player.projectile_range += random.uniform(-player.projectile_range / 2, player.projectile_range / 2)
elif c == 2:
    player.projectile_speed += random.uniform(-player.projectile_speed / 2, player.projectile_speed / 2)
elif c == 3:
    player.projectile_size += random.uniform(-player.projectile_size / 2, player.projectile_size / 2)
elif c == 4:
    player.projectile_damage += random.uniform(-player.projectile_damage / 2, player.projectile_damage / 2)
elif c == 5:
    player.period += random.uniform(-player.period / 2, player.period / 2)
elif c == 6:
    player.max_hp += random.uniform(-player.max_hp / 2, player.max_hp / 2)

print(player.max_speed, player.period, player.projectile_range, player.projectile_speed, player.projectile_size,
      player.projectile_damage, player.max_hp)
