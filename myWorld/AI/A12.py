from cv2 import *
import numpy as np 
def trackBar1(val):
    global hueLow
    hueLow = val
    print('Hue Low', hueLow)
def trackBar2(val):
    global hueHigh
    hueHigh = val
    print('Hue High', hueHigh)
def trackBar3(val):
    global satLow
    satLow = val
    print('Sat Low', satLow)
def trackBar4(val):
    global satHigh
    satHigh = val
    print('Sat High', satHigh)
def trackBar5(val):
    global valLow
    valLow = val
    print('Val Low', valLow)
def trackBar6(val):
    global valHigh
    valHigh = val
    print('Val High', valHigh)

hueLow = 0
hueHigh = 20
satLow = 0
satHigh = 255
valLow = 0
valHigh = 255
Cam = 0
windowWidth = 640
windowHeight = 360
fps = 30
mainWindowName = 'Asquare'
cam = VideoCapture(Cam, CAP_DSHOW)
cam.set(CAP_PROP_FRAME_WIDTH, windowWidth)
cam.set(CAP_PROP_FRAME_HEIGHT, windowHeight)
cam.set(CAP_PROP_FPS, fps)
cam.set(CAP_PROP_FOURCC, VideoWriter_fourcc(*'MJPG'))
namedWindow('Track bar')
moveWindow('Track bar',windowWidth,0)
createTrackbar('Hue Low','Track bar',0,180,trackBar1)
createTrackbar('Hue High','Track bar',180,180,trackBar2)
createTrackbar('Sat Low','Track bar',0,255,trackBar3)
createTrackbar('Sat High','Track bar',255,255,trackBar4)
createTrackbar('Val Low','Track bar',0,255,trackBar5)
createTrackbar('Val High','Track bar',255,255,trackBar6)
while True:
    ignore, frame = cam.read()
    frameHsv = cvtColor(frame,COLOR_BGR2HSV)
    hsvHigh = np.array([hueHigh,satHigh,valHigh])
    hsvLow = np.array([hueLow,satLow,valLow])
    myMask = inRange(frameHsv,hsvLow,hsvHigh)
    #myMask = bitwise_not(myMask)
    myMaskSmall = resize(myMask,[320,180])
    img = bitwise_and(frame,frame,mask=myMask)
    imgSmall = resize(img,(int(windowWidth/2),int(windowHeight/2)))
    imshow('Img',imgSmall)
    moveWindow('Img',int(windowWidth/2),windowHeight)
    imshow('my mask small', myMaskSmall)
    moveWindow('my mask small', 0, windowHeight )
    imshow(mainWindowName, frame)
    moveWindow(mainWindowName, 0,0)
    #frameHsvSmall = resize(frameHsv,(int(windowWidth/2),int(windowHeight/2)))
    #imshow('frame Hsv', frameHsvSmall)
    #moveWindow('frame Hsv', windowWidth,windowHeight+70)
    if (waitKey(1) & 0xff == ord('q')):
        break
cam.release()