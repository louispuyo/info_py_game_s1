import pygame
from utils.bases import Personnage
from utils.box import MysteryBox

pygame.init()


red = (255, 0, 0)
BLACK = (0,0,0)
screen = pygame.display.set_mode((1300, 600))
clock = pygame.time.Clock()


# Background
background = pygame.image.load('/Users/snowden/Documents/COURS_L1S1/option_info/python/games/makets/models_invaders/background.png')
fence = [
    pygame.draw.rect(screen, red, pygame.Rect(455, 65, 20, 85)),
    pygame.draw.rect(screen, red, pygame.Rect(390, 65, 85, 20)),
    pygame.draw.rect(screen, red, pygame.Rect(390, 0, 20, 85)),
    pygame.draw.rect(screen, red, pygame.Rect(395, 0, 240, 20)),
    pygame.draw.rect(screen, red, pygame.Rect(615, 0, 20, 150)),
    pygame.draw.rect(screen, red, pygame.Rect(580, 130, 40, 20)),
    pygame.draw.rect(screen, red, pygame.Rect(455, 130, 80, 20))
]



# fence = [
#     pygame.draw.rect(screen, red, pygame.Rect(500, 65, 20, 85)),
#     pygame.draw.rect(screen, red, pygame.Rect(530, 65, 85, 20)),
#     pygame.draw.rect(screen, red, pygame.Rect(530, 0, 20, 85)),
#     pygame.draw.rect(screen, red, pygame.Rect(395, 0, 240, 20)),
#     pygame.draw.rect(screen, red, pygame.Rect(615, 0, 20, 150)),
#     pygame.draw.rect(screen, red, pygame.Rect(580, 130, 40, 20)),
#     pygame.draw.rect(screen, red, pygame.Rect(500, 130, 80, 20))
# ]

player = Personnage('freeze')
player_x = 300
player_y = 300

playerImg = pygame.image.load('/Users/snowden/Documents/COURS_L1S1/option_info/python/games/makets/models_invaders/ufo.png')
# bg01 = pygame.image.load("/Users/snowden/Documents/COURS_L1S1/option_info/games/img/bg/3ac9aa82578ac6346fed433e7b9766b5.jpg")

# def player():
#     screen.blit(playerImg, (player_x, player_y))
#     pygame.display.update()

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def display_player(element:object):
    # screen.blit(bg, (0,0))
    screen.fill(BLACK)
    screen.blit(element.small_image, (element.x, element.y))
    pygame.display.update()



running = True

while running:
    screen.fill(BLACK)
    player.move()
    # 
    display_player(player)
   
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        
        # if event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_LEFT:
        #         player.x -= player.speed_left
        #         display_player(player)

        #     if event.key == pygame.K_RIGHT:
        #         player.x += player.speed_right
        #         display_player(player)

        #     if event.key == pygame.K_UP:
        #         player.y -= player.speed_up
        #         display_player(player)

        #     if event.key == pygame.K_DOWN:
        #         player.y += player.speed_down
        #         display_player(player)
        
    
        clock.tick(60)



        
