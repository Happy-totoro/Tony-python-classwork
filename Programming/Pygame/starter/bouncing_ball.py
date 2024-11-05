import pygame
import random
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BALL_SIZE = 25
size = (700, 500)
gameOver = False
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bouncing Ball")
clock = pygame.time.Clock()
GRAVITY = 0.5
class Ball:
    def __init__(self) -> None:
        self.y = 15
        self.change_y = 10
ball = Ball()
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (350, int(ball.y)), 15,0)
    if ball.y <= size[1]:
        ball.change_y += GRAVITY
        ball.y += ball.change_y
    elif ball.y >= size[1]:
        ball.change_y *= -1
        ball.y += ball.change_y
    pygame.display.flip()
    clock.tick(60)
    