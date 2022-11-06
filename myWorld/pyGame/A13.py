import pygame 
from pygame.locals import *
from sys import exit
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
    screen.lock()
    for i in range(100):
        ran_pos = (randint(0,799), randint(0,599))
        screen.set_at(ran_pos, ran_col)
    screen.unlock()
    pygame.display.update()