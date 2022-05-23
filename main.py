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

dimensions = 1200, 720
width = dimensions[0]
height = dimensions[1]

px = width // 2
py = height // 2
psize = (10,10)

screen_2d = pygame.display.set_mode(dimensions)
screen_2_5d = pygame.display.set_mode(dimensions)

clock = pygame.time.Clock()
fps = 60
###############

map = [
    ["1","1","1","1","1","1"],
    ["1","0","0","0","0","1"],
    ["1","0","0","0","0","1"],
    ["1","0","0","0","0","1"],
    ["1","0","0","0","0","1"],
    ["1","1","1","1","1","1"]
]

def draw_map():
    square_res = 60

    screen_2d.fill(white)
    # pygame.draw.line(surface, color, start_pos, end_pos, width)
    # draw vertical lines
    for i in range(1, square_res + 1):
        offset = square_res * i
        start_pos = (0 + offset, 0)
        end_pos = (0 + offset, height)
        pygame.draw.line(screen_2d, black, start_pos, end_pos)

    # draw horizontal lines
    for i in range(1, square_res + 1):
        offset = square_res * i
        start_pos = (0, 0 + offset)
        end_pos = (width, 0 + offset)
        pygame.draw.line(screen_2d, black, start_pos, end_pos)



def main():
    run = True

    while run:
        clock.tick(fps)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False

        draw_map()


        pygame.display.update()


if __name__ == "__main__":
    main()
