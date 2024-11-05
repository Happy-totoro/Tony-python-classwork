import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Flake:
    def __init__(self, x_pos, y_pos, velocity, size) -> None:
        self.x = x_pos
        self.y = y_pos
        self.vel = velocity
        self.size = size

pygame.init()


size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Snow")

rows = 50
arr = [None for _ in range(rows)]  


for row in range(rows):  
    my_flake = Flake(random.randint(0, size[0] - 1), random.randint(0, size[1] - 1), random.randint(1, 3), random.randint(2, 7))
    arr[row] = my_flake

done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    for flake in arr:
        flake.y += flake.vel
        if flake.y > size[1]:
            flake.y = 0
            flake.x = random.randint(0, size[0] - 1)

    screen.fill(BLACK)

    for flake in arr:
        pygame.draw.circle(screen, WHITE, (flake.x, flake.y), flake.size)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
