import pygame
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
pygame.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Moving Rectangle")
gameOver = False
clock = pygame.time.Clock()
x = 0
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, [x, 225, 100, 50])
    x += 5
    if x > 700:
        x = -100
    pygame.display.flip()
    clock.tick(60)
pygame.quit()