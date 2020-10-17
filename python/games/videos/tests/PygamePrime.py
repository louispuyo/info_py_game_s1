import pygame
from pygame.locals import *
from typing import List
from Math_pygame import scalar
import Env
import Menupyg

pygame.init()


# ENV INIT
DIMENSION = (1200, 600)
WHITE = (255,255,255)
BLACK = (0,0,0)
screen = pygame.display.set_mode(DIMENSION)
# REAL INIT
Env1 = Env.Image(Env.data)
menu1 = Menupyg.Menu(Menupyg.menu_data, screen)

def show_fonts():
    for index, font in enumerate(pygame.font.get_fonts()):
        print(str(index)+" - "+font)


def display_text(message:str, position:tuple=(100, 100), font="arialroundedboldttf", size=25, color=(255, 255, 255)):
    font = pygame.font.match_font(font)
    myfont = pygame.font.Font(font, size)
    screen.blit(myfont.render(message, True, color), position)


def display_element(element_id:str):
    """ display a new image in the screen from the id of the image :
        ex: 'image_arbre1' -> display_element('arbre1') 
        screen.blit(image_arbre1,position_arbre1...) 
    """
    Element_image = Env1.Environement.__getattribute__(f"image_{element_id}")
    Element_position = Env1.Environement.__getattribute__(f"position_{element_id}")
    screen.blit(Element_image, Element_position)


def generate_decor(element_list_ids:List[str]):
    """ using the display_element function this function
    can be use to fill up your env with many element from a python dict
    and a special syntaxe cf:README
    """
    for element_id in element_list_ids:
        display_element(element_id)


def change_parameters(parameter:str, element_id:str, element_new_position:(tuple or int)=(0,0), relative=False, coef_of_change=(0.9,0.9)):
    if not relative:
        if parameter in ["image", "position", "size"]:
            Env1.Environement.__setattr__(f"{parameter}_{element_id}", element_new_position)
            return Env1
        else:
            return Exception("invalid key isnt't image, position or size !")

    else:
        if parameter in ["position", "size"]:
            old_position=Env1.Environement.__getattribute__(f"{parameter}_{element_id}")
            new_position = scalar(old_position, coef_of_change)
            Env1.Environement.__setattr__(f"{parameter}_{element_id}", new_position)
            return Env1
        
        else:
            return Exception("invalid key for relative param change only (position or size) !")


# def start_menu(started=False):
#     if not started:
#         Menupyg.Menu(Menupyg)



# TEST
def loop(is_running=True, bg_color=WHITE):
    screen.fill(bg_color)
    globals_params = Menupyg.Params()
    
    while is_running:
        for event in pygame.event.get():

            if event.type == QUIT:
                is_running = False

            elif event.type == KEYDOWN:
                if event.key == KEYUP:
                    print("up")
                if event.key == K_DOWN:
                    print("down")
                if event.key == K_LEFT:
                    print("left")
                if event.key == K_RIGHT:
                    print("rigth")
                    # add actions ...

            # MENU #
            elif not globals_params.button_started_pressed:
                menu1.display()
                pygame.display.update()
                globals_params.button_started_pressed = Menupyg.click_handler_begin([menu1.button_start], globals_params, event=event)
                


        # MAIN # GAME #
        if globals_params.button_started_pressed:
            screen.fill(bg_color)
            display_text(menu1.title)
            # display_element('arbre1')
            # display_element('arbre2')
            # change_parameters("position", "arbre1", relative=True, coef_of_change=(0.91, 0.91))
            generate_decor(['arbre1', 'arbre2'])
            # display_text("no way", position=(200, 20))
            pygame.display.update()
    




loop()
# show_fonts()

# Env1 = Env.Image(Env.data)
# print(Env1.Environement.image_arbre1)