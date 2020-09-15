import pygame
import random 
import time
from math import sqrt, sin, cos
from utils.blackwindow import Screen, Element, Image
from Math.distances import euclidian_distance

pygame.init()
S = 300
text_size = 60
bg_col = [0,0,0]
text_col = [255,255,255]
myfont = pygame.font.Font(None, text_size) # uses default pygame font; you can also specify a named font


# bulletImg = pygame.image.load('python/games/img/png/029-vortex.png')
# bulletX = 0
# bulletY = 480
# bulletX_change = 0
# bulletY_change = 10
# bullet_state = "ready"


class Alien(Element):
    def __init__(self, attack, defense, speed_up, speed_down, speed_right, speed_left):
        self.screen = Screen(background="python/games/img/bg/bg2.jpg").screen
        self.dimension = (500,500)
        self.tire_position = (0,0)
        self.py = pygame
        self.x = 10
        self.y = 10
        self.enemy_x = 100
        self.enemy_y = 50
        self.defense = defense
        self.enemy3_x = 30
        self.enemy3_y = 100
        self.enemy3_defense = 100
        self.enemy2_x = 56
        self.enemy2_y = 400
        self.image = Element(1, 2, [3,4,3,1], (0,0,0), 10).image
        self.speed_up = speed_up
        self.speed_down = speed_down
        self.speed_left = speed_left
        self.speed_right = speed_right
        self.bulletImg = pygame.image.load('python/games/img/png/029-vortex.png')
        self.missileImg = pygame.image.load('python/games/img/png/008-ufo.png')
        self.bullet = pygame.transform.scale(self.bulletImg, (10,10))
        self.missile = pygame.transform.scale(self.missileImg, (20,20))


    def tire(self, bx, by):
         
         img = pygame.transform.scale(self.bulletImg, (30,30))
         self.screen.blit(img, (bx, by))
         pygame.display.update()

    def tire_missile(self, bx, by):
         img = pygame.transform.scale(self.missileImg, (40,40))
         self.screen.blit(img, (bx, by))
         pygame.display.update()
        
    def mega_missile(self, bx, by):
        pass

 
        # fire_bullet(10,10)
        

    

A0 = Alien(10,200,9,6,5,10)
score_value = 0

def show_score(x, y):
    score = myfont.render("score: "+str(score_value), True,(255, 255, 255))
    A0.screen.blit(score, (x, y))
    pygame.display.update()


def enemy():
   screen = A0.screen
   img = pygame.image.load('python/games/img/png/020-ufo.png')
   if A0.enemy_x > 500:
       A0.enemy_x -= 14
   elif A0.enemy_x < 0:
       A0.enemy_x += 14
       
   if A0.enemy_y > 500:
       A0.enemy_y -= 14
   elif A0.enemy_y < 0:
       A0.enemy_y += 14

   img = pygame.transform.scale(img,(60, 60))
   A0.enemy_x += random.randint(-7, 7)
   A0.enemy_y += random.randint(-15, 15)
   screen.blit(img, (A0.enemy_x, A0.enemy_y))
   pygame.display.update()

def enemy3():
   screen = A0.screen
   img = pygame.image.load('python/games/img/png/021-ufo.png')
   if A0.enemy2_x > 500:
       A0.enemy2_x -= 14
   elif A0.enemy2_x < 0:
       A0.enemy2_x += 14
       
   if A0.enemy2_y > 500:
       A0.enemy2_y -= 14
   elif A0.enemy2_y < 0:
       A0.enemy2_y += 14
   

   img = pygame.transform.scale(img,(60, 60))
   A0.enemy2_x += random.randint(-10, 10)
   A0.enemy2_y += random.randint(-25, 15)
   screen.blit(img, (A0.enemy2_x, A0.enemy2_y))
   pygame.display.update()

def enemy2():
   screen = A0.screen
   img = pygame.image.load('python/games/img/png/012-ufo.png')
   if A0.enemy2_x > 500:
       A0.enemy2_x -= 14
   elif A0.enemy2_x < 0:
       A0.enemy2_x += 14
       
   if A0.enemy2_y > 500:
       A0.enemy2_y -= 14
   elif A0.enemy2_y < 0:
       A0.enemy2_y += 14
   

   img = pygame.transform.scale(img,(60, 60))
   A0.enemy2_x += random.randint(-10, 10)
   A0.enemy2_y += random.randint(-25, 15)
   screen.blit(img, (A0.enemy2_x, A0.enemy2_y))
   pygame.display.update()


A0.x = A0.image.x
A0.y = A0.image.y
missile_is_active = False
bullet_is_active = False
running = True
in_live = True
level2 = False
level3 = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_SPACE:
                bullet_is_active = True
                missile_is_active = False
                A0.x = A0.image.x
                A0.y = A0.image.y
                A0.tire_position = (A0.x, A0.y)
                # print("bullet is active fire")
            
            if event.key == pygame.K_n:
                print("next vague !")
                in_live = True
                level3 = True
                level2 = True
            
            if event.key == pygame.K_p:
                missile_is_active = True
                bullet_is_active = False
                A0.x = A0.image.x
                A0.y = A0.image.y
                A0.tire_position = (A0.x, A0.y)

            


    
    
    A0.move()
    show_score(10, 10)

    if euclidian_distance(A0.enemy_x, A0.enemy_y, A0.tire_position[0], A0.tire_position[1])<40:
        in_live = False
        bullet_is_active = False
        score_value += 10

    if euclidian_distance(A0.enemy2_x, A0.enemy2_y, A0.tire_position[0], A0.tire_position[1])<40:
        
        
        in_live = False
        bullet_is_active = False
        score_value += 20

    if euclidian_distance(A0.enemy3_x, A0.enemy3_y, A0.tire_position[0], A0.tire_position[1])<40:
        if A0.enemy3_defense <= 0:
            level3 = False
            bullet_is_active = False
            score_value += 50
        
        else:

            A0.enemy3_defense = A0.enemy3_defense-50
        
            bullet_is_active = False

    if not in_live:
        if random.randint(0,4) == 1:
            in_live  = False
            
            
            
    if level3 == True:
        enemy3()

    if level2 == True:
        enemy2()

    if in_live:
        enemy()

    if not in_live:
        if random.randint(0,4) == 1:
            in_live  = False
            # level2 = True

    if not level2:
        if A0.enemy3_defense > 0:
            level3 = True

    


    if bullet_is_active:
        bx = A0.tire_position[0]
        by = A0.tire_position[1]
        A0.tire_position = (bx, by-10)


        if by > A0.dimension[0]:
            bullet_is_active = False
            bx = 1000
            by = 1000
        if by < 0:
            bullet_is_active = False
            # print("crack")
            bx  = 1000
            by = 1000

        A0.tire(bx, by)


    if missile_is_active:
        bx = A0.tire_position[0]
        by = A0.tire_position[1]
        A0.tire_position = (bx, by-29)

        
        
    
        if by > A0.dimension[0]:
            bullet_is_active = False
            bx = 1000
            by = 1000
        if by < 0:
            bullet_is_active = False
            # print("crack")
            bx  = 1000
            by = 1000
       
        
        A0.tire_missile(bx, by)
            


