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
# Enemies in a list

enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
enemy_speed = 1

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('images/enemy.png'))   # 64px
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(0, 50))
    # Changing enemy position
    enemyX_change.append(2)
    enemyY_change.append(40)

# Bullet
# Ready - you cant see the bullet
# Fire - the bullet will fire

bulletImg = pygame.image.load('images/bullet.png')  # 32px
bulletX = 0
bulletY = 480
bullet_state = "ready"

# Score
score = 0

# Changing bullet position
bulletX_change = 0
bulletY_change = 5


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False


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

    # Enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        # the ship does not pass the bounding box
        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            # explosion_Sound = mixer.Sound('explosion.wav')
            # explosion_Sound.play()
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(0, 50)

        enemy(enemyX[i], enemyY[i], i)

    # bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change



    player(playerX, playerY)
    pygame.display.update()
