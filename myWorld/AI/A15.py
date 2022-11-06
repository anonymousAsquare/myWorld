from cv2 import *
import numpy as np

def trackBar1(val):
    global Hue1Low
    Hue1Low = val
def trackBar2(val):
    global Hue1High
    Hue1High = val
def trackBar3(val):
    global Hue2Low
    Hue2Low = val
def trackBar4(val):
    global Hue2High
    Hue2High = val
def trackBar5(val):
    global SatLow
    SatLow = val
def trackBar6(val):
    global SatHigh
    SatHigh = val
def trackBar7(val):
    global ValLow
    ValLow = val
def trackBar8(val):
    global ValHigh
    ValHigh = val
x = 0
y = 0
Hue1Low = 0
Hue1High = 0
Hue2Low = 0
Hue2High = 0
SatLow = 0
SatHigh = 0
ValLow = 0
ValHigh = 0

fHeight = 360
fWidth = 640
fps = 30
winName = '@AnonymousAsquare'
trackBars = 'track Bars'

cam = VideoCapture(0, CAP_DSHOW)
cam.set(CAP_PROP_FRAME_WIDTH, fWidth)
cam.set(CAP_PROP_FRAME_HEIGHT, fHeight)
cam.set(CAP_PROP_FPS, 60)
cam.set(CAP_PROP_FOURCC, VideoWriter_fourcc(*'MJPG'))

namedWindow(trackBars)
resizeWindow(trackBars,int(fWidth/2),fHeight)
moveWindow(trackBars,fWidth,0)
createTrackbar('Hue1 low',trackBars,105,180,trackBar1)
createTrackbar('Hue1 High',trackBars,135,180,trackBar2)
createTrackbar('Hue2 low',trackBars,35,180,trackBar3)
createTrackbar('Hue2 High',trackBars,80,180,trackBar4)
createTrackbar('sat low',trackBars,80,255,trackBar5)
createTrackbar('sat High',trackBars,255,255,trackBar6)
createTrackbar('val low',trackBars,0,255,trackBar7)
createTrackbar('val High',trackBars,255,255,trackBar8)
while True:
    ignore, frame = cam.read()
    frameHsv = cvtColor(frame, COLOR_BGR2HSV)
    hsvLow1 = np.array([Hue1Low,SatLow,ValLow])
    hsvHigh1 = np.array([Hue1High,SatHigh,ValHigh])
    hsvLow2 = np.array([Hue2Low,SatLow,ValLow])
    hsvHigh2 = np.array([Hue2High,SatHigh,ValHigh])
    myMask1 =inRange(frameHsv,hsvLow1,hsvHigh1)
    myMask2 =inRange(frameHsv,hsvLow2,hsvHigh2)
    #myMask = myMask1 | myMask2
    myMask = add(myMask1,myMask2)
    contours,junk = findContours(myMask,RETR_EXTERNAL,CHAIN_APPROX_SIMPLE)
    #drawContours(frame,contours,-1,(0,255,0),3)
    for contour in contours:
        area = contourArea(contour)
        if area >= 500:
            #drawContours(frame,[contour],0,(0,255,0),3)
            x,y,w,h = boundingRect(contour)
            rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
    #myMaskSmall = resize(myMask,[int(fWidth/2),int(fHeight/2)])
    ivt = bitwise_and(frame,frame,mask=myMask)
    ivtSmall = resize(ivt,[int(fWidth/2),int(fHeight/2)])
    #imshow('myMask', myMaskSmall)
    #moveWindow('myMask',  int(fWidth/2),fHeight+70)
    imshow('invert', ivtSmall)
    moveWindow('invert',0,fHeight+70)
    imshow(winName, frame)
    moveWindow(winName, x,y)
    if waitKey(1) & 0xff == ord('q'):
        break
cam.release()

