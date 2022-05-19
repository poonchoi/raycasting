import pygame
import numpy as np

##COLORS##
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
##########

##PYGAME INIT##
pygame.init()

dimensions = 700, 700
width = dimensions[0]
height = dimensions[1]

screen_2d = pygame.display.set_mode(dimensions)
screen_2_5d = pygame.display.set_mode(dimensions)

clock = pygame.time.Clock()
fps = 60


###############


def draw2d():
    map = [
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "0",
        "0",
        "0",
        "0",
        "1",
        "1",
        "0",
        "0",
        "0",
        "0",
        "1",
        "1",
        "0",
        "0",
        "0",
        "0",
        "1",
        "1",
        "0",
        "0",
        "0",
        "0",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
        "1",
    ]
    screen_2d.fill(black)
    lines = 40


def main():

    run = True

    while run:
        clock.tick(fps)
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False

        pygame.display.update()
