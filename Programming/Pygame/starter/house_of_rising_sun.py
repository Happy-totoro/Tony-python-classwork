import pygame

import pygame

pygame.init()

RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLUE = (135, 206, 250)

size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Sunrise and Sunset Animation")

gameOver = False
clock = pygame.time.Clock()

canvas_size = (32*640,32*480)
gravity = 1
initial_y_velocity = -100
initial_x_velocity = -110
circle_x_pos = 680*32
circle_y_pos = 150*32
y_velocity = initial_y_velocity

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    if circle_x_pos < -40*32:
        circle_x_pos = 680*32
        circle_y_pos = 180*32
        y_velocity = initial_y_velocity
    else:
        circle_x_pos = circle_x_pos + initial_x_velocity
        y_velocity += gravity
        circle_y_pos = circle_y_pos + y_velocity

    
    screen.fill(BLUE)
    pygame.draw.rect(screen, RED, [250, 285, 200, 100])
    pygame.draw.polygon(screen, BLACK, [[350, 210], [250, 285], [450, 285]])
    pygame.draw.rect(screen, GREEN, [0, 385, 700, 125])
    pygame.draw.circle(screen, YELLOW, (circle_x_pos//32,circle_y_pos//32),40,0)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
