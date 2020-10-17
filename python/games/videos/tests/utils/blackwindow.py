import pygame

pygame.init()
fps = pygame.time.Clock()







class Screen(object):
    def __init__(self, dimension=(500,500), title="window", background=None):
        BLACK = (0,0,0)
        self.dimension = dimension
        self.background = (None if background is None else pygame.image.load(background))
        self.screen = pygame.display.set_mode(dimension)
        self.title = self.caption
        self.surface = self.screen.fill(BLACK)
        self.py = pygame

    
    def set_bg(self):
        if self.background is None:
            pass
        else:
            self.screen.blit(self.background, [0,0])

    
    def caption(self, text="the Game"):
        """ add a caption : "legende" is french """
        self.py.display.set_caption(text)


    def refresh(self, Fond=(0,0,0)):
        # self.screen.fill(Fond)
        self.py.display.update()
    
    def insert(self, element:object):
        self.screen.blit(element.small_image, (element.x, element.y))
        self.py.display.flip()

    
    def loop(self, exps):
        running = True
        while running:
            for event in self.py.event.get():
                if event.type == self.py.QUIT:
                    running = False
        

            self.refresh()


class Image(Screen):

    def __init__(self, image_path, x_custom=100, y_custom=100, x=10, y=10):
        self.py = pygame
        self.speed_up = 5
        self.speed_down = 5
        self.speed_right = 10     
        self.speed_left = 10
        self.x = x
        self.y = y
        self.image = pygame.image.load(image_path)
        self.small_image = pygame.transform.scale(self.image, (50, 60))
        self.custom_image = pygame.transform.scale(self.image, (x_custom, y_custom))
        self.screen = Screen()
        self.refresh = self.screen.refresh
        # self.background_set = self.set_bg

    def move(self):
        self.insert(self.small_image)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and self.y > 0: self.y -= self.speed_up
        if pressed[pygame.K_DOWN] and self.y < 480 - 60: self.y += self.speed_down
        if pressed[pygame.K_LEFT] and self.x > 0: self.x -= self.speed_left
        if pressed[pygame.K_RIGHT] and self.x < 630 - 60: self.x += self.speed_right
        # self.refresh()
    
class Element(Screen):
    def __init__(self, x:int, y:int, dimension:list, colors:list, filled:int):
        self.py = pygame
        self.image = Image("python/games/img/alien.png")
        self.x = self.image.x
        self.y = self.image.y
        self.speed_up = 5
        self.speed_down = 5
        self.speed_right = 10     
        self.speed_left = 10
        self.dimension = dimension
        self.screen = Screen().screen
        self.surface = pygame.draw.rect(self.screen, colors, dimension, filled)

    def move(self):
        self.screen.fill((0,0,0)) 
        bg = self.py.image.load("python/games/img/bg/bg2.jpg")
        self.screen.blit(bg, [0,0])
        # self.set_bg()
        self.insert(self.image)
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP] and self.image.y > 0: self.image.y -= self.speed_up
        if pressed[pygame.K_DOWN] and self.image.y < 480 - 60: self.image.y += self.speed_down
        if pressed[pygame.K_LEFT] and self.image.x > 0: self.image.x -= self.speed_left
        if pressed[pygame.K_RIGHT] and self.image.x < 630 - 60: self.image.x += self.speed_right
        # self.refresh()
        # fps.tick(30)




# i0 = Image("python/games/img/alien.png")
# e0 = Element(10, 10, (30, 30, 42, 40), (200,100,100), 10)



# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

        
#     e0.move()
        



