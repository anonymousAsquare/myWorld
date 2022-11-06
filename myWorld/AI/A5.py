#ADDING RECTANGLE, CIRCLE AND TEXT TO THE FRAME/IMAGE
from turtle import width
from cv2 import *
myText = '@Asquare'
width = 640
height = 360
framePerSec = 30
camera = 0
moveWinX = 360
moveWindY = 0
myFont = FONT_HERSHEY_COMPLEX_SMALL
textPos = (30,60)
textColor = (255,0,0)
textSize = 2
textOpacity = 1
circlePos = (320,180)
circleRadius = 25
circleColor = (0,0,255)
circleOpacity = -1
rectangleX1Y1 = (280,140)
rectangleX2Y2 = (360,220)
rectangleColor = (0,255,0)
rectangleOpacity = 3
cam = VideoCapture(camera, CAP_DSHOW)
cam.set(CAP_PROP_FRAME_WIDTH, width)
cam.set(CAP_PROP_FRAME_HEIGHT, height)
cam.set(CAP_PROP_FPS, framePerSec)
cam.set(CAP_PROP_FOURCC, VideoWriter_fourcc(*'MJPG'))
while True:
    ignore, frame = cam.read()
    #frame[140:220,280:360] = (0,0,0)
    rectangle(frame,rectangleX1Y1,rectangleX2Y2,rectangleColor,rectangleOpacity)
    circle(frame,circlePos,circleRadius,circleColor, circleOpacity)
    putText(frame,myText,textPos,myFont,textSize,textColor,textOpacity)
    imshow('Asquare', frame)
    moveWindow('Asquare', moveWinX,moveWindY)
    if waitKey(1) & 0xff == ord('q'):
        break
cam.release()