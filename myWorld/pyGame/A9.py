import pygame
from pygame.locals import *
from sys import exit

pygame.init()
window_size = (800,600)
my_text = ' My Name is Alainengiya George Junior, but you can call me anonymousAsquare '
screen = pygame.display.set_mode(window_size,FULLSCREEN,32)
font = pygame.font.SysFont('arial',16)
my_font = font.render(my_text,True,(0,0,0),(255,255,255))
backgroundImg = pygame.image.load('background.png').convert()

w = backgroundImg.get_width()
x = w
y = (window_size[1]-my_font.get_height())/2
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()

    screen.blit(backgroundImg,(0,0))    
    x -= 0.1
    if x < -my_font.get_width() * 2:
        x = w
    screen.blit(my_font,(x,y))
    screen.blit(my_font,(x+ my_font.get_width(),y))
    pygame.display.update()