# -*- coding: utf-8 -*-
 
import pygame
from pygame.locals import *
 
# On initialise pygame
pygame.init()
taille_fenetre = (600, 400)
fenetre_rect = pygame.Rect((0, 0), taille_fenetre)
screen_surface = pygame.display.set_mode(taille_fenetre)
 
BLEU_NUIT = (  5,   5,  30)
VERT      = (  0, 255,   0)
JAUNE     = (255, 255,   0)
 
timer = pygame.time.Clock()
 
joueur = pygame.Surface((25, 25))
joueur.fill(JAUNE)
# Position du joueur
x, y = 25, 100
# Vitesse du joueur
vx, vy = 0, 0
# Gravité vers le bas donc positive
GRAVITE = 2
 
mur = pygame.Surface((25, 25))
mur.fill(VERT)
 
niveau = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
 
def dessiner_niveau(surface, niveau):
    """Dessine le niveau sur la surface donnée.
 
    Utilise la surface `mur` pour dessiner les cases de valeur 1
    """
    for j, ligne in enumerate(niveau):
        for i, case in enumerate(ligne):
            if case == 1:
                surface.blit(mur, (i*25, j*25))
 

def from_coord_to_grid(pos):
    """Retourne la position dans le niveau en indice (i, j)
 
    `pos` est un tuple contenant la position (x, y) du coin supérieur gauche.
    On limite i et j à être positif.
    """
    x, y = pos
    i = max(0, int(x / 25))
    j = max(0, int(y / 25))
    return i, j

def get_neighbour_blocks(niveau, i_start, j_start):
    """Retourne la liste des rectangles autour de la position (i_start, j_start).
 
    Vu que le personnage est dans le carré (i_start, j_start), il ne peut
    entrer en collision qu'avec des blocks dans sa case, la case en-dessous,
    la case à droite ou celle en bas et à droite. On ne prend en compte que
    les cases du niveau avec une valeur de 1.
    """
    blocks = list()
    for j in range(j_start, j_start+2):
        for i in range(i_start, i_start+2):
            if niveau[j][i] == 1:
                topleft = i*25, j*25
                blocks.append(pygame.Rect((topleft), (25, 25)))
    return blocks 

# Boucle événementielle
def collision(niveau, pos):
    rect = pygame.Rect(pos, (25, 25))
    i, j = from_coord_to_grid(pos)
    for block in get_neighbour_blocks(niveau, i, j):
        if rect.colliderect(block):
            return True
    return False
 
# Boucle événementielle
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                vy = -20
 
    timer.tick(30)
    keys_pressed = pygame.key.get_pressed()
    # Sauvegarde de l'ancienne position
    old_x, old_y = x, y
    vx = (keys_pressed[K_RIGHT] - keys_pressed[K_LEFT]) * 5
    vy += GRAVITE
    vy = min(20, vy) # vy ne peut pas dépasser 25 sinon effet tunnel...
    x += vx
    y += vy
    if collision(niveau, (x, y)):
        x, y = old_x, old_y
 
    screen_surface.fill(BLEU_NUIT)
    dessiner_niveau(screen_surface, niveau)
    screen_surface.blit(joueur, (x, y))
    pygame.display.flip()
 
pygame.quit()