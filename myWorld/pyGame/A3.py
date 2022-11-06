import pygame
from pygame.locals import *
from sys import exit

pygame.init()
windowSize = (800,600)
screen = pygame.display.set_mode(windowSize,0,32)

font = pygame.font.SysFont('arial', 16)
font_height = font.get_linesize()
print(font_height)
eventText = []

while True:
    event = pygame.event.wait()
    eventText.append(str(event))
    eventText = eventText[-int(windowSize[1]/font_height):]

    if event.type == QUIT:
        exit()
    screen.fill((255,255,255))

    y = windowSize[1] - font_height
    for text in reversed(eventText):
        screen.blit(font.render(text,True,(0,0,0)),(0,y))
        y -= font_height
    
    pygame.display.update()