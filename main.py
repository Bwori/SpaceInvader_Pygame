import pygame

# initialize game
pygame.init()

#create screen
screen = pygame.display.set_mode((800, 600))

#Title and Icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('logo.png') #32px
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space.png') #64px
playerX = 370
playerY = 480

# Changing position
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))



#GameLoop
running = True
while running:

    #RGB background
    screen.fill((64, 224, 208))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # If keystroke is pressed move right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.1
            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0




    playerX += playerX_change

    # the ship does not pass the bounding box
    if playerX <=0:
        playerX = 0
    elif playerX >=736:
        playerX = 736


    player(playerX,playerY)
    pygame.display.update()






