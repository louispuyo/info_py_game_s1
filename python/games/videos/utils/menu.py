import pygame
import sys
pygame.init()

text_size = 30
myfont = pygame.font.Font(None, text_size) 
perso_dict = {0:"galas0", 1:"gorgon", 2:"freeze"}
weapon_dict = {0: "standard", 1:"war", 2:"mars"}


def menu(screen, list_to_disp, menu_condition=True):
    while menu_condition:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_condition = False
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                for event.key in range(len(list_to_disp)):
                    perso = perso_dict[event.key]
                    print(str(event.key))
                    menu_condition = False
                    return perso


        screen.fill((0,0,0))
        for index, el in enumerate(list_to_disp):
            caption = myfont.render(f"{index} : {el.name} ", True,(255, 255, 255))
            screen.blit(el.small_image, (220, (index+1)*60))
            screen.blit(caption, (50, (index+1)*60))
            
            
            
        
        pygame.display.update()




def menu_weapon(screen, list_to_disp, w_menu_condiction=True):
    while w_menu_condiction:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                w_menu_condiction = False
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                for event.key in range(len(list_to_disp)):
                    weapon_model = weapon_dict[event.key]
                    print(str(event.key))
                    w_menu_condiction = False
                    return weapon_model

                
        screen.fill((0,0,0))
        for index, el in enumerate(list_to_disp):
            caption = myfont.render(f"{index} : {el.name} ", True,(255, 255, 255))
            screen.blit(el.bullet, (220, (index+1)*60))
            screen.blit(el.missile, (300, (index+1)*60))
            screen.blit(caption, (50, (index+1)*60))
            
            
            
        
        pygame.display.update()