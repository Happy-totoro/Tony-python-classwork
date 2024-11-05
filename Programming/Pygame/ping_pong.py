import pygame

pygame.init()

size = (700, 400)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ball")

RED = (255, 0, 0)
BLACK = (0, 0, 0)

BALL_SIZE = 25
ball_x = size[0] // 2
ball_y = size[1] // 2
ball_x_speed = 5
ball_y_speed = 5

paddleY1 = 175
paddleY2 = 175
paddle_width = 10
paddle_height = 50
paddle_velocity = 10

gameOver = False
clock = pygame.time.Clock()

while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddleY1 > 0:
        paddleY1 -= paddle_velocity
    if keys[pygame.K_s] and paddleY1 < size[1] - paddle_height:
        paddleY1 += paddle_velocity
    if keys[pygame.K_UP] and paddleY2 > 0:
        paddleY2 -= paddle_velocity
    if keys[pygame.K_DOWN] and paddleY2 < size[1] - paddle_height:
        paddleY2 += paddle_velocity

    ball_x += ball_x_speed
    ball_y += ball_y_speed

    if ball_y <= 0 or ball_y >= size[1] - BALL_SIZE:
        ball_y_speed = -ball_y_speed
    if ball_x <= paddle_width and paddleY1 <= ball_y <= paddleY1 + paddle_height:
        ball_x_speed = -ball_x_speed
    if ball_x >= size[0] - paddle_width - BALL_SIZE and paddleY2 <= ball_y <= paddleY2 + paddle_height:
        ball_x_speed = -ball_x_speed

    if ball_x < 0 or ball_x > size[0]:
        ball_x = size[0] // 2
        ball_y = size[1] // 2
        ball_x_speed = 5
        ball_y_speed = 5

    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (0, paddleY1, paddle_width, paddle_height))
    pygame.draw.rect(screen, RED, (size[0] - paddle_width, paddleY2, paddle_width, paddle_height))
    pygame.draw.ellipse(screen, RED, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
