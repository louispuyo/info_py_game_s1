import pygame
from math import sqrt

pygame.init()

########## PERSO ###############

class Alien:
    def __init__(self, name:str, speed_up, speed_down, speed_right, speed_left, attack, defense,
    image:str, weapon_image:str):
        self.name = name
        self.speed_up = speed_up
        self.speed_down = speed_down
        self.speed_right = speed_right
        self.speed_left = speed_left
        self.attack = attack
        self.defense = defense
        self.image = "python/games/img/png/"+image
        self.weapon_image = "python/games/img/"+weapon_image
        



Alien_list = {"galas0":Alien("galas0", 10, 8, 11, 9, 30, 120, "017-ufo.png", "029-vortex.png"),
              "gorgon":Alien("gorgon", 12, 12, 8, 7, 56, 200, "026-alien.png", "029-vortex.png"),
              "freeze":Alien("freeze",10, 10, 10, 10, 50, 1000, "028-alien.png", "008-ufo.png")}
    

############### END ################

############ WEAPONS ###############


class Weapons:
    def __init__(self, name, attack, defense, bullet_speed, missile_speed, 
    bullet_degat, missile_degat, bullet_image:str, missile_image:str):
        self.name = name
        self.dimension = (500,500)
        self.tire_position = (0,0)
        self.py = pygame
        self.x = -100
        self.y = 100
        self.bx = -100
        self.by = 100
        self.bullet_speed = bullet_speed
        self.missile_speed = missile_speed
        self.bulletImg = pygame.image.load(f'python/games/img/png/{bullet_image}')
        self.missileImg = pygame.image.load(f'python/games/img/png/{missile_image}')
        self.bullet = pygame.transform.scale(self.bulletImg, (10,10))
        self.missile = pygame.transform.scale(self.missileImg, (20,20))
        self.shooted = False
        self.shot = False


    def shoot(self):

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    self.shot = True
                    return self.tire()
    
                    
    def tire(self):
         img = pygame.transform.scale(self.bulletImg, (30,30))
         return img
         

    def tire_missile(self, bx, by):

         img = pygame.transform.scale(self.missileImg, (40,40))
         return img

    def mega_missile(self, bx, by):
        pass



Weapons_list = {"standard":Weapons("standard", 30, 40, 20, 10, 30, 60, "029-vortex.png", "007-capsule.png"), 
"war":Weapons("war", 60, 40, 20, 20, 30, 90, "029-vortex.png", "missile.png"),
"mars":Weapons("mars", 10, 100, 29, 20, 20, 300, "008-ufo.png", "torpille.png")}


############# END ##################



class Screen(object):
    def __init__(self, dimension=(500,500), title="window", background=None):
        BLACK = (0,0,0)
        self.dimension = dimension
        self.background = (None if background is None else pygame.image.load(background))
        self.screen = pygame.display.set_mode(dimension)
        self.title = self.caption
        self.surface = self.screen.fill(BLACK)
        self.py = pygame

    
    def set_bg(self):
        if self.background is None:
            pass
        else:
            self.screen.blit(self.background, [0,0])

    
    def caption(self, text="the Game"):
        """ add a caption : "legende" is french """
        self.py.display.set_caption(text)


    def loop(self):
        return """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        

            pygame.display.update()
            """

class Personnage:

    def __init__(self, name, x_custom=100, y_custom=100, x=10, y=10):
        self.name = name
        self.core = Alien_list[name]
        self.py = pygame
        self.speed_up = self.core.speed_up
        self.speed_down = self.core.speed_down
        self.speed_right = self.core.speed_right
        self.speed_left = self.core.speed_left
        self.defense = self.core.defense
        self.attack = self.core.attack
        self.x = x
        self.y = y
        self.image = pygame.image.load(self.core.image)
        self.small_image = pygame.transform.scale(self.image, (50, 50))
        self.custom_image = pygame.transform.scale(self.image, (x_custom, y_custom))
        self.available_actions = {}

    
    def use_action(self, action_key):
        self.available_actions[action_key]()

    def move(self):

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and self.y > 0: self.y -= self.speed_up
        if pressed[pygame.K_DOWN] and self.y < 400: self.y += self.speed_down
        if pressed[pygame.K_LEFT] and self.x > 0: self.x -= self.speed_left
        if pressed[pygame.K_RIGHT] and self.x < 450: self.x += self.speed_right
    

        
def euclidian_distance(x1, y1, x2, y2):
    """ return the distance betwenn 2 points in plan(x,y) """
    distance = sqrt(pow((x1-x2), 2)+(pow((y1-y2), 2)))
    return distance


def colision(obj1, obj2, bullet_mode=False):
    if bullet_mode:
        x1 = obj1.bx
        y1 = obj1.by
    else:
        x1 = obj1.x
        y1 = obj1.y 

    x2 = obj2.x
    y2 = obj2.y

    if euclidian_distance(x1, y1, x2, y2) < 37:
        return True
    else:
        return False






class HeathBare:
    def __init__(self, owner):
        self.vie = owner.defense
        self.base = pygame.Rect(250, 5, 0, 30)
    
    def disp_jauge(self):
        return self.base