import pygame
pygame.init()


class Personage(object):
    def __init__(self, image_path:str, name="gringo"):
        self.x = 140
        self.y = 40 
        self.raw_image = pygame.image.load(image_path) # image avant la redimension
        self.image = pygame.transform.scale(self.raw_image, (90,90)) # on redimensionne l image
        self.dx = 10 # deplacement en x
        self.dy = 5 # deplacement en y

    def move(self, direction:str, sens:int): 
        """
        # vecteur | direction : 'x' ou 'y' | sens -1(gauche) 
        # ou 1 (droite)         
        """
        new_position = self.__getattribute__(direction)*self.sens_decision(1)
        self.__setattr__(direction, new_position)

    def sens_decision(self, sens:int):
        if sens > 0:
            return 1
        elif sens == 0:  
            return 0
        else: # au pire si aucune des condition est vrai 
            return -1



        
gringo = Personage("/Users/snowden/Documents/COURS_L1S1/option_info/python/class/cours/python/GringoGame01/core/images/spritesheet_caveman.png")
gringo.move('x', 'negatif') 
