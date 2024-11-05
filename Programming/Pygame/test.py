import pygame

# Initialize Pygame
pygame.init()

# Set up the screen
size = (700, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ping Pong")

# Colors
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Ball settings
BALL_SIZE = 25
ball_x = size[0] // 2
ball_y = size[1] // 2
ball_speed_x = 5
ball_speed_y = 5

# Paddle settings
paddle_width = 10
paddle_height = 100
paddle_speed = 10
paddle1_y = 150
paddle2_y = 150

# Game loop control
gameOver = False
clock = pygame.time.Clock()

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1_y > 0:
        paddle1_y -= paddle_speed
    if keys[pygame.K_s] and paddle1_y < size[1] - paddle_height:
        paddle1_y += paddle_speed
    if keys[pygame.K_UP] and paddle2_y > 0:
        paddle2_y -= paddle_speed
    if keys[pygame.K_DOWN] and paddle2_y < size[1] - paddle_height:
        paddle2_y += paddle_speed

    ball_x += ball_speed_x
    ball_y += ball_speed_y

    if ball_y <= 0 or ball_y >= size[1] - BALL_SIZE:
        ball_speed_y *= -1

    if (ball_x <= paddle_width and paddle1_y < ball_y < paddle1_y + paddle_height) or \
       (ball_x >= size[0] - paddle_width - BALL_SIZE and paddle2_y < ball_y < paddle2_y + paddle_height):
        ball_speed_x *= -1

    if ball_x < 0 or ball_x > size[0]:
        ball_x, ball_y = size[0] // 2, size[1] // 2
        ball_speed_x, ball_speed_y = 5, 5

    screen.fill(BLACK)
    
    pygame.draw.rect(screen, RED, (10, paddle1_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, RED, (size[0] - 20, paddle2_y, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
