from vpython import *
from numpy import *
arrowLength = 2
arrowThick = .02
ballRadius = .05
XarrowColor = vector(255,0,0)
YarrowColor = vector(0,255,0)
ZarrowColor = vector(0,0,255)
Xarrow = arrow(lenght = arrowLength, shaftwidth = arrowThick, color = XarrowColor)
Yarrow = arrow(axis = vector(0,1,0),lenght = arrowLength, shaftwidth = arrowThick, color = YarrowColor)
Zarrow = arrow(axis = vector(0,0,1),lenght = arrowLength, shaftwidth = arrowThick, color = ZarrowColor)
Marrow = arrow(axis = vector(0,0,0),lenght = arrowLength, shaftwidth = arrowThick)
myBall = sphere(radius = ballRadius, make_trail = True)
#Marrow.axis = vector(sin(pi/4),cos(pi/4),0)
#Marrow.lenght = 2
wait = 50
while True:

    

    for i in linspace(pi*2,pi/2,750):
        rate(wait)
        Marrow.axis = vector(cos(i),sin(i),0) 
        Marrow.color = XarrowColor
        myBall.color = XarrowColor
        myBall.pos =  vector(cos(i),sin(i),0)
        myBall.trail_color = XarrowColor
        #Marrow.length = 2

    for i in linspace(pi*2,pi/2,750):
        rate(wait)
        Marrow.axis = vector(0,cos(i),sin(i)) 
        Marrow.color = YarrowColor
        myBall.color = YarrowColor
        myBall.pos =  vector(0,cos(i),sin(i)) 
        myBall.trail_color = YarrowColor
        #Marrow.length = 2

    for i in linspace(pi*2,pi/2,750):
        rate(wait)
        Marrow.axis = vector(sin(i),0,cos(i)) 
        Marrow.color = ZarrowColor
        myBall.color = ZarrowColor
        myBall.pos =  vector(sin(i),0,cos(i))  
        myBall.trail_color = ZarrowColor
        #Marrow.length = 2
    
    for i in linspace(0,pi/2,250):
        rate(wait)
        Marrow.axis = vector(cos(i),sin(i),0) 
        Marrow.color = XarrowColor
        myBall.color = XarrowColor
        myBall.pos =  vector(cos(i),sin(i),0)
        myBall.trail_color = XarrowColor
        
        #Marrow.length = 2

    for i in linspace(0,pi/2,250):
        rate(wait)
        Marrow.axis = vector(0,cos(i),sin(i)) 
        Marrow.color = YarrowColor
        myBall.color = YarrowColor
        myBall.pos =  vector(0,cos(i),sin(i)) 
        myBall.trail_color = YarrowColor
        #Marrow.length = 2
    
    for i in linspace(0,pi/2,250):
        rate(wait)
        Marrow.axis = vector(sin(i),0,cos(i)) 
        Marrow.color = ZarrowColor
        myBall.color = YarrowColor
        myBall.pos =  vector(sin(i),0,cos(i))
        myBall.trail_color = ZarrowColor
        #Marrow.length = 2