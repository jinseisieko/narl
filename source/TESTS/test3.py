import ctypes
import pygame
import pyglet

# setup pyglet & the video
path = r"chipichipichapachapa.avi"

player = pyglet.media.Player()
source = pyglet.media.load(path)
player.queue(source)
player.play()

# setup pygame
pygame.init()
pygame.display.set_mode((800, 800), 0)
pygame.display.set_caption("Video in Pygame!")
screen = pygame.display.get_surface()
pygame.display.flip()

# blit the video in a standard pygame event loop
while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            quit()
    screen.fill(0)

    player.dispatch_events()
    tex = player.get_texture()
    raw = tex.get_image_data().get_data('RGBA', tex.width * 4)
    raw = ctypes.string_at(ctypes.addressof(raw), ctypes.sizeof(raw))
    img = pygame.image.frombuffer(raw, (tex.width, tex.height), 'RGBA')
    screen.blit(img, (0, 0))

    pygame.display.flip()
