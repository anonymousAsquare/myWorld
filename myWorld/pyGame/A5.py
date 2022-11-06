from turtle import Screen
import pygame
from sys import exit
from pygame.locals import *

pygame.init()
#print(pygame.display.list_modes())
window_size = (800,600)
Screen= pygame.display.set_mode(window_size,0,32)
backgrounImg = pygame.image.load('background.png').convert()

FullScreen = True
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()
            if event.key == K_f:
                FullScreen = not FullScreen
                print(FullScreen)
                if FullScreen:
                    Screen = pygame.display.set_mode(window_size,FULLSCREEN,32)
                else:
                    Screen = pygame.display.set_mode(window_size,0,32)
    
    Screen.blit(backgrounImg,(0,0))
    pygame.display.update()
            