from unittest import runner

import pygame

pygame.init()
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('@aA^2 Games')
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)
playerimg = pygame.image.load('alien.png')
playerX = 100
playerY = 40
def player():
    screen.blit(playerimg,(playerX,playerY))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((0,255,0))
    player()
    pygame.display.update()
