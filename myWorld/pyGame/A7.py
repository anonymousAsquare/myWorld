import pygame
from pygame.locals import *
from sys import exit

pygame.init()
window_size = (800,600)
screen = pygame.display.set_mode(window_size,NOFRAME,32)
fullScreen = False
while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()
            if event.key == K_f:
                fullScreen = not fullScreen
                if fullScreen:
                    screen = pygame.display.set_mode(window_size,DOUBLEBUF|HWSURFACE,32)
                    #screen = pygame.display.set_mode(window_size,FULLSCREEN,32)
                    #screen = pygame.display.set_mode(window_size,HWSURFACE|FULLSCREEN,32)
                    #screen = pygame.display.set_mode(window_size,NOFRAME,32)
                    
                else:
                    screen = pygame.display.set_mode(window_size,NOFRAME,32)
                    #screen = pygame.display.set_mode(window_size,0,32)
                    
    #pygame.display.update()
    pygame.display.flip()