import pygame
from sys import exit
from pygame.locals import *
from random import randint
pygame.init()

screen = pygame.display.set_mode((800,600),0,32)
point = []
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()
        if event.type == MOUSEBUTTONDOWN:
            point.append(event.pos)
            if len(point) > 100:
                del point[0]
    
    screen.fill((255,255,255))

    if len(point) > 1:
        pygame.draw.lines(screen,(0,0,255),False,point,2)
        #pygame.draw.aalines(screen,(0,0,255),False,point,2)
        """start = point[0]
        for i in point:
            pygame.draw.aaline(screen,(0,0,255),start,i,2)
            start = i"""
    
    pygame.display.update()