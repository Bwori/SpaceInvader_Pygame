import pygame
import random
import math
from pygame import mixer

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

# Bullet
# Ready - you cant see the bullet
# Fire - the bullet will fire

bulletImg = pygame.image.load('images/bullet.png')  # 32px
bulletX = 0
bulletY = 480
bullet_state = "ready"

# Changing bullet position
bulletX_change = 0
bulletY_change = 5


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


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
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_Sound = mixer.Sound('sound/laser.wav')
                    # bullet_Sound.play()
                    # Get the current x coordinate of the spaceship
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

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

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
