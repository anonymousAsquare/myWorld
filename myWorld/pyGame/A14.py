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
    screen.lock()
    for i in range(10):
        ran_col = (randint(0,255),randint(0,255),randint(0,255))
        ran_pos = (randint(0,799),randint(0,599))
        ran_size = (799 - randint(ran_pos[0],799), 599 - randint(ran_pos[1],599))
        pygame.draw.rect(screen,ran_col,Rect(ran_pos,ran_size))
    screen.unlock()
    pygame.display.update()