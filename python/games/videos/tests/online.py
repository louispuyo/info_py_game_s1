import pygame 
from data import BANK


pygame.init()


PERS = {"p1":"python/games/videos/tests/img/hiclipart.com.png"} # 760x700
BLACK = (0,0,0)
WHITE = (255, 255, 255)
BACKGROUND = pygame.image.load("python/games/img/bg/bg_mod.jpg")
BACKGROUND = pygame.transform.scale(BACKGROUND, (1300, 700))
SCREEN_SIZE = (1300,700)
screen = pygame.display.set_mode((SCREEN_SIZE))
screen.blit(BACKGROUND, (0,0)) 



class Game(object):
    def __init__(self):
        self.online = False
        self.caractere = []
        self.running = True
        self.base = True
        ... 
        self._availables_caractere = []
        # other sub class attr


class SpriteSheet(object):

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


def refresh():
    screen.blit(BACKGROUND, (0,0))
    pygame.display.update()


class Env(object):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("python/games/videos/tests/img/hiclipart.com.png").convert()
        self.image.set_colorkey(WHITE)
        # self.block_list = pygame.sprite.Group()


class Person(object):
    def __init__(self, name, pos_x, pos_y, pos_z, sprite_sheet_data):
        self.name = name
        self.perso = SpriteSheet("python/games/videos/tests/img/hiclipart.com.png").get_image(sprite_sheet_data.SP_test_1[0],
                                                                                                sprite_sheet_data.SP_test_1[1],
                                                                                                sprite_sheet_data.SP_test_1[2],
                                                                                                sprite_sheet_data.SP_test_1[3])
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.pos_z = pos_z
        self.base = True
        self.right_1 = False
        self.right_2 = False
        self.left = False
        self.down = False
        self.base_img = SpriteSheet("python/games/videos/tests/img/hiclipart.com.png").get_image(sprite_sheet_data.SP_test_1[0], sprite_sheet_data.SP_test_1[1],
                                                                sprite_sheet_data.SP_test_1[2],
                                                                sprite_sheet_data.SP_test_1[3]) 
        self.right_img_1 = SpriteSheet("python/games/videos/tests/img/hiclipart.com.png").get_image(sprite_sheet_data.SP_test_2[0], sprite_sheet_data.SP_test_2[1],
                                                                sprite_sheet_data.SP_test_2[2],
                                                                sprite_sheet_data.SP_test_2[3])
        self.right_img_2 = SpriteSheet("python/games/videos/tests/img/hiclipart.com.png").get_image(sprite_sheet_data.SP_test_3[0], sprite_sheet_data.SP_test_3[1],
                                                                sprite_sheet_data.SP_test_3[2],
                                                                sprite_sheet_data.SP_test_3[3])
        self.right_img_3 = SpriteSheet("python/games/videos/tests/img/hiclipart.com.png").get_image(sprite_sheet_data.SP_test_6[0], sprite_sheet_data.SP_test_6[1],
                                                                sprite_sheet_data.SP_test_6[2],
                                                                sprite_sheet_data.SP_test_6[3]) 
        # self.image = pygame.Surface([15, 15])
        self.image = pygame.image.load(PERS[f"{name}"])
        # self.image.fill(BLACK)            
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()


    def deplacement3D(self, dx, dy, dz):
        self.pos_x += dx
        self.pos_y += dy
        self.pos_z += dz


    def rot_center(self, angle):
        """rotate an image while keeping its center"""
        rot_image = pygame.transform.rotate(self.image, angle)
        rot_rect = rot_image.get_rect(center=self.rect.center)
        return rot_image,rot_rect

game = Game()
P1 = Person("p1", 200, 200, 100, BANK.SP_test())


while game.running:
    screen.blit(BACKGROUND, (1200,700)) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game.running = False

        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:

                if P1.right_1:
                    screen.blit(BACKGROUND, (0,0))

                    print("right")
                    P1.right_1 = False
                    P1.right_2 = True
                    screen.blit(P1.right_img_1, (200, 200))
                # refresh()
                elif P1.right_2:
                    screen.blit(BACKGROUND, (0,0))

                    print("right2")
                    screen.blit(P1.right_img_2, (200, 200))
         
                
                # P1_1.perso
                # P1_2.perso
                # P1_3.perso
                # P1_4.perso
                # P1_5.perso
                
                P1.base = False
                P1.right_1 = True
        
            elif event.key == pygame.K_UP:
                if P1.base:
                    print("up")
                P1.base = True
                screen.blit(BACKGROUND, (0,0))
                # if game.base:
                #     screen.blit(P1.base_img, (200, 200))

                
    if P1.base:
        screen.blit(P1.base_img, (200, 200))

    # screen.blit(BACKGROUND, (1200,700)) 
    screen.blit(P1.right_img_1, (500, 500))
    screen.blit(P1.right_img_2, (500, 500))


    pygame.display.update()
