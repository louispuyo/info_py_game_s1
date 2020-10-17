
import pygame 
from PIL import Image

pygame.init()
screen = pygame.display.set_mode((500, 500))

question = ["how are u ?", "how did you hear about that organisation ?"]

def l():
    return lambda indice: input(f"{question[indice]} -->  ");


def decorator(magasin1="drugs"):
    return f"""
    {magasin1}

  |-,-,-,--***    _   |
  | ----| |   |_|  |
  |  #X | |        | 
  | ----| |________|
*******************|
   ###             |
                   |
         ###       |
    !!++++++++++!! |
        """

def decoder():
    space = 0
    deco = decorator()
    for index,i in enumerate(deco):
        if i == " ":
            space += 1
        if i == "|":
            deco.split(",")[index%3] = " "
            pygame.draw.line(screen, (10, 122, 122), (10, 10),(space, 10+space))



# for i in range(len(question)):
#     print(l().__call__(i))
#     # print(decorator())

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
    
#     decoder()
#     pygame.display.update()

src="/Users/snowden/Documents/COURS_L1S1/option_info/python/games/videos/tests/img/hiclipart.com.png"

image = Image.open(src)
compteur_wpx = 0 
image_rgb = image.convert("RGB")
print(image.size[0]/6)
print(image.size[1]/5)

# for (i, j) in zip(range(50), range(50)):
#     print(image_rgb.getpixel((i, j)))




# i=0
# c=0
# j=0
# while c < 5:
#     while image_rgb.getpixel((i, 50)) == (255, 255, 153):
#         i += 1 
#     while image_rgb.getpixel((i, 50)) == (34, 34, 34):
#         j += 1
#     else:
#         print(image_rgb.getpixel((i, 50)))

#     c += 1
#     print(j)
#     print(i)


def get_pixel_color(image):
    image = Image.open(image)
    compteur_wpx = 0 
    image_rgb = image.convert("RGB")
    coords_sep = [(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0), (0,0)]
    nb_cut = 0
    for i in range(image.size[0]):
        if image_rgb.getpixel((i, 25)) == (255, 255, 153):
            # print(compteur_wpx)
            compteur_wpx += 1
            if compteur_wpx > 70:
                # print("cut")
                coords_sep[nb_cut] = (i, 45)
                nb_cut += 1
                compteur_wpx = 0
        else:
            compteur_wpx = 0
    print(nb_cut)
    print(coords_sep)
    return coords_sep


s0 = get_pixel_color("/Users/snowden/Documents/COURS_L1S1/option_info/python/games/videos/tests/img/hiclipart.com.png")


run = True
width = 130
height = 130
COORDS = (s0[0][0], 120, s0[1][0], height)
image = pygame.Surface([130, 130]).convert()
sprite_sheet = pygame.image.load("/Users/snowden/Documents/COURS_L1S1/option_info/python/games/videos/tests/img/hiclipart.com.png").convert()


while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_0:
                image.fill((0,0,0))
                COORDS = (s0[0][0], 130, s0[0][0], height)
        
            if event.key == pygame.K_1:
                image.fill((0,0,0))
                COORDS = (s0[1][0], 130, width, height)
        
            if event.key == pygame.K_2:
                image.fill((0,0,0))
                COORDS = (s0[2][0], 130, width, height)
        
            if event.key == pygame.K_3:
                image.fill((0,0,0))
                COORDS = (s0[3][0], 130, width, height)
        
            if event.key == pygame.K_4:
                # screen.fill((0,0,0))
                image.fill((0,0,0))

                COORDS = (s0[4][0], 130, width, height)
    
    
    image.blit(sprite_sheet, (0,0), COORDS)

    screen.blit(image, (30, 30))
    pygame.display.update()
