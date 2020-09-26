import pygame
import time
pygame.init()

first = True
TEXT_SIZE = 30
font = pygame.font.SysFont(None, TEXT_SIZE)
BACKGROUND = (0,0,0)
WHITE = (255,255,255)
RED = (255, 0, 0)
end = False
fill = False
end_2 = False
running = True
compteur = 0
screen = pygame.display.set_mode((700, 700))
nombre_alumettes = 12
acc = []
black_list = []

# alumette_img = pygame.image.load("")


class Game:
   def __init__(self, nb_allumettes, player_list):
      self.nb_allumettes = nb_allumettes
      self.player_list = player_list
      self.tours = 12
      self.max_player = 3
      self.black_list = []
      self.is_running = True
      # self.button_pass = pygame.draw.rect(screen, WHITE, (400, 400, 90, 90))


class Player:
   def __init__(self, name):
      self.name = name
      self.score = 0
      self.max_pioche = 3



player1 = Player("freeze")
player2 = Player("william")


game = Game(nombre_alumettes,[player1, player2])



class allumettes(object):
    def __init__(self, x:int, y:int, allumette_img_path:str):
       self.x = x
       self.y = y
       #self.image = self.get_image(allumette_img_path)
       self.rect = pygame.draw.rect(screen,(255,255,255),(x,y,20,200))
       self.bou = pygame.draw.rect(screen,(255,0,0),(x,y-20,20,20))
       self.name = ""

    def get_image(self, image):
       pygame.image.load(image)

def display(List):
   for el in List:
      el.rect
      el.bou
      


def id_pointer(name):
   try:
      nb = int(name[-2:])
      # print("###")
      return {"nb":nb}

   except:
      nb = int(name[-1])
      print(nb)
      return {"nb":nb}

   


def click_handler(obj_list, joueur, joueur2):
   
   
   for obj in obj_list:
      if event.type == pygame.MOUSEBUTTONDOWN:


         if obj.rect.collidepoint(event.pos):
	         # print(f"collide with {obj.name}")
            # obj.__setattr__('rect', pygame.draw.rect(screen,(0,0,0),(obj.x,obj.y,20,200)))
            # obj.__setattr__('bou', pygame.draw.rect(screen,(0,0,0),(obj.x,obj.y-20,20,20)))
            position = int(id_pointer(obj.name)["nb"])
            # Black List
               
               
            if int(position) not in game.black_list:
               # print("YES")
                  # print(position)
                  # acc.remove(acc[position])
               game.max_player = game.max_player-1
               game.nb_allumettes = game.nb_allumettes-1
               game.black_list.append(position)
               print(game.nb_allumettes)
               display_text(joueur.name+" is playing", color=BACKGROUND)
               display_text(joueur2.name+" is playing", color=BACKGROUND)
               display_text(joueur.name+" is playing")
               display_text("prend au moins une allumettes !", color=BACKGROUND, posx=200, posy=450)

               # first = False

               # screen.fill(BACKGROUND)
         
               nb_allumettes = game.nb_allumettes
               display(acc)
               textsurface = font.render(f"allumette restante :{nb_allumettes} ", False, (255,255, 255))
               textcleaner = font.render(f"allumette restante :{nb_allumettes+1} ", False, (0,0, 0))
               screen.blit(textcleaner, (10,10))
               screen.blit(textsurface, (10,10))
               acc[position].__setattr__('rect', pygame.draw.rect(screen,(0,0,0),(obj.x,obj.y,20,200)))
               acc[position].__setattr__('bou', pygame.draw.rect(screen,(0,0,0),(obj.x,obj.y-20,20,20)))

            
      # if game.button_pass.collidepoint(event.pos):
      #    print("click!")
            
            

def nombre_de_pioche(joueur, joueur2):
   # display_text(joueur.name+" is playing", color=BACKGROUND)
   # display_text(joueur2.name+" is playing", color=BACKGROUND)
   # display_text(joueur.name+" is playing")


   if (game.nb_allumettes)>0:
      click_handler(acc, joueur, joueur2)
      # display_text(joueur.name+" is playing", color=BACKGROUND)
      # display_text(joueur2.name+" is playing", color=BACKGROUND)
      # display_text(joueur.name+" is playing")

   elif (game.nb_allumettes)==0:
      print(f"GAME OVER for {joueur.name} !")
      game.is_running = False
      
   else:
      pass



def generator(nb_allumettes, base_x, base_y):
   for i in range(nb_allumettes):
      a = allumettes(base_x+i*40, base_y, "")
      a.__setattr__("name", f"a_{i}")
      acc.append(a)
   return acc



def display_text(message, color=WHITE, posx=190, posy=400):
   surface = font.render(message, False, color)
   screen.blit(surface, (posx, posy))

def refresh():
   screen.fill((BACKGROUND))
   pygame.display.update()

def fst(j1, j2):
   display_text(j1.name+" is playing", color=BACKGROUND)
   display_text(j2.name+" is playing", color=BACKGROUND)
   display_text(j1.name+" is playing")
   # game.max_player = game.max_player -1


# a1 = allumettes(100,100,"")
# a2 = allumettes(140,100,"")
# a3 = allumettes(180,100,"")

generator(game.nb_allumettes, 50, 50)
# generator(4, 50, 300)


while game.is_running:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         game.is_running = False
      
      if event.type == pygame.KEYDOWN:
         if event.key == pygame.K_RIGHT:
            print(f">>> {game.max_player}")
            if game.max_player < 3:

               # end_2 =
               # end = end_2
               end_tmp = end
               end = (not end_2)

               end_2 = end_tmp
               print(end)
            
               fill = True
               # display_text("prend au moins une allumettes !", color=BACKGROUND, posx=200, posy=450)
               
            else:
               
               display_text("prend au moins une allumettes !", color=RED, posx=200, posy=450)
               # time.sleep(2.7)
               # display_text("prend au moins une allumettes !", color=BACKGROUND, posx=200, posy=450)


   

   if first:
      if end:
         fst(player2, player1)
      else:
         fst(player1, player2)
   
      
      first = False
   # click_handler(acc)
   if (not end):
      # print(game.max_player)
      display_text(player1.name+" is playing", color=BACKGROUND)
      display_text(player2.name+" is playing", color=BACKGROUND)
      display_text(player1.name+" is playing")

  
      if fill:
         game.max_player = 3
         fill = False

      if (game.max_player > 0):
         nombre_de_pioche(player1, player2)
      else:
         end_2 = False
         end = True
         fill = True
      

   elif end_2 == False:
      display_text(player2.name+" is playing", color=BACKGROUND)
      display_text(player1.name+" is playing", color=BACKGROUND)
      display_text(player2.name+" is playing")
      
      # print(game.max_player)
      if fill:
         game.max_player = 3
         fill = False

      if (game.max_player > 0):
         # display_text(player1.name)
         
         nombre_de_pioche(player2, player1)
            # game.max_player = game.max_player-1
      else:
         end_2 = True
         end = False
         fill = True

   else:
      print("ERROR#")
      end = not end
      end_2 = not end_2
      first = True


   pygame.display.update()
