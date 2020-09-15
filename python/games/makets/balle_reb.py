
import pygame
import time
import sys

SCREEN_SIZE = WIDTH, HEIGHT = (640, 480)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 50, 50)
GREEN = (50, 255, 50)
CIRCLE_RADIUS = 30

# Initialization
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE)

pygame.display.set_caption('Game option info')
fps = pygame.time.Clock()
paused = False

# Ball setup
ball_pos1 = [50, 50]

mem = {}

class balle:
  def __init__(self):
    self.inc_x = 10
    self.inc_y = 10
    # self.x = 100 
    # self.y = 100

# ball_pos2 = [50, 240]
# ball_pos3 = [50, 430]

"""
func():
-> var: inc_x, inc_y 
-> if x > 999:
  inc_x = -inc_x


"""


# class Boost:

class Perso:
  def __init__(self):
    self.started_at = ((time.localtime().__getattribute__("tm_min")*60*200)+time.localtime().__getattribute__("tm_sec")*200)
    self.x = 300
    self.y = 400
    self.inc_x = 10
    self.inc_y = 10
  
p1 = Perso()

def move():
  pressed = pygame.key.get_pressed()
  if pressed[pygame.K_UP] and p1.y > 0: p1.y -= 5
  if pressed[pygame.K_DOWN] and p1.y < 480 - 60: p1.y += 5
  if pressed[pygame.K_LEFT] and p1.x > 0: p1.x -= 5
  if pressed[pygame.K_RIGHT] and p1.x < 630 - 60: p1.x += 5

# if pygame.type == pygame.KEYDOWN:
#   if pygame.K_LEFT:
    
def score():
  score = p1.started_at - ((time.localtime().__getattribute__("tm_min")*60*200)+time.localtime().__getattribute__("tm_sec")*200)
  return abs(score)

def play(pos, cx, cy):

  pos[0] += cx 
  pos[1] += cy
  return (cx, cy)
  
Bal = balle()

def conflict():
  if abs(p1.x-ball_pos1[0])<70:
    if abs(p1.y-ball_pos1[1])<60:
      return True
  if abs(p1.y-ball_pos1[1]) <70:
    if abs(p1.x-ball_pos1[0])<60:
      return True

  return False


def collide(form, ball_form):
  pass

def update():
  inc_x = Bal.inc_x
  inc_y = Bal.inc_y

  pos = ball_pos1
  if pos[0]>640:
    Bal.__setattr__('inc_x',-inc_x)
    # inc_y = (inc_y if (pos[1] < 540 & pos[1] > 2) else -inc_y)
  
  elif pos[0] < 2:
    Bal.__setattr__('inc_x',-inc_x)
    # inc_y = (inc_y if pos[1] < 540 else -inc_y)
  
  if pos[1] > 480:
    Bal.__setattr__('inc_y',-inc_y)
  
  elif pos[1] < 2:
    Bal.__setattr__('inc_y',-inc_y)
  
  pygame.display.set_caption("score:"+str(score()))
  play(pos, Bal.__getattribute__("inc_x"), Bal.__getattribute__("inc_y"))


def render():
    screen.fill(BLACK)
    ball_form = pygame.draw.circle(screen, RED, ball_pos1, CIRCLE_RADIUS, 0)
    p1_forme = pygame.draw.circle(screen, WHITE, (p1.x, p1.y), CIRCLE_RADIUS, 0)
    collide(p1_forme, ball_form)
    # pygame.draw.circle(screen, GREEN, ball_pos3, CIRCLE_RADIUS, 0)
    pygame.display.update()
    fps.tick(60)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                paused = not paused
        
              
        if conflict():
          print("Fail !")
          paused = True
        
          
          
    if not paused:
        update()
        move()
        render()  