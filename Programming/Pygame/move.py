import pygame
import sys
pygame.init()
clock = pygame.time.Clock()
width = 640
height = 480
screen = pygame.display.set_mode((width, height))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

block_width = 50
block_height = 50
blockx = 0
blocky = (height-block_height)//2
block_speed = 50

gameover = False

while not gameover == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
            pygame.quit()
            sys.quit()
