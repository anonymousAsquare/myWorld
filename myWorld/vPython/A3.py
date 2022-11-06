from vpython import *
from time import *

roomHeight = 25
roomWidth = 25
roomDepth = 30
wallThick = .9
roomColor = color.cyan
marRad = 2
marCol = color.orange

leftWall = box(pos = vector(roomWidth/2,0,0), size = vector(wallThick,roomHeight,roomDepth), color = roomColor)
rightWall = box(pos = vector(-roomWidth/2,0,0), size = vector(wallThick,roomHeight,roomDepth), color = roomColor)
backWall = box(pos = vector(0,0,-roomDepth/2), size = vector(roomWidth,roomHeight,wallThick), color = roomColor)
top = box(pos = vector(0,roomHeight/2,0), size = vector(roomWidth,wallThick,roomDepth), color = roomColor)
rFloor = box(pos = vector(0,-roomHeight/2,0), size = vector(roomWidth,wallThick,roomDepth), color = roomColor)
marble = sphere(radius = marRad, color = marCol)

mXP = 0
mYP = 0
mZP = 0

addX = .1
addY = .2
addZ = .3

while True:
    rate(500)
    mXP = mXP + addX
    mYP = mYP + addY
    mZP = mZP + addZ

    xmPp = mXP + marRad >= ((roomWidth/2) - (wallThick/2))
    xmPn = mXP - marRad <= ((-roomWidth/2) + (wallThick/2))

    YmPp = mYP + marRad >= ((roomHeight/2) - (wallThick/2))
    YmPn = mYP - marRad <= ((-roomHeight/2) + (wallThick/2))

    ZmPp = mZP + marRad >= ((roomHeight/2) - (wallThick/2))
    ZmPn = mZP - marRad <= ((-roomHeight/2) + (wallThick/2))

    if(xmPp or xmPn):
        addX = addX * -1
    
    if(YmPp or YmPn):
        addY = addY * -1

    if(ZmPp or ZmPn):
        addZ = addZ * -1

    marble.pos = vector(mXP,mYP,mZP)
