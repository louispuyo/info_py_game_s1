import pygame
from utils.bases import Element

pygame.init()

screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('/Users/snowden/Documents/COURS_L1S1/option_info/python/games/makets/models_invaders/background.png')


player_x = 300
player_y = 300

playerImg = pygame.image.load('/Users/snowden/Documents/COURS_L1S1/option_info/python/games/makets/models_invaders/ufo.png')


def player():
    screen.blit(playerImg, (player_x, player_y))
    pygame.display.update()


    


running = True

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        player() 
