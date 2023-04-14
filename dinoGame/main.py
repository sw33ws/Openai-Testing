import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the window dimensions
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 300
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Dino Game")

# Set up the game variables
GROUND_Y = WINDOW_HEIGHT - 70
dino_width = 60
dino_height = 71

cactus_width = 23
cactus_height = 46

cloud_width = 46
cloud_height = 14

dino_x = 50
dino_y = GROUND_Y - dino_height
dino_vel = 0
jump_vel = 20
GRAVITY = 1
score = 0

# Load the game images
dino_img = pygame.image.load('dinoGame\dino.png')
cactus_img = pygame.image.load('dinoGame\cactus.png')
cloud_img = pygame.image.load('dinoGame\cloud.png')
ground_img = pygame.image.load('dinoGame\ground.png')

# Scale the game images
dino_img = pygame.transform.scale(dino_img, (dino_width, dino_height))
cactus_img = pygame.transform.scale(cactus_img, (50, 100))
cloud_img = pygame.transform.scale(cloud_img, (50, 30))
ground_img = pygame.transform.scale(ground_img, (WINDOW_WIDTH, 70))

# Set up the game objects
cactus_list = []
cloud_list = []

# Define functions to create game objects
def create_cactus(cactus_vel):
    cactus_x = WINDOW_WIDTH + 20
    cactus_y = GROUND_Y - 100
    cactus_list.append((cactus_x, cactus_y, cactus_vel))

def create_cloud():
    cloud_x = WINDOW_WIDTH + 20
    cloud_y = random.randint(0, 100)
    cloud_list.append((cloud_x, cloud_y))

# Define a function to draw the game objects
def draw_objects():
    # Draw the dino
    window.blit(dino_img, (dino_x, dino_y))

    # Draw the cacti
    for cactus in cactus_list:
        window.blit(cactus_img, (cactus[0], cactus[1]))

    # Draw the clouds
    for cloud in cloud_list:
        window.blit(cloud_img, (cloud[0], cloud[1]))


# Define a function to check for collisions
def check_collision():
    for cactus in cactus_list:
        cactus_rect = pygame.Rect(cactus[0], cactus[1], 50, 100)
        dino_rect = pygame.Rect(dino_x, dino_y, dino_width, dino_height)
        if cactus_rect.colliderect(dino_rect):
            return True
    return False

# Define the game loop
game_over = False
clock = pygame.time.Clock()

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                dino_vel = -jump_vel

    # Move the dino
    dino_y += dino_vel
    dino_vel += GRAVITY

    # Check if the dino is on the ground
    if dino_y >= GROUND_Y - dino_height:
        dino_y = GROUND_Y - dino_height
        dino_vel = 0

    # Create game objects
    if len(cactus_list) < 2:
        create_cactus(10)
    if len(cloud_list) < 5:
        create_cloud()

    # Move game objects
    for cactus in cactus_list:
        cactus_x, cactus_y, cactus_vel = cactus
        cactus_x -= cactus_vel
        cactus_list[cactus_list.index(cactus)] = (cactus_x, cactus_y, cactus_vel)
        if cactus_x < -50:
            cactus_list.remove(cactus)
            create_cactus(10)

    for cloud in cloud_list:
        cloud_x, cloud_y = cloud
        cloud_x -= 2
        cloud_list[cloud_list.index(cloud)] = (cloud_x, cloud_y)

    # Check for collisions
    def check_collision():
        global cloud_list

        # Check for collisions with cacti
        for cactus in cactus_list:
            if dino_x + dino_width > cactus[0] and dino_x < cactus[0] + cactus_width and dino_y + dino_height > cactus[1]:
                return True

        # Check for collisions with clouds
        for cloud in cloud_list:
            if dino_x + dino_width > cloud[0] and dino_x < cloud[0] + cloud_width and dino_y + dino_height > cloud[1]:
                if cloud in cloud_list:
                    cloud_list.remove(cloud)
                return False

        return False


    # Draw objects
    window.fill((255, 255, 255))
    draw_objects()

    # Update score
    score += 1
    font = pygame.font.Font(None, 30)
    text = font.render("Score: " + str(score//10), True, (0, 0, 0))
    window.blit(text, (10, 10))

    # Update the display
    pygame.display.update()

    # Set the game speed
    clock.tick(60)

# Quit Pygame
pygame.quit()