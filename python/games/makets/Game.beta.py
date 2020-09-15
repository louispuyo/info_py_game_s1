# import here
import pygame
import time 
import random
import sys
from math import sqrt
# init 
pygame.init()

# create the screen / size of the screen / time
screen = pygame.display.set_mode((800, 600))
fps = pygame.time.Clock() 
font = pygame.font.SysFont(None, 30)


# Params Global
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
CIRCLE_RADIUS = 30
ball_pos1 = [50, 50]

# Booleans that stop/start the loop 
running = True
pressed_down = False
pressed_left = False
pressed_right = False
pressed_up = False
click = False

# Statistics for each personnage
stats_dx = {"alien":10, "028-alien":30, "png/001-ufo":7, "png/003-plant":12}
stats_dy = {"alien":15, "028-alien":10, "png/001-ufo":7, "png/003-plant":12}
# Title and icons


## DATA SCORE SAVE/READ
def score():
  score = p1.started_at - ((time.localtime().__getattribute__("tm_min")*60*200)+time.localtime().__getattribute__("tm_sec")*200)
  return abs(score)

def save_score():
    with open("python/games/data/score.txt", "a+") as score:
        score.write(f"{score()},")
        score.close()

def open_score():
     with open("python/games/data/score.txt", "a+") as score:
        score_content = score.read()
        return score_content

###

class balle:
  def __init__(self):
    # self.width = 200
    # self.length = 200
    # self.x = ball_pos1[0]
    # self.y = ball_pos1[1]
    # self.edge_thickness = 100
    # self.rect = pygame.draw.rect(screen, BLACK, [self.x, self.y, 
    # self.width, self.length], self.edge_thickness)

    self.inc_x = 10
    self.inc_y = 10


def active_balle(pos, cx, cy):

  pos[0] += cx 
  pos[1] += cy
  return (cx, cy)



def update():
  inc_x = Bal.inc_x
  inc_y = Bal.inc_y

  pos = ball_pos1
  if pos[0]>765:
    Bal.__setattr__('inc_x',-inc_x)
    # inc_y = (inc_y if (pos[1] < 540 & pos[1] > 2) else -inc_y)
  
  elif pos[0] < 35:
    Bal.__setattr__('inc_x',-inc_x)
    # inc_y = (inc_y if pos[1] < 540 else -inc_y)
  
  if pos[1] > 565:
    Bal.__setattr__('inc_y',-inc_y)
  
  elif pos[1] < 35:
    Bal.__setattr__('inc_y',-inc_y)
  
  pygame.display.set_caption("score:"+str(p1.score))
  active_balle(pos, Bal.__getattribute__("inc_x"), Bal.__getattribute__("inc_y"))
  


class Player:
    def __init__(self, personnage:str):
        self.started_at = ((time.localtime().__getattribute__("tm_min")*60*200)+time.localtime().__getattribute__("tm_sec")*200)
        self.image = pygame.image.load(f"python/games/img/{personnage}.png")
        self.small_image = pygame.transform.scale(self.image, (50, 60))
        self.x = 380    
        self.y = 430
        self.rect = self.small_image.get_rect(topleft=(self.x, self.y))
        self.dx = stats_dx[personnage]
        self.dy = stats_dy[personnage]
        self.score = 0



class Ennemy:
    def __init__(self, personnage:str):
        self.image = pygame.image.load(f"python/games/img/png/{personnage}.png")
        self.small_image = pygame.transform.scale(self.image, (50, 60))
        self.x = 220    
        self.y = 130
        self.dx = stats_dx[personnage]
        self.dy = stats_dy[personnage]


# Element Creations
# Add a menu to choose your personnage
p1 = Player("alien")
e1 = Ennemy("028-alien")
Bal = balle()


def options():
    running = True
    empty_score = []
    screen.fill((0,0,0))
    # print(open_score())
    for s in open_score():
            
        empty_score.append(s)
        
                
        
    while running:
 
        draw_text('options', font, (255, 255, 255), screen, 20, 20)
        for index, i in enumerate(empty_score):
            draw_text(f"{i}", font, (255, 255, 255), screen, 50, 20+index*20)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        
        pygame.display.update()
        fps.tick(60)
 

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
 

def main_menu(score=0):
    click = False

    while True:
        screen.fill((0,0,0))
        draw_text('Menu', font, (GREEN), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        # Differents Game modes
        button_1 = pygame.Rect(50, 100, 200, 50)
        button_2 = pygame.Rect(50, 200, 200, 50)
        button_3 = pygame.Rect(50, 300, 200, 50)

        # Label of Buttons
        draw_text('Classic mode', font, (GREEN), screen, 80,80)
        draw_text('Complete mode', font, (RED), screen, 80,180)
        draw_text('Options', font, (WHITE), screen, 80,280)

    
        if button_1.collidepoint((mx, my)):
            if click: # Play the Game
                break

        if button_3.collidepoint((mx, my)):
            if click:
                
                options()
            
        if button_2.collidepoint((mx, my)):
            if click:
                print("complete_mode")
                choose_perso()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)


        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        fps.tick(60)


def move_player():
    if pressed_left:
        if p1.x > 0:
            p1.x -= p1.dx
    if pressed_right:
        if p1.x < 750:
            p1.x += p1.dx
    if pressed_up:
        if p1.y > 0:
            p1.y -= p1.dy
    if pressed_down:
        if p1.y < 550:
            p1.y += p1.dy


# BUTTONS FACTORY #


#### END BUTTON


## RESULT ##

def new_partie():
    p1 = Player("alien")
    return p1

p1 = new_partie()

def ResultView(score_user=0):
    click = False

    while True:
        screen.fill((0,0,0))
        draw_text(f'Result {score_user}', font, (GREEN), screen, 20, 20)

        mx, my = pygame.mouse.get_pos()

        # Differents Game modes
        button_1 = pygame.Rect(50, 100, 200, 50)

        # Label of Buttons
        draw_text('Menu', font, (WHITE), screen, 80,80)
        ball_pos1 = [40,40]
   
            
        if button_1.collidepoint((mx, my)):
            if click:
                main_menu(score=0)
        
        pygame.draw.rect(screen, (255, 0, 0), button_1)

      


        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        fps.tick(60)
        


##



def choose_perso():
    # Load here all Aliens character
    
    classic_ufo = Player("png/001-ufo") # NOT optimize at all
    plant = Player("png/003-plant")
    
   
    choosing = True
    # List all theme here / Lock or unLocked Perso + Money
    # save party... (bonus)
    while choosing:
        mx, my = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            screen.fill(BLACK)
            screen.blit(classic_ufo.small_image, (100, 100))
            screen.blit(plant.small_image, (200, 100))


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    choosing = False

            if event.type == pygame.QUIT:
                # running = False
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
            

            pygame.display.update()



def enemy(ex, ey):
    # enemy_move()
    screen.blit(e1.small_image, (ex, ey))

def play(px, py):
    # Display our player
    screen.blit(p1.small_image, (px, py))
    move_player()


def Iscolision():

    ballX = ball_pos1[0]
    ballY = ball_pos1[1]
    playX = p1.x
    playY = p1.y
    distance = sqrt(pow((ballX-playX),2)+ pow((ballY-playY),2))
    if distance < 70:
        print("::COLISION::")
        pygame.display.set_caption(f"FAIL : SCORE : {score()}")
        ResultView(score_user=p1.score)
        
    

def render():
    # enemy(e1.x, e1.y)
    screen.fill(BLACK)
    ball_form = pygame.draw.circle(screen, RED, ball_pos1, CIRCLE_RADIUS, 0)
    update()
    
    play(p1.x, p1.y)
    Iscolision()
    # colision()

    pygame.display.update()

    fps.tick(30)


# MENU
menu = False
if menu:
    main_menu()


# GAME
p1 = Player("alien")
p1.score = score()

while running:
       
        render()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:          # check for key presses          
                if event.key == pygame.K_LEFT:        # left arrow turns left
                    pressed_left = True
                if event.key == pygame.K_RIGHT:     # right arrow turns right
                    pressed_right = True
                if event.key == pygame.K_UP:        # up arrow goes up
                    pressed_up = True
                if event.key == pygame.K_DOWN:     # down arrow goes down
                    pressed_down = True

            if event.type == pygame.KEYUP:            # check for key releases
                if event.key == pygame.K_LEFT:        # left arrow turns left
                    pressed_left = False
                if event.key == pygame.K_RIGHT:     # right arrow turns right
                    pressed_right = False
                if event.key == pygame.K_UP:        # up arrow goes up
                    pressed_up = False
                if event.key == pygame.K_DOWN:     # down arrow goes down
                    pressed_down = False
        
            

