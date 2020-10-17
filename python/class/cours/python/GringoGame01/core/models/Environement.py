import pygame
pygame.init()

DIMENSION = (1200,700)
screen = pygame.display.set_mode((DIMENSION))

class Environment:
    def __init__(self, bg_image_path:str):
        self.image = pygame.image.load(bg_image_path) # image a coller sur la surface
        self.surface = pygame.Surface((DIMENSION)) # surface
    
    def blit(self):
        self.surface.blit(self.image, (0,0))
    
    def blit_element(self, element):
        self.surface.blit(element.image, (element.x, element.y))


        