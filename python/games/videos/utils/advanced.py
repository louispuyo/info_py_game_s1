import pygame

pygame.init()

class Weapons:
    def __init__(self, attack, defense, speed_up, speed_down, speed_right, speed_left):
        self.dimension = (500,500)
        self.tire_position = (0,0)
        self.py = pygame
        self.x = -100
        self.y = 100
        self.bx = -100
        self.by = 100
        self.speed_up = speed_up
        self.speed_down = speed_down
        self.speed_left = speed_left
        self.speed_right = speed_right
        self.bulletImg = pygame.image.load('python/games/img/png/029-vortex.png')
        self.missileImg = pygame.image.load('python/games/img/png/008-ufo.png')
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
         
        
    def mega_missile(self, bx, by):
        pass


