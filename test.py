import math

dx = 40
dy = 1

print(math.atan2(dx, dy))
tmp_dx = math.sin(math.atan2(dx, dy)) * dx
tmp_dy = math.cos(math.atan2(dx, dy)) * dy

print(tmp_dx, tmp_dy, (tmp_dx ** 2 + tmp_dy ** 2) ** 0.5)