import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Set up display
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Define game variables
BLOCK_SIZE = 20
SPEED = 10

# Initial snake settings
snake_List = []
lengthOfSnake = 1

# Initialize the snake at the center of the screen
snake_List.append([width // 2, height // 2])

# Initial direction
direction = "RIGHT"
change_to = direction

# Random initial food position
foodx = round(random.randrange(0, width - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
foody = round(random.randrange(0, height - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE

# Game clock
clock = pygame.time.Clock()

# Game over flag
game_over = False

def draw_snake(snake_List):
    """Draw the snake on the screen."""
    for x in snake_List:
        pygame.draw.rect(screen, GREEN, [x[0], x[1], BLOCK_SIZE, BLOCK_SIZE])

while not game_over:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Control snake direction with arrow keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                change_to = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                change_to = "RIGHT"
            elif event.key == pygame.K_UP and direction != "DOWN":
                change_to = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                change_to = "DOWN"

    # Update direction
    direction = change_to

    # Snake movement
    snake_Head_x = snake_List[0][0]
    snake_Head_y = snake_List[0][1]

    if direction == "LEFT":
        snake_Head_x -= BLOCK_SIZE
    elif direction == "RIGHT":
        snake_Head_x += BLOCK_SIZE
    elif direction == "UP":
        snake_Head_y -= BLOCK_SIZE
    elif direction == "DOWN":
        snake_Head_y += BLOCK_SIZE

    # Insert new head at the beginning of the snake list
    snake_Head = [snake_Head_x, snake_Head_y]
    snake_List.insert(0, snake_Head)

    # Check if snake has eaten the food
    if snake_Head[0] == foodx and snake_Head[1] == foody:
        foodx = round(random.randrange(0, width - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        foody = round(random.randrange(0, height - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        lengthOfSnake += 1
    else:
        # Remove the last segment if no food is eaten
        snake_List.pop()

    # Check for collisions with boundaries
    if snake_Head_x < 0 or snake_Head_x >= width or snake_Head_y < 0 or snake_Head_y >= height:
        game_over = True

    # Check for collision with itself
    for segment in snake_List[1:]:
        if segment == snake_Head:
            game_over = True

    # Draw everything
    screen.fill(BLACK)  # Background color
    draw_snake(snake_List)  # Draw the snake
    pygame.draw.rect(screen, RED, [foodx, foody, BLOCK_SIZE, BLOCK_SIZE])  # Draw the food

    # Update the display
    pygame.display.update()

    # Set the speed of the game
    clock.tick(SPEED)

# End game
pygame.quit()
sys.exit()
