import pygame
from pygame.locals import *
from sys import exit
import time

pygame.init()

window_size = (640,480)
screen = pygame.display.set_mode(window_size,0,32)
logo = pygame.image.load('AsquareeLOGO.png')
pygame.display.set_icon(logo)
pygame.display.set_caption('Asquare Games')

color1 = (221,99,20)
color2 = (96,130,51)
factor = 0.

def blend_color(color1,color2,blend_factor):
    red1,green1,blue1 = color1
    red2,green2,blue2 = color2
    red = red1+(red2-red1)*blend_factor
    green = green1+(green2-green1)*blend_factor
    blue = blue1+(blue2-blue1)*blend_factor
    return red,green,blue


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        if event.type == KEYDOWN:
            if event.key == K_q:
                exit()
    screen.fill((255,255,255))

    tri = [(0,120),(639,100),(639,140)]
    pygame.draw.polygon(screen,(0,255,0),tri)
    pygame.draw.circle(screen,(0,0,0),(int(factor*639),120),10)

    x,y = pygame.mouse.get_pos()
    if pygame.mouse.get_pressed()[0]:
        factor = x/639.
        pygame.display.set_caption("PyGame Color Blend Test - %.3f"%factor)

    color = blend_color(color1,color2,factor)
    pygame.draw.rect(screen,color,(0,240,640,240))
    pygame.display.update()
