import pygame
from pygame.locals import *
from sys import exit

screen_size = (800,600)
pygame.init()
screen = pygame.display.set_mode(screen_size,0,32)
obj = pygame.image.load('player.png')

clock = pygame.time.Clock()
x1 = 0
x2 = 0

speed = 250

frame_no = 0
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()
    
    screen.fill((0,0,0))
    screen.blit(obj,(x1,50))
    screen.blit(obj,(x2,250))

    time_passed = clock.tick(30)
    time_passed_seconds = time_passed/1000.

    distance = time_passed_seconds * speed
    x1 += distance

    if (frame_no % 5) == 0:
        distance = time_passed_seconds * speed
        x2 += distance * 5

    if x1 > 800.:
        x1 -= 800
    if x2 > 800:
        x2 -= 800

    pygame.display.update()
    frame_no += 1