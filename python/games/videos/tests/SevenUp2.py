import pygame
import os 
from math import floor, ceil
from PIL import Image
from Menupyg import Menu, Params, click_handler_begin
from utils.elements import Element
from utils.bases import Weapons, colision
from typing import List

pygame.init()
pygame.font.init()
clock = pygame.time.Clock()

BLACK = (0,0,0)

test = "/Users/snowden/Documents/COURS_L1S1/option_info/python/games/videos/tests/img/hiclipart.com.png"


def get_pixel_color(image):
    image = Image.open(image)
    compteur_wpx = 0 
    image_rgb = image.convert("RGB")
    coords_sep = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0), (0,0)]
    nb_cut = 0
    for i in range(image.size[0]):
        if image_rgb.getpixel((i, 25)) == (255, 255, 153):
            print(compteur_wpx)
            compteur_wpx += 1
            if compteur_wpx > 70:
                print("cut")
                coords_sep[nb_cut] = (i-70, 25)
                nb_cut += 1
                compteur_wpx = 0
        else:
            
            compteur_wpx = 0
    print(nb_cut)
    return (coords_sep)

def get_dimension(base_w=0, base_h=0, im=1):
    from PIL import Image
    image = Image.open(img_path)
    size = image.size

    return (base_w*(im),base_h,base_w*(im),base_h)


class SevenUpClass(object):
    """ Sprite Sub Class """
    def __init__(self, file_name):
 
        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name).convert()
 
 
    def get_image(self, x, y, width, height):
 
        # Create a new blank image
        image = pygame.Surface([width, height]).convert()
 
        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
 
        # Assuming black works as the transparent color
        image.set_colorkey(BLACK)
 
        # Return the image
        return image



# it is better to have an extra variable, than an extremely long line.
img_path = test

class Bird(object):  # represents the bird, not the game
    def __init__(self):
        """ The constructor of the class """
        self.image = pygame.image.load(img_path).convert()
        self.coords_sep = get_pixel_color(img_path)

        self.current_image = SevenUpClass(img_path).get_image(0, 0, 128, 142.8)
        # 128.0
        # 142.8
        # the bird's position
        self.x = 0   
        self.y = 140
        self.line_compteur = 0
        self.col_compteur = 0
        self.rot_right = 0

        for y in range(5):
            for im in range(6):
                im += 1
                dim = (((im)*130), y*125, 130, 120)
                self.__setattr__(f"image_{y}{im}", SevenUpClass(img_path).get_image(dim[0],
                                                                                dim[1],
                                                                                dim[2],
                                                                                dim[3]))                 
    @property
    def check_rot(self):
        return self.rot_right

    def rotation_px(self):    
        dist = 3
        pattern = "_0"
        self.rot_right = (1 if self.rot_right < 1 else self.rot_right)
        if self.rot_right >= 25:
            self.y += dist
            pattern = "_"

        else:
            if self.rot_right % 10 == 0:
                self.rot_right += 1
            if (self.rot_right % 10) >= 6:
                self.rot_right += 5
            if self.rot_right > 6:
                pattern = "_"
                # self.rot_right += 5
            if self.rot_right < 1:
                self.rot_right = 1
            
            if self.rot_right <= 6:
                pattern = "_0"
        
        print(self.rot_right)
        return pattern

    def rotation_nx(self):    
        dist = 3
        pattern = "_"
        self.rot_right -= 1
        self.rot_right = (1 if self.rot_right < 1 else self.rot_right)
        if self.rot_right == 1:
            pattern = "_0"
  
        else:
            if self.rot_right % 10 == 0:
                pattern = "_"
                
                self.rot_right += 1

            if (self.rot_right % 10) >= 6:
                self.rot_right -= 5 

            if self.rot_right < 11:
                pattern = "_"
                self.rot_right -= 5
                if self.rot_right < 1:
                    self.rot_right = 1
            
            if self.rot_right <= 6:
                pattern = "_0"

        return pattern

    def handle_shoot(self):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                w1.shoot()
                w1.tire_position = (self.x, self.y)
                w1.shooted = True

                                                                                                   
                                                            
    def handle_keys(self):
        """ Handles Keys """
        
        # CHECK THAT ALL IMAGES HAVE BEEN CREATED

        key = pygame.key.get_pressed()
        dist = 3 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            pattern = self.rotation_px()
           
            if self.rotation_nx == 1:
                self.y += dist
            
            pattern = "_0"
            self.rot_right = (1 if self.rot_right < 1 else self.rot_right)
            if self.rot_right > 25:
                print("OK")
                self.y = self.y + dist
                print(self.y)
                pattern = "_"
                if (self.rot_right % 10) >= 6:
                    self.rot_right += 5

                if self.rot_right % 10 == 0:
                    self.rot_right -= 5
            
                self.current_image = self.__getattribute__(f"image{pattern}{self.rot_right}")


            elif self.rot_right < 25:
                print("SALOPE")
                self.rot_right += 1

                if self.rot_right % 10 == 0:
                    self.rot_right += 1
                if (self.rot_right % 10) >= 6:
                    self.rot_right += 5
                if self.rot_right > 6:
                    pattern = "_"
                    # self.rot_right += 5
                if self.rot_right < 1:
                    self.rot_right = 1
                
                if self.rot_right <= 6:
                    pattern = "_0"
                
                self.current_image = self.__getattribute__(f"image{pattern}{self.rot_right}")

            
        elif key[pygame.K_UP]: # up key
            pattern = self.rotation_nx()
         
            
            if self.rot_right == 25:
                pattern = "_"

            else:
                if self.rot_right % 10 == 0:
                    self.rot_right += 1
                if (self.rot_right % 10) >= 6:
                    self.rot_right += 5
                if self.rot_right > 6:
                    pattern = "_"
                    # self.rot_right += 5
                if self.rot_right < 1:
                    self.rot_right = 1

                
                if self.rot_right <= 6:
                    pattern = "_0"
                    self.y -= dist

                
            
            self.current_image = self.__getattribute__(f"image{pattern}{self.rot_right}")

        elif key[pygame.K_RIGHT]: # right key
            self.x += dist
            self.rot_right += 1 # move right
            self.rot_right = (self.rot_right+5 if self.rot_right == 6 else self.rot_right)
            if self.rot_right > 15:
                self.x += dist
            else:
                if self.rot_right > 6:
                    pattern = "_"
                else:
                    pattern = "_0"
                
                self.current_image = self.__getattribute__(f"image{pattern}{self.rot_right}")

        elif key[pygame.K_LEFT]: # left key
            # self.x -= dist # move left
            pattern = "_"
            self.rot_right -= 1
            self.rot_right = (1 if self.rot_right < 1 else self.rot_right)
            if self.rot_right == 1:
                self.x -= dist
            else:
                if self.rot_right % 10 == 0:
                    self.rot_right -= 5

                if self.rot_right < 11:
                    pattern = "_"
                    self.rot_right -= 5
                if self.rot_right < 1:
                    self.rot_right = 1
            
                if self.rot_right <= 6:
                    pattern = "_0"
                    
                self.current_image = self.__getattribute__(f"image{pattern}{self.rot_right}")
       


    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.current_image, (self.x, self.y))


class Enemy(Element):
    def __init__(self, data:List[dict], ID):
        sub_pack = [el for el in data[ID].values()]
        self.core = Element(sub_pack[1], 
                               sub_pack[2],
                               sub_pack[3],
                               sub_pack[4],
                               sub_pack[5],
                               sub_pack[6],
                               sub_pack[7])



screen = pygame.display.set_mode((1200, 600))
menu_data = {"title":"stark", "key_to_start": "K_SPACE", "bg_color":(10,90,0), "font_color":(155,155,155), "button_start":((200, 200, 130, 40),5, (245, 0, 20)),"button_option":((200, 300, 130, 40),5, (245, 0, 20))}
enemy_data = [{"name1":"jack","image_path":"/Users/snowden/Documents/COURS_L1S1/option_info/python/games/img/png/001-ufo.png", "speed_down":10, "speed_up":10, "speed_right":10, "speed_left":10, "attack":10, "defense":10}]

bird = Bird() # create an instance
clock = pygame.time.Clock()
enemy1 = Enemy(enemy_data, 0)
w1 = Weapons("war", 10, 10, 10, 10, 10,10, "029-vortex.png", "029-vortex.png")
# w1.shoot()
running = True
menu1 = Menu(menu_data, screen)
params_list = Params()
compteur_shoot = 0
first = True
while running:
    while not params_list.button_started_pressed:
        menu1.display()
        menu1.draw_button("button_start")

        pygame.display.update()
        for event in pygame.event.get():
            if click_handler_begin([menu1.button_start],params=params_list, event=event):
                params_list.button_started_pressed = True

            if event.type == pygame.QUIT:
                pygame.quit() # quit the screen
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.__getattribute__((menu1.__getattribute__("key_to_start")).strip("\'\'")):

                    params_list.button_started_pressed = True
                    

    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False
        
    
    compteur_shoot += 1
    
    bird.handle_keys() # handle the keys
    bird.handle_shoot()
    screen.fill((255,255,255)) # fill the screen with white
    enemy1.core.moving()
    if enemy1.core.defense > 0:
        screen.blit(enemy1.core.small_image, (enemy1.core.x, enemy1.core.y))

    bird.draw(screen) # draw the bird to the screen

    if w1.shooted:
        screen.blit(w1.tire(), (w1.tire_position[0]+10*compteur_shoot, w1.tire_position[1]+compteur_shoot))

    if colision(bird, enemy1.core):
        enemy1.core.defense = 0
    
  

    pygame.display.update() # update the screen

    clock.tick(40)


