import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen_size = (800,600)
screen = pygame.display.set_mode(screen_size,RESIZABLE,32)
backgrounImg = pygame.image.load('background.png').convert()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()
        if event.type == VIDEORESIZE:
            screen_size = event.size
            screen = pygame.display.set_mode(screen_size,RESIZABLE,32)
            pygame.display.set_caption("Window resized to "+str(event.size))
    
    screen_Width, screen_height = screen_size
    for y in range(0,screen_height,backgrounImg.get_height()):
        for x in range(0,screen_Width,backgrounImg.get_width()):
            screen.blit(backgrounImg,(x,y))
    pygame.display.update()