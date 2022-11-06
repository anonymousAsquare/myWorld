import pygame
from sys import *
from pygame.locals import *
from random import randint

pygame.init()

screen = pygame.display.set_mode((800,600),0,32)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()
        
    ran_col = (randint(0,255),randint(0,255),randint(0,255))
    ran_pos = (randint(0,799),randint(0,599))
    ran_rad = randint(1,200)
    pygame.draw.circle(screen,ran_col,ran_pos,ran_rad)
    pygame.display.update()