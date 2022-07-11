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
dimensions = 600, 600
width = dimensions[0]
height = dimensions[1]

px = width // 2
py = height // 2
rot = np.pi / 4
pvel = 2
########


##PYGAME INIT##
pygame.init()

screen = pygame.display.set_mode(dimensions)

clock = pygame.time.Clock()
fps = 60
###############


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
    [1,1,1,1,1,1,1,1,1,1]]


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


def main(px, py):
    run = True

    while run:
        clock.tick(fps)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False

        px, py = player_move(px, py)

        for i in range(60):
            rot_i = rot + np.deg2rad(i - 30)
            x, y = (px, py)
            sin, cos =(0.02 * np.sin(rot_i), 0.02 * np.cos(rot_i))
            n = 0
            while True:
                x, y = (x + cos, y + sin)
                n = n + 1
                print(int(x), int(y))
                print(x,y)
                if map[int(x)][int(y)] != 0:
                    h = 1 / (0.02 * n)
                    break
                pygame.draw.line(screen, green, (i-30, height//2), (i-30, (height-h)//2), 5)
                pygame.draw.line(screen, green, (i-30, height//2), (i-30, height-(height-h)//2), 5)
       
        pygame.display.update()


if __name__ == "__main__":
    main(px, py)
