import pygame 
from random import randint

pygame.init()


class MysteryBox:
    def __init__(self):
        self.luck = randint(1, 1000)


    def tirage(self):
        if self.luck < 10:
            return "epics personage"
        
        elif self.luck == 777:
            return "hero perso"
        
        elif self.luck < 100:
            return "gold personnage"
        
        elif self.luck > 910:
            return "platinum perso"
        
        elif self.luck > 700:
            return "bronze perso"
        
        else:
            return "basics perso"




res = MysteryBox().tirage()
print(res)


