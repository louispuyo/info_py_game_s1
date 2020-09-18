import pygame
import sys
pygame.init()

text_size = 30
myfont = pygame.font.Font(None, text_size) 
perso_dict = {0:"galas0", 1:"gorgon", 2:"freeze", 3:"theodore",4:"BlueBeam"}
weapon_dict = {0: "standard", 1:"war", 2:"mars", 3:"techno", 4:"freezer"}


def menu(screen, list_to_disp, menu_condition=True):
    while menu_condition:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu_condition = False
                sys.exit()
            
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_0:
                    perso = perso_dict[0]
                    menu_condition = False
                    return perso

                if event.key == pygame.K_1:
                    perso = perso_dict[1]
                    menu_condition = False
                    return perso

                if event.key == pygame.K_2:
                    perso = perso_dict[2]
                    menu_condition = False
                    return perso
                    
                if event.key == pygame.K_3:
                    perso = perso_dict[3]
                    menu_condition = False
                    return perso

                if event.key == pygame.K_4:
                    perso = perso_dict[4]
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

                if event.key == pygame.K_0:
                        perso = weapon_dict[0]
                        menu_condition = False
                        return perso
                    
                if event.key == pygame.K_1:
                        perso = weapon_dict[1]
                        menu_condition = False
                        return perso
                    
                if event.key == pygame.K_2:
                        perso = weapon_dict[2]
                        menu_condition = False
                        return perso
                
                if event.key == pygame.K_3:
                        perso = weapon_dict[3]
                        menu_condition = False
                        return perso
                
                if event.key == pygame.K_4:
                        perso = weapon_dict[4]
                        menu_condition = False
                        return perso
                
                


                
        screen.fill((0,0,0))
        for index, el in enumerate(list_to_disp):
            caption = myfont.render(f"{index} : {el.name} ", True,(255, 255, 255))
            screen.blit(el.bullet, (220, (index+1)*60))
            screen.blit(el.missile, (300, (index+1)*60))
            screen.blit(caption, (50, (index+1)*60))
            
            
            
        
        pygame.display.update()