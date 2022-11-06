import pygame
from pygame.locals import *
from sys import exit

screen_size = (800,600)
pygame.init()
screen = pygame.display.set_mode(screen_size,0,32)
obj = pygame.image.load('player.png')

clock = pygame.time.Clock()
x = 0
speed = 250
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()
    
    screen.fill((0,0,0))
    screen.blit(obj,(x,100))

    time_passed = clock.tick()
    time_passed_seconds = time_passed/1000.

    distance = time_passed_seconds * speed
    x += distance
    if x > 800.:
        x -= 800
    pygame.display.update()