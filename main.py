import pygame
import numpy as np
import math


##COLORS##
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
gray = (80, 80, 80)
##########


##VARS##
dimensions = 1200, 600
width = dimensions[0]
height = dimensions[1]

px = width // 4
py = height // 2
psize = 10
pvel = 2
pangle = 0
pvel_rotate = 0.1

scl = 60
rows, cols = (height // scl), (width // scl)
########


##PYGAME INIT##
pygame.init()

screen_2d = pygame.display.set_mode(dimensions)
#screen_2_5d = pygame.display.set_mode(dimensions)

clock = pygame.time.Clock()
fps = 60
###############


def draw_map():
    map = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,1,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,1,0,1,1,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,1],
    [1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,0,0,1,0,0,1],
    [1,1,1,1,1,1,1,1,1,1],
    ]

    screen_2d.fill(gray)
    screen_2d.fill(green, pygame.Rect(width / 2, height / 2, width / 2, height / 2))
    screen_2d.fill(blue, pygame.Rect(width / 2, 0, width / 2, height / 2))
    for y in range(0, len(map)):
        for x in range(0, len(map[0])):

            startx = x * scl
            starty = y * scl
            w, h = scl - 1, scl - 1

            if map[y][x] == 1:
                screen_2d.fill(black, pygame.Rect(startx, starty, w, h))
            else:
                screen_2d.fill(white, pygame.Rect(startx, starty, w, h))


def player_move(px, py):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        py -= pvel
    if keys[pygame.K_a]:
        px -= pvel
    if keys[pygame.K_s]:
        py += pvel
    if keys[pygame.K_d]:
        px += pvel

    return px, py


def player_rotate(pangle):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        pangle += pvel_rotate
    if keys[pygame.K_LEFT]:
        pangle -= pvel_rotate

    if pangle > 360 or pangle < -360:
        pangle = 0

    return pangle


def player_draw(px, py, pangle):
    pygame.draw.rect(screen_2d, red, (px, py, psize, psize))

    line_start = (px + (psize / 2), py + (psize / 2))
    line_end = calc_pos(pangle, px, py)
    pygame.draw.line(screen_2d, green, line_start, line_end, 1)


def calc_pos(pangle, px, py):
    x = 1 * math.cos(pangle) * (180.0 / math.pi)
    y = 1 * math.sin(pangle) * (180.0 / math.pi)

    return (px + x + (psize / 2), py + y + (psize / 2))


def main(px, py, pangle):
    run = True

    while run:
        clock.tick(fps)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False

        draw_map()
        px, py = player_move(px, py)
        pangle = player_rotate(pangle)
        player_draw(px, py, pangle)

        pygame.display.update()


if __name__ == "__main__":
    main(px, py, pangle)
