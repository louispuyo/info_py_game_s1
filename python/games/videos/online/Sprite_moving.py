import pygame
from PIL import Image
pygame.init()

screen = pygame.display.set_mode((1200, 700))
running = True

perso = {"standard":"/Users/snowden/Documents/COURS_L1S1/option_info/python/games/videos/online/images/TrashPanda/TrashPanda_front.png"}

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
    return (image_rgb.getpixel((i, 25)))

class Sprite:
    def __init__(self, image_path, perso_img=perso["standard"]):
        self.image = pygame.image.load(image_path).convert().convert_alpha()
        self.surface = pygame.Surface((1200, 700))
        self.color = get_pixel_color(image_path)
        self.perso = pygame.image.load(perso_img)
        # self.background = [terrain1, terrain1, terrain2, terrain2, terrain2, terrain1]
    
    def blit(self, pos_x, pos_y):
        self.surface.blit(self.image, (pos_x, pos_y))
        return self.surface
    
    def blit_perso(self, pos_x, pos_y):
        self.surface.blit(self.perso, (pos_x, pos_y))
        return self.surface

class Personage(Sprite):
    def __init__(self):
        # im = "/Users/snowden/Documents/COURS_L1S1/option_info/python/games/videos/tests/data/background_01.png"
        # super().__init__(self, im)
        self.head = pygame.draw.circle(screen, 200, (220, 223), 100)
        self.body = pygame.draw.rect(screen, (0,222,111), (100, 222, 223//10, 300//10), 100//10)
        self.elment = pygame.draw.rect(screen, (0,11,111), (100, 150, 200, 333//10), 10)


        



s0 = Sprite("/Users/snowden/Documents/COURS_L1S1/option_info/python/games/videos/tests/img/background_01.png")
x = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                x-=10
            
            if event.key == pygame.K_LEFT:
                x+=10

    screen.fill(s0.color)
    screen.blit(s0.blit(0, 0), (x, 10))
    screen.blit(s0.blit_perso(50, 0), (0, 600))
    p1c = Personage()
    p1c.head
    p1c.body
    pygame.display.update()
