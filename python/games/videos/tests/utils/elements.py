import pygame

pygame.init()


class Element:
    def __init__(self, image_path, speed_down, speed_up, speed_right, speed_left, attack, defense, x_custom=100, y_custom=100, x=10, y=10):
        self.py = pygame
        self.attack = attack
        self.defense = defense
        self.speed_up = speed_up
        self.speed_down = speed_down
        self.speed_right = speed_right
        self.speed_left = speed_left
        self.x = x
        self.y = y
        self.direction_x = (self.speed_right+self.speed_left)//2
        self.direction_y = (self.speed_up+self.speed_down)//2
        self.image = pygame.image.load(image_path)
        self.small_image = pygame.transform.scale(self.image, (50, 60))
        self.custom_image = pygame.transform.scale(self.image, (x_custom, y_custom))

    def moving(self):
        if self.x >= 400:
            self.direction_x = -self.direction_x
        
        if self.x <= 0:
            self.direction_x = -self.direction_x
        
        if self.y >= 400:
            self.direction_y = -self.direction_y
        
        if self.y <= 0:
            self.direction_y = -self.direction_y
        
        self.x += self.direction_x
        self.y += self.direction_y


enemies = {"vilan":Element('python/games/img/png/002-alien.png', 7, 5, 5, 5, 10, 50),
          "kratos":Element('python/games/img/png/025-alien.png', 10, 15, 10, 10, 150,500, x=1, y=1)}

        
