"""pygame main loop (rendering, updates, organization)"""
import sys

import pygame
from Constants import *

class Field:
    def __init__(self):
        self.field: pygame.surface = pygame.Surface((FIELD_WIDTH, FIELD_HEIGHT))
        self.field.fill(GRAY)
        # сделать его красивым


# groups
all_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
enemies = pygame.sprite.Group()
particles = []

# игрок
player = Player()
all_sprites.add(player)

screen = pygame.display.set_mode((WIDTH_, HEIGHT))
pygame.display.set_caption("NARL")

running = True
shooting = False
console = False

# задержки
frame_count_projectile = 0
frame_count_target = 0
frame_end_console = 0
player.update_characteristics()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False




    pygame.display.flip()
    pygame.time.Clock().tick(TICKS)
    # print("FPS:", int(clock.get_fps()))


pygame.quit()
sys.exit()