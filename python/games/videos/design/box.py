import pygame

pygame.init()


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


    def loop(self):
        return """
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        

            pygame.display.update()
            """


screen = Screen().screen


class Cube():
    def __init__(self, l, h, L):
        self.x = l
        self.y = L
        self.z = h
        self.volume = self.x*self.y*self.z

    
    def build(self):
        pygame.draw.line(screen,(255, 255, 255), (100,300), (100, 20), 5)
        pygame.draw.line(screen,(255, 255, 255), (self.x,5), (self.x, 300), 5)
        pygame.draw.line(screen,(255, 255, 255), (self.x,300), (100, 300), 5)
        pygame.draw.line(screen,(255, 255, 255), (self.x,100), (100, 100), 5)
        # pygame.draw.rect(screen, (40, 10), (49, 100), 10)
        
        # pygame.draw.line(screen,(255, 255, 255), (self.x,self.y), (self.x, 20), 5)
        # pygame.draw.line(screen,(255, 255, 255), (self.z,5), (self.z, self.y), 5)
        # pygame.draw.line(screen,(255, 255, 255), (self.z,self.y), (self.x, self.y), 5)

    def move_x(self):
        screen.fill((0,0,0))
        pygame.draw.line(screen,(255, 255, 255), (100,300), (100, 20), 5)
        pygame.draw.line(screen,(255, 255, 255), (self.x,5), (self.x, 300), 5)
        pygame.draw.line(screen,(255, 255, 255), (self.x,300), (100, 300), 5)
        pygame.draw.line(screen,(255, 255, 255), (self.x,100), (100, 100), 5)
        



C = Cube(400, 20, 10)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            pass

    
    

    C.move_x()
    pygame.display.update()
        
