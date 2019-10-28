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

def player():
    screen.blit(playerImg, (playerX,playerY))



#GameLoop
running = True
while running:

    #RGB background
    screen.fill((64, 224, 208))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #RGB background
    screen.fill((64, 224, 208))
    player()
    pygame.display.update()






