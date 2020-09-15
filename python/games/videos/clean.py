import pygame 
from utils.bases import Screen, Personnage, colision, Weapons_list, HeathBare
from utils.elements import enemies
# from utils.advanced import Weapons


# Screen
Screen_class = Screen(background="/Users/snowden/Documents/COURS_L1S1/option_info/python/games/img/bg/bg2.jpg", dimension=(500, 700))
screen = Screen_class.screen

# fonts 
text_size = 30
myfont = pygame.font.Font(None, text_size) 



# Players ex:(galas0)
# CHOOSE
Player_class = Personnage("galas0")
player = Player_class.small_image
#
# ##

# bots
e0 = enemies["vilan"]
e1 = enemies["kratos"]
# accesoires  (ie: standard, war)
name = "war"
w0 = Weapons_list[name]
kratos_h = HeathBare(e1)
# Weapons(20, 200, 30, 20, 20, 50, "029-vortex.png","029-vortex.png")
shoot = w0.shoot
shoot


# independant functions
def show_score(x, y):
    # score = myfont.render("score: "+str(score_value), True,(0, 0, 0))
    score = myfont.render("score: "+str(score_value), True,(255, 255, 255))
    screen.blit(score, (x, y))

def show_stock(x, y):
    # stock_label = myfont.render("stock: "+str(stock_value), True,(0, 0, 0))
    stock_label = myfont.render("stock: "+str(stock_value), True,(255, 255, 255))
    screen.blit(stock_label, (x, y))

def show_HeathBare(x, y, level=0):
    if level < 0:
        level = 0
    stock_label = myfont.render("HP: "+str(level), True,(255, 255, 255))
    screen.blit(stock_label, (x, y-30))
    color = (0,200,0)
    if level <= 0:
        level = 0
        color = (200, 0, 0)

    pygame.draw.rect(screen, color, (x, y, level, 10))
    # screen.blit(screen, vie)


# MAIN
boost = False
stock_value = 10
score_value = 0
running = True
shooted = True
missile_drop = False
dropped = False
bullet = False
in_live = True
kratos = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shooted = False
                missile_drop = False
                dropped = False
            
            if event.key == pygame.K_p:
                missile_drop = True
                shooted = False
                bullet = False
            
            if event.key == pygame.K_n:
                in_live = True
            
            if event.key == pygame.K_2:
                kratos = True
                # print("key 2 pressed")
            if event.key == pygame.K_b:
                print("boost")
                boost = True
                stock_value -= 2
            

   
    # Actions
    screen.fill((0,0,0))
    Screen_class.set_bg()
    Player_class.move()
    e0.moving()

   


    if boost:
        if (Player_class.speed_up > 0 and stock_value >= 0):
            Player_class.speed_up = Player_class.speed_up + 1
            boost = False

    if missile_drop:
        w0.bx = Player_class.x 
        w0.by = Player_class.y 

        missile = w0.tire_missile(w0.bx, w0.by)
        dropped = True
        bullet = False
        missile_drop = False
        screen.blit(missile, (w0.bx, w0.by))
    
    if dropped:
        if ((w0.bx > 0)and(w0.bx < 500)):
            if ((w0.by < 400) and (w0.by > 0)):
                if name == "war":
                    w0.by = w0.by - w0.missile_speed
                else:
                    w0.bx = w0.bx + w0.missile_speed//4
                    w0.by = w0.by + w0.missile_speed 

                bullet = False
                missile = w0.tire_missile(w0.bx, w0.by)
                screen.blit(missile, (w0.bx, w0.by))


    if kratos:
        e1.moving()
        # screen.blit(screen, kratos_h.disp_jauge())
        if colision(Player_class, e1):
            Player_class.defense = Player_class.defense - e1.attack
            if Player_class.defense <= 0:
                running == False
        

    if shooted == False:
        w0.bx = Player_class.x+18
        w0.by = Player_class.y
        # print("shoot")
        shooted = True
        bullet = True


        
    if shooted:
        if bullet == True:
            w0.by = w0.by-7
            screen.blit(w0.bullet, (w0.bx, w0.by))

    # Condition
    if colision(w0, e0, bullet_mode=True):
        bullet = False
        in_live = False
        dropped = False
        missile = False
        score_value += 100
    
    if colision(w0, e1, bullet_mode=True):
        bullet = False
        missile = False
        dropped = False
        if e1.defense < 0:
            kratos = False
            e1.defense = 1000
            score_value += 5000
        else:
            e1.defense = e1.defense - Player_class.attack
        
    # Standard Display
    show_score(10,600)
    show_stock(10,640)
    show_HeathBare(400, 600, level=Player_class.defense)

    # blit on screen
    screen.blit(player, (Player_class.x, Player_class.y))
    if in_live: screen.blit(e0.small_image, (e0.x, e0.y))
    if kratos: screen.blit(e1.small_image, (e1.x, e1.y))
    pygame.display.update()