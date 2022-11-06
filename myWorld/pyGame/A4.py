import pygame 
from pygame.locals import *
from sys import exit
import os
full_screen = (1366,768)
half_screen = (800,600)
while True:
    print('Would love to play the game on Full Screen?')
    print('A. Yes')
    print('B. No')
    ipt = input('')
    if ipt == 'A' or ipt == 'a':
        window_size = full_screen
        break
    if ipt == 'B' or ipt == 'b':
        window_size = half_screen
        break
    print('Error: please select between, A and B')
windowPosF = (0,0)
windowPosH = (50,50)
windowPos = windowPosH
def moveWindow(windowP):
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % windowP
pygame.init()
def screens(screen): 
    screen = pygame.display.set_mode(window_size)
    return screen
caption = pygame.display.set_caption('@Asquare_Games')
dark = (0,0,0)
light = (255,255,255)
background_color = light


while True:
    if window_size is half_screen:
        windowPos = windowPosH
    elif window_size is full_screen:
        windowPos = windowPosF
    moveWindow(windowPos)
    screen = screens(window_size)
    screen.fill(background_color)
    x = screen.get_width()
    
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        
        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()
            if event.key == K_d:
                if background_color is light:
                    background_color = dark
                elif background_color is dark:
                    background_color = light
            """if event.key == K_f:
                if window_size is half_screen:
                    window_size = full_screen
                elif window_size is full_screen:
                    window_size = half_screen"""
    pygame.display.update()