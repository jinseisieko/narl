"""pygame main loop"""

import sys
import pygame
from Constants import *
from Player import Player


class Field:
    def __init__(self) -> None:
        self.field: pygame.surface = pygame.Surface((FIELD_WIDTH, FIELD_HEIGHT))
        self.field.fill(GRAY)
        # сделать его красивым

    def draw(self, *groups: pygame.sprite.Group) -> None:
        self.field.fill(GRAY)
        for group in groups:
            group.draw(self.field)


# groups
all_sprites: pygame.sprite.Group = pygame.sprite.Group()
players_projectile: pygame.sprite.Group = pygame.sprite.Group()
enemies: pygame.sprite.Group = pygame.sprite.Group()
enemies_projectile: pygame.sprite.Group = pygame.sprite.Group()
player_group: pygame.sprite.Group = pygame.sprite.Group()

# player
player: Player = Player()
player_group.add(player)
all_sprites.add(player_group)
# field
field: Field = Field()
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.NOFRAME)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update
    all_sprites.update()

    # draw
    field.draw(enemies_projectile, players_projectile, player_group, enemies)
    screen.fill((0, 0, 0))
    screen.blit(field.field, (0, 0),
                (player.rect.centerx - WIDTH // 2, player.rect.centery - HEIGHT // 2, WIDTH, HEIGHT))

    pygame.display.flip()
    pygame.time.Clock().tick(TICKS)

pygame.quit()
sys.exit()
