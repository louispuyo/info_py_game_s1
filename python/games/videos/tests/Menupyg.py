import pygame
# from typing import Dict
pygame.init()



# screen = pygame.display.set_mode((400, 400))
RED = (255, 0, 0)
menu_data = {"title":"the title of the game", "key_to_start": pygame.K_SPACE, "bg_color":(10,90,0), "font_color":(155,155,155), "button_start":((200, 200, 130, 40),5, (245, 0, 20)),"button_option":((200, 300, 130, 40),5, (245, 0, 20))}
params_data = {"button_started_pressed":False}
# button (dimension, border width, color in hexa)


class Params(object):
    def __init__(self):
        self.button_started_pressed = False

# Group status condition 
params = Params()

# UTILS

def watcher(params):
    for p in params.keys():
        if params[p]:
            return params_data.__setattr__(p, True)


def click_handler_begin(obj_list, params=params, event=None):
        
    for obj in obj_list:
        if event.type == pygame.MOUSEBUTTONDOWN:

            if obj.collidepoint(event.pos):
                params.__setattr__(f'{obj}ed_pressed', True)
                return True
    return False

class Menu(object):
    def __init__(self, Menu_params:dict, screen):
        self.Menu_params = Menu_params
        self.screen = screen 
        for param in Menu_params.keys():
            self.__setattr__(param, self.Menu_params[param])
        
    def set_color(self, element, option="bground"):
        if option == "bground":
            self.screen.fill(self.Menu_params["bg_color"])
        else:
            pass

    
    def draw_button(self, name:str):
        tmp = self.Menu_params[name]
        size = (tmp[0][2], tmp[0][3])
        color = tmp[2]
        dimension = (tmp[0][0], tmp[0][1], tmp[0][2], tmp[0][3])
        rect_border = pygame.Surface(size)  # Create a Surface to draw on.
        pygame.draw.rect(rect_border, color, rect_border.get_rect(), tmp[1])  # Draw on it.
        rect_filled = pygame.Surface(size)
        pygame.draw.rect(rect_filled, color, rect_filled.get_rect())
        self.screen.blit(rect_border, (dimension[0],dimension[1]))
        self.display_text(name.replace("_", " "), size=15, position=(dimension[0]+10, dimension[1]+10))
        return (pygame.Rect(dimension), dimension)
        # pygame.rect.Rect(tmp[0][0], tmp[0][1], tmp[0][2], tmp[0][3])
        
            

    def display(self):
        for el in vars(self).copy():
            self.analyse(el)
            

   

    def display_text(self, message:str, position:tuple=(100, 100), font="arialroundedboldttf", size=25, color=(255, 255, 255)):
        font = pygame.font.match_font(font)
        myfont = pygame.font.Font(font, size)
        self.screen.blit(myfont.render(message, True, color), position)

    def analyse(self, index):
        if index == "title":
            return self.display_text(self.Menu_params[index])
        
        elif index == "bg_color":
            return self.set_color(self.Menu_params[index], option="bground", )

        elif index == "font_color":
            return self.display_text(self.Menu_params["title"], position=(90, 10))

        elif index.startswith("button"):
            self.__setattr__(index, self.draw_button(index)[0])
            # self.__setattr__(index+"_pos", self.draw_button(index)[1])
            return (self.__getattribute__(index),(200, 200))
            
        else:
            pass


# r = True
# while r:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             r = False
            

#     menu1 = Menu(menu_data)
#     menu1.display()
#     click_handler([menu1.button_start])
#     pygame.display.update()





"""
def click_handler(obj_list, joueur, joueur2):
   
   for obj in obj_list:
      if event.type == pygame.MOUSEBUTTONDOWN:


         if obj.rect.collidepoint(event.pos):
            print("click")

"""