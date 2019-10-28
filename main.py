import pygame
import random

# initialize game
pygame.init()

# create screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('images/background.jpg')  # 800px x 600px

# Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('images/logo.png')  # 32px
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('images/space.png')  # 64px
playerX = 370
playerY = 480

# Changing player position
playerX_change = 0

# Enemy
enemyImg = pygame.image.load('images/enemy.png')  # 64px
enemyX = random.randint(0, 800)
enemyY = random.randint(0, 50)

# Changing enemy position
enemyX_change = 2
enemyY_change = 40


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# GameLoop
running = True
while running:

    # RGB background
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed move right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0

    playerX += playerX_change

    # the ship does not pass the bounding box
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change

    # the ship does not pass the bounding box
    if enemyX <= 0:
        enemyX_change = 2
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -2
        enemyY += enemyY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
