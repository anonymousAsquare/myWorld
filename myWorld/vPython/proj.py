from numpy import size
from vpython import *
rmdepth = 16.
rmHeight = 12.
rmLength = 16.
wallThick = .6
rmColor = color.white
windowOpacity = .5
xPos = (rmLength/2) 
yPos = (rmHeight/2)
zPos = (rmdepth/2)
lWall_Z_size = rmdepth*0.34
lWall1_Z_Pos = zPos-lWall_Z_size/2
lwall2_Y_size = rmHeight*0.4
lwall2_Y_Pos = -yPos+lwall2_Y_size/2
lwall3_Y_size = rmHeight*0.2
lwall3_Y_Pos = yPos-lwall3_Y_size/2
lWall4_Z_Pos = -zPos+lWall_Z_size/2
bWall1_X_size = rmLength*0.05
bWall1_X_Pos = xPos-bWall1_X_size/2
bWall2_Y_size = rmHeight*0.2
bWall2_Y_Pos = yPos - bWall2_Y_size/2
bWall3_X_size = rmLength*0.65
bWall3_X_Pos = -xPos + bWall3_X_size/2
fWall1_Y_size = rmHeight*0.2
fWall1_Y_Pos = yPos - fWall1_Y_size/2
fWall2_X_size = (rmLength*0.6) + bWall1_X_size
fWall2_X_Pos = -xPos + fWall2_X_size/2
tLWall_Z_size = rmdepth/3
tLWall_X_Pos = -xPos
tLWall_Z_Pos = -zPos - tLWall_Z_size/2
tRWall_Z_size = rmdepth/3
tRWall_X_Pos = xPos
tRWall_Z_Pos = -zPos - tRWall_Z_size/2
tBWall1_X_size = rmLength*0.38
tBWall2_X_size = rmLength*0.38
tBWall3_X_size = rmLength*0.24
tBWall3_Y_size = rmHeight*0.5
tBWall4_X_size = rmLength*0.24
tBWall4_Y_size = rmHeight*0.2
tBWall1_X_Pos = xPos-tBWall1_X_size/2
tBWall2_X_Pos = -xPos+tBWall1_X_size/2
tBWall1_Z_Pos = -zPos-tLWall_Z_size
tBWall2_Z_Pos = -zPos-tLWall_Z_size
tBWall3_Y_Pos = -yPos+tBWall3_Y_size/2
tBWall3_Z_Pos = -zPos-tLWall_Z_size
tBWall4_Y_Pos =  yPos-tBWall4_Y_size/2
tBWall4_Z_Pos = -zPos-tLWall_Z_size

rmFloor = box(pos = vector(0,-yPos,0), size = vector(rmLength,wallThick,rmdepth))
roomRightWall = box(pos = vector(xPos,0,0), size = vector(wallThick,rmHeight+wallThick,rmdepth+wallThick), color = rmColor)
roomLeftWall1 = box(pos = vector(-xPos,0,lWall1_Z_Pos), size = vector(wallThick,rmHeight+wallThick,lWall_Z_size), color = rmColor)
roomLeftWall2 = box(pos = vector(-xPos,lwall2_Y_Pos,0), size = vector(wallThick,lwall2_Y_size+wallThick,lWall_Z_size), color = rmColor)
roomLeftWall3 = box(pos = vector(-xPos,lwall3_Y_Pos,0), size = vector(wallThick,lwall3_Y_size+wallThick,lWall_Z_size), color = rmColor)
roomLeftWall4 = box(pos = vector(-xPos,0,lWall4_Z_Pos), size = vector(wallThick,rmHeight+wallThick,lWall_Z_size), color = rmColor)
bWall1 = box(pos = vector(bWall1_X_Pos,0,-zPos), size = vector(bWall1_X_size,rmHeight,wallThick), color = rmColor)
bWall2 = box(pos = vector(0,bWall2_Y_Pos,-zPos), size = vector(rmLength,bWall2_Y_size,wallThick), color = rmColor)
bWall3 = box(pos = vector(bWall3_X_Pos,0,-zPos), size = vector(bWall3_X_size,rmHeight,wallThick), color = rmColor)
roomFrontWalll = box(pos = vector(0,fWall1_Y_Pos,zPos), size = vector(rmLength+wallThick,fWall1_Y_size+wallThick,wallThick), color = rmColor)
roomFrontWall2 = box(pos = vector(fWall2_X_Pos,0,zPos), size = vector(fWall2_X_size+wallThick,rmHeight+wallThick,wallThick), color = rmColor)
#fWall = box(pos = vector(0,0,zPos), size = vector(rmLength,rmHeight,wallThick), color = rmColor)
ToiletLeftWall = box(pos = vector(tLWall_X_Pos,0,tRWall_Z_Pos), size = vector(wallThick,rmHeight+wallThick,tLWall_Z_size+wallThick))
ToiletRightWall = box(pos = vector(tRWall_X_Pos,0,tRWall_Z_Pos), size = vector(wallThick,rmHeight+wallThick,tRWall_Z_size+wallThick))
tBWall1 = box(pos = vector(tBWall1_X_Pos,0,tBWall1_Z_Pos), size = vector(tBWall1_X_size,rmHeight,wallThick))
tBWall2 = box(pos = vector(tBWall2_X_Pos,0,tBWall2_Z_Pos), size = vector(tBWall2_X_size,rmHeight,wallThick))
tBWall3 = box(pos = vector(0,tBWall3_Y_Pos,tBWall3_Z_Pos), size = vector(tBWall3_X_size,tBWall3_Y_size,wallThick))
tBWall4 = box(pos = vector(0,tBWall4_Y_Pos,tBWall4_Z_Pos), size = vector(tBWall4_X_size,tBWall4_Y_size,wallThick))
tFloor = box(pos = vector(0,-yPos,tLWall_Z_Pos), size = vector(rmLength,0,tRWall_Z_size))
roomWindowFrame1 = box(pos= vector(-xPos,yPos-(rmHeight*0.4),zPos-lWall_Z_size), size = vector(wallThick*0.9,rmHeight*0.4,wallThick), color = color.black)
roomWindowFrame2 = box(pos= vector(-xPos,yPos-(rmHeight*0.4),zPos-lWall_Z_size-(rmdepth*0.32)), size = vector(wallThick*0.9,rmHeight*0.4,wallThick), color = color.black)
roomWindowFrame3 = box(pos= vector(-xPos,yPos-(rmHeight*0.4/2)-wallThick/2,zPos-lWall_Z_size-(rmdepth*0.32/2)), size = vector(wallThick*0.9,wallThick,rmdepth*0.34), color = color.black)
roomWindowFrame4 = box(pos= vector(-xPos,yPos-(rmHeight*0.4*1.5)+wallThick/2,zPos-lWall_Z_size-(rmdepth*0.32/2)), size = vector(wallThick*0.9,wallThick,rmdepth*0.34), color = color.black)
roomWindow = box(pos = vector(-xPos,yPos-(rmHeight*0.4),0), size = vector(wallThick*0.8,rmHeight*0.4,rmdepth*0.34), opacity = windowOpacity)
wallDropLeg = box(pos = vector(0,-yPos+(rmHeight*0.7/2),-zPos+(rmdepth*0.2/2)), size = vector(rmLength*0.06,rmHeight*0.7,rmdepth*0.2))
wallDropTop = box(pos = vector(-xPos+(xPos/2),-yPos+(rmHeight*0.7)-(rmLength*0.06/2),-zPos+(rmdepth*0.2/2)), size = vector(xPos,rmLength*0.06,rmdepth*0.2), color = rmColor)
ToiletWindowFrame1= box(pos = vector(tBWall4_X_size/2,yPos+(rmHeight*0.3/2)-(rmHeight*0.5),tBWall1_Z_Pos), size = vector(wallThick,rmHeight*0.3,wallThick*0.9), color = color.black)
ToiletWindowFrame2= box(pos = vector(-tBWall4_X_size/2,yPos+(rmHeight*0.3/2)-(rmHeight*0.5),tBWall1_Z_Pos), size = vector(wallThick,rmHeight*0.3,wallThick*0.9), color = color.black)
ToiletWindowFrame3= box(pos = vector(0,yPos-tBWall3_Y_size ,tBWall1_Z_Pos), size = vector(tBWall4_X_size,wallThick,wallThick*0.9), color = color.black)
ToiletWindowFrame4= box(pos = vector(0,yPos-tBWall4_Y_size ,tBWall1_Z_Pos), size = vector(tBWall4_X_size,wallThick,wallThick*0.9), color = color.black)
ToiletWindow= box(pos = vector(0,yPos-tBWall4_Y_size-(rmHeight*0.3/2),tBWall1_Z_Pos), size = vector(tBWall4_X_size,rmHeight*0.3,wallThick*0.8), opacity = windowOpacity)
roomDoorFrame1=box(pos = vector(xPos-wallThick/2,-yPos+(rmHeight*0.8/2),zPos), size = vector(wallThick,rmHeight*0.8,wallThick*0.9), color = color.black)
#roomDoorFrame2=box(pos = vector(xPos-(rmLength*0.4/2),-yPos+(rmHeight*0.8/2),zPos), size = vector(wallThick,rmHeight*0.8,wallThick), color = color.black)
roomDoorFrame3=box(pos = vector(xPos-(rmLength*0.4/2),yPos-(rmHeight*0.2)-wallThick/2,zPos), size = vector(rmLength*0.4,wallThick,wallThick*0.9), color = color.black)
roomDoorFrame4=box(pos = vector(xPos-(rmLength*0.4/2),-yPos+wallThick/4,zPos), size = vector(rmLength*0.4,wallThick,wallThick*0.9), color = color.black)
toiletDoorFrame1= box(pos = vector(0,0,0), size = vector(0,0,0), color = color.black)
while True:
    pass