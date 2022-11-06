import pygame
from pygame.locals import *
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,600),0,32)
all_colors = pygame.Surface((4096,4096), depth= 24)

for r in range(256):
    print(r + 1)
    x = (r & 15)*256
    y = (r >> 4)*256
    for g in range(256):
        for b in range(256):
            all_colors.set_at((x+g,y+b), (r,g,b))
pygame.image.save(all_colors,'allcolors.png')
"""pygame.display.set_caption('Asquare Games')
logo = pygame.image.load('AsquareeLOGO.png')
pygame.display.set_icon(logo)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()
    
    pygame.display.update()"""
