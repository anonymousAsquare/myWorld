from vpython import *
from time import *

wallThick = .5
wallHeight = 10
wallDepth = 20
wallWidth = 15
paint = color.white
mRadius = .5

leftWall = box(pos = vector(wallWidth/2,0,0), size = vector(wallThick,wallHeight,wallDepth), color = paint)
rightWall = box(pos = vector(-wallWidth/2,0,0), size = vector(wallThick,wallHeight,wallDepth), color = paint)
top = box(pos = vector(0,wallHeight/2,0), size = vector(wallWidth,wallThick,wallDepth), color = paint)
buttonW = box(pos = vector(0,-wallHeight/2,0), size = vector(wallWidth,wallThick,wallDepth), color = paint)
backWall = box(pos = vector(0,0,-wallDepth/2), size = vector(wallWidth,wallHeight,wallThick), color = paint)
marble = sphere(radius = mRadius, color = color.red)

marXPos = 0
add = .1
while True:
    rate(10)
    marXPos = marXPos + add
    xW = (marXPos + mRadius >= (wallWidth/2 - wallThick/2))
    nXW = (marXPos - mRadius <= (-wallWidth/2 + wallThick/2)) 
    if (xW or nXW):
        add = add * -1
    marble.pos = vector(marXPos,0,0)