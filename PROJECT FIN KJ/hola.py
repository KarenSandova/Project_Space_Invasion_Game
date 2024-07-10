





import pygame
import random

pygame.init()
pygame.mixer.init()

fondo = pygame.image.load()
laser_sonido = pygame.mixer.Sound ()
explosion_sonido = pygame.mixer.Sound()
golpe_sonido = pygame.mixer.Sound()

explosion_list = []
for i in range (1,13):
    explosion = pygame.image.load()     
    explosion_list.append(explosion)
    
width = fondo.get_with()
height=
window = 
pygame.display.set_caption('Play Space Invaders')
run =
fps = 60
clock =
score= 
