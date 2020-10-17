import pygame
import os 
from math import floor, ceil
from PIL import Image

pygame.init()

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

        # for y in range(1, 6):
        #     tmp = 0
        #     for index,coord in enumerate(self.coords_sep):
        #         dim = (tmp, 130, coord[0]+tmp, ((y)*130-(y-1)*130))
        #         tmp = coord[0]

        #         self.__setattr__(f"image_{y-1}{index}", SevenUpClass(img_path).get_image(dim[0],
        #                                                                         dim[1],
        #                                                                         dim[2],
        #                                                                         dim[3]))  


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
        # self.rot_right += 1
        self.rot_right = (1 if self.rot_right < 1 else self.rot_right)
        # self.current_image = self.__getattribute__(f"image_0{self.rot_right}")
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
        # self.rot_right += (self.rot_right+4 if self.rot_right == 27 else self.rot_right)
        return pattern

    def rotation_nx(self):    
        dist = 3
        pattern = "_"
        self.rot_right -= 1
        self.rot_right = (1 if self.rot_right < 1 else self.rot_right)
        # self.current_image = self.__getattribute__(f"image_0{self.rot_right}")
        if self.rot_right == 1:
            self.x += dist
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
            

                                                                                                   
                                                            
    def handle_keys(self):
        """ Handles Keys """
        
        # CHECK THAT ALL IMAGES HAVE BEEN CREATED

        key = pygame.key.get_pressed()
        dist = 3 # distance moved in 1 frame, try changing it to 5
        if key[pygame.K_DOWN]: # down key
            pattern = self.rotation_px()
            # self.rot_right = 1
            # move up
            if self.rotation_nx == 1:
                self.y += dist
            
            pattern = "_0"
            self.rot_right = (1 if self.rot_right < 1 else self.rot_right)
            # self.current_image = self.__getattribute__(f"image_0{self.rot_right}")
            if self.rot_right > 25:
                print("OK")
                self.y = self.y + dist
                print(self.y)
                pattern = "_"
                if (self.rot_right % 10) >= 6:
                    self.rot_right += 5
                    # self.y += dist

              
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
            # self.rot_right = 1
            # move up
            # if self.rotation_nx == 1:
            #     self.y -= dist
            
            if self.rot_right > 25:
                self.y -= dist
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
                
            
            self.current_image = self.__getattribute__(f"image{pattern}{self.rot_right}")

        elif key[pygame.K_RIGHT]: # right key
            self.x += dist
            # self.current_image = self.image_01
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
            # self.current_image = self.__getattribute__(f"image_0{self.rot_right}")
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
                    
                try:
                    self.current_image = self.__getattribute__(f"image{pattern}{self.rot_right}")
                except:
                    self.current_image = self.__getattribute__(f"image{pattern}{self.rot_right-((self.rot_right%10)-6)}")
                finally:
                    self.current_image = self.__getattribute__("image_01")
                    self.rot_right = 1


    def draw(self, surface):
        """ Draw on surface """
        # blit yourself at your current position
        surface.blit(self.current_image, (self.x, self.y))


screen = pygame.display.set_mode((1200, 600))

bird = Bird() # create an instance
clock = pygame.time.Clock()
# print(vars(bird))

running = True
while running:
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False

    bird.handle_keys() # handle the keys

    screen.fill((255,255,255)) # fill the screen with white
    bird.draw(screen) # draw the bird to the screen
    pygame.display.update() # update the screen

    clock.tick(40)


