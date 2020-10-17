import pygame

pygame.init()

class Weapons:
    def __init__(self, attack, defense, speed_up, speed_down, speed_right, speed_left):
        self.dimension = (500,500)
        self.tire_position = (0,0)
        self.py = pygame
        self.x = -100
        self.y = 100
        self.bx = -100
        self.by = 100
        self.speed_up = speed_up
        self.speed_down = speed_down
        self.speed_left = speed_left
        self.speed_right = speed_right
        self.bulletImg = pygame.image.load('python/games/img/png/029-vortex.png')
        self.missileImg = pygame.image.load('python/games/img/png/008-ufo.png')
        self.bullet = pygame.transform.scale(self.bulletImg, (10,10))
        self.missile = pygame.transform.scale(self.missileImg, (20,20))
        self.shooted = False
        self.shot = False


    def shoot(self):

        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_SPACE:
                    self.shot = True
                    return self.tire()
        
                
                    
    def tire(self):
         img = pygame.transform.scale(self.bulletImg, (30,30))
         return img
         

    def tire_missile(self, bx, by):

         img = pygame.transform.scale(self.missileImg, (40,40))
         
        
    def mega_missile(self, bx, by):
        pass




class Personnage_X(pygame.sprite.Sprite):
	
	spriteSheet = pygame.image.load("advnt_full.png").convert_alpha()
	
	sequences = [(0,1,False),(1,6,True),(7,3,False)]
	
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
	
		self.image = Personnage.spriteSheet.subsurface(pygame.Rect(0,0,32,64))
		self.rect = pygame.Rect(0,0,32,64)
		self.rect.bottom = HEIGHT

		self.numeroSequence = 0
		self.numeroImage = 0
		self.flip = False

		self.deltaTime = 0
		self.vitesse = int(round(100/FPS))
			
	def update(self,time):
		self.deltaTime = self.deltaTime + time
		
		if self.deltaTime>=150:
			self.deltaTime = 0
			
			n = Personnage.sequences[self.numeroSequence][0]+self.numeroImage
			self.image = Personnage.spriteSheet.subsurface(pygame.Rect(n%10*32,n//10*64,32,64))
			if self.flip:
				self.image = pygame.transform.flip(self.image,True,False)
			
			self.numeroImage = self.numeroImage+1
			
			if self.numeroImage == Personnage.sequences[self.numeroSequence][1]:
				if Personnage.sequences[self.numeroSequence][2]:
					self.numeroImage = 0
				else:
					self.numeroImage = self.numeroImage-1
	
	def setSequence(self,n):
		if self.numeroSequence != n:
			self.numeroImage = 0
			self.numeroSequence = n
	
	def goRight(self):
		self.rect = self.rect.move(self.vitesse,0).clamp(rectScreen)
		self.flip = False
		self.setSequence(1)
	
	def goLeft(self):
		self.rect = self.rect.move(-self.vitesse,0).clamp(rectScreen)
		self.flip = True
		self.setSequence(1)