import math
import random

import pygame

pygame.init()
WIDTH, HEIGHT = 1000, 1000
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()
REPEAT = 100
SPEED = 1
COLLISIONS_REPELLING = 0.005


class MaterialPoint:
    def __init__(self):
        self.x = self.y = 100
        self.vx = self.vy = 0

    def update(self):
        self.x += self.vx
        self.y += self.vy

    @property
    def pos(self):
        return self.x, self.y


# def get_line_eq(ax, ay, bx, by):
#     a = by - ay
#     b = -(bx - ax)
#     c = ay * (bx - ax) - ax * (by - ay)
#     t = (a ** 2 + b ** 2) ** 0.5
#     a /= t
#     b /= t
#     c /= t
#     return a, b, c


class Ball(MaterialPoint):
    REPELLING = 0.05

    def __init__(self, radius, x, y, color):
        super().__init__()
        self.r = radius
        self.d = radius * 2
        self.x = x
        self.y = y
        self.color = color

    def bounce_box(self, left, top, right, bottom):
        # for _ in range(REPEAT):
        #     leftdt = left - (self.x - self.r)
        #     rightdt = right - (self.x + self.r)
        #     forcex = (max(leftdt, 0) + min(rightdt, 0))
        #     self.vx += self.REPELLING * forcex
        #     if abs(forcex) > 1.0e-6:
        #         self.x += self.vx
        #
        #     topdt = top - (self.y - self.r)
        #     bottomdt = bottom - (self.y + self.r)
        #     forcey = (max(topdt, 0) + min(bottomdt, 0))
        #     self.vy += self.REPELLING * forcey
        #     if abs(forcey) > 1.0e-6:
        #         self.y += self.vy
        #
        #     if abs(forcex) + abs(forcey) < 1.0e-5:
        #         break

        if self.x < left + self.r or self.x > right - self.r:
            self.x = max(left + self.r, (min(right - self.r, self.x)))
            self.vx = 0
        if self.y < top + self.r or self.y > bottom - self.r:
            self.y = max(top + self.r, (min(bottom - self.r, self.y)))
            self.vy = 0


def speed2normal(balls):
    k = 5
    for i in balls:
        i.vx = min(abs(i.vx), k) * math.copysign(1, i.vx)
        i.vy = min(abs(i.vy), k) * math.copysign(1, i.vy)


def collisions(balls):
    for i in balls:
        for j in balls:
            if i == j:
                continue
            i: Ball
            j: Ball
            size_1 = i.r
            size_2 = j.r
            real_dist = size_1 + size_2
            for _ in range(100):
                dist_x = i.x - j.x
                dist_y = i.y - j.y
                dist = math.hypot(dist_x, dist_y)

                if dist < real_dist:
                    if dist_x == 0:
                        j.x -= 1e-6
                        continue
                    if dist_y == 0:
                        j.y -= 1e-6
                        continue
                    i.vx += real_dist / dist_x * COLLISIONS_REPELLING
                    j.vx -= real_dist / dist_x * COLLISIONS_REPELLING
                    i.vy += real_dist / dist_y * COLLISIONS_REPELLING
                    j.vy -= real_dist / dist_y * COLLISIONS_REPELLING
                else:
                    break


COLLISIONS_REPELLING = 0.005

mouse_ball = Ball(50, 100, 100, (255, 255, 255))

objects = [Ball(40, 200, 200, ([random.randint(0, 255) for __ in range(3)])) for _ in range(40)] + [mouse_ball]

IS_GRABBING = False

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            quit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                IS_GRABBING = True
        if e.type == pygame.MOUSEBUTTONUP:
            if e.button == 1:
                IS_GRABBING = False
    SCREEN.fill("black")

    if IS_GRABBING:
        mouse_ball.x, mouse_ball.y = pygame.mouse.get_pos()
        mouse_ball.vx = mouse_ball.vy = 0

    collisions(objects)
    speed2normal(objects)

    for x in objects:
        # x.vy += 0.0
        x.update()
        x.bounce_box(0, 0, WIDTH, HEIGHT)
        pygame.draw.rect(SCREEN, x.color, (x.x - x.r, x.y - x.r, x.d, x.d), 10)
        # pygame.draw.circle(SCREEN, x.color, x.pos, x.r, 10)
        mx, my = pygame.mouse.get_pos()
        angle = math.atan2(my - x.y, mx - x.x)
        s = 0.5
        x.vx += s * math.cos(angle)
        x.vy += s * math.sin(angle)
    #
    # pygame.draw.circle(SCREEN, "white", mouse_ball.pos, mouse_ball.r, 10)
    #
    # pygame.draw.circle(SCREEN, "white", ball1.pos, ball1.r, 10)
    # pygame.draw.circle(SCREEN, "white", ball2.pos, ball2.r, 10)

    pygame.display.flip()
    CLOCK.tick(60)
