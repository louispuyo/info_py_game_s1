import Menupyg as mp
from utils.bases import Screen
import pygame 
import os
pygame.init()
pygame.mixer.init()


class Audio:
    def __init__(self, audio_file):
        self.content = pygame.mixer.music.load(audio_file)

    
    def play(self):
        pygame.mixer.music.play()

    
    def stop(self):
        pygame.mixer.music.stop()



class Text:
    def __init__(self):
        self.intro1 = " we are in 1967, cold war in vietnam... "
        self.intro2 = " tan long truong 19 yo, in jail in china hiring to hack usa system"
        self.intro3 = "in order to get free..."
        self.intro4 = "you will incarn one of those person.."
        self.intro5 = "Tan, Eleonore, Daniel"
        self.intro6 = "choose one above"
        self.intro7 = "sure ?"


class Image:
    def __init__(self, image_path, screen, coords=(100,100)):
        self.base_path = os.getcwd()
        self.screen = screen
        self.coords = coords
        self.tmp = pygame.image.load(self.base_path +f"/tests/img/{image_path}")
        self.image = pygame.transform.scale(self.tmp, (150, 150))
    
    def display(self):
        self.screen.blit(self.image, (self.coords))


menu_dt = mp.menu_data
# menu_dt["title"] = 
screen = Screen(dimension=(1400,600)).screen
screen.fill((0,0,0))
audio1 = Audio("tests/sounds/CYCLONE.mp3")
running = True
audio1.play()

inc = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            audio1.stop()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                inc += 1

        
    menu_dt["title"] = Text().__getattribute__(f"intro{inc}")
    # menu_dt["button_Start"][""]
    mp.Menu(menu_dt, screen).display()
    if inc == 6:
        Image("sample_image.png", screen).display()

    pygame.display.update()
