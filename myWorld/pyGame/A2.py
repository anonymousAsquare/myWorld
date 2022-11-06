import pygame
from pygame.locals import *
from sys import exit

pygame.init()
backgroungImg = 'background.png'
mouseImg = 'player.png'
screen = pygame.display.set_mode((800,600),0,32)
pygame.display.set_caption('Hello World')

background = pygame.image.load(backgroungImg).convert()
mouse_cusur = pygame.image.load(mouseImg).convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    
    screen.blit(background,(0,0))
    x,y = pygame.mouse.get_pos()
    x -= mouse_cusur.get_width()/2
    y -= mouse_cusur.get_height()/2
    print(x,y)
    screen.blit(mouse_cusur,(x,y))
    pygame.display.update()