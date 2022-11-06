from turtle import width
from cv2 import *
inc = 0
incPx = 0
incPy = 0
def trackBar1(val):
    global inc
    inc = val
def trackBar2(val):
    global incPx
    incPx = val
def trackBar3(val):
    global incPy
    incPy = val
w = 160
h = 90
width = 1280
height = 720
fps = 30
cam = VideoCapture(0, CAP_DSHOW)
cam.set(CAP_PROP_FRAME_WIDTH, width)
cam.set(CAP_PROP_FRAME_HEIGHT, height)
cam.set(CAP_PROP_FPS, fps)
cam.set(CAP_PROP_FOURCC, VideoWriter_fourcc(*'MJPG'))
namedWindow('AsquareCam... Trackbar')
moveWindow('AsquareCam... Trackbar',w,0)
resizeWindow('AsquareCam... Trackbar',300,130)
createTrackbar('winSize', 'AsquareCam... Trackbar',0,7, trackBar1)
createTrackbar('winPosX', 'AsquareCam... Trackbar',0,1175, trackBar2)
createTrackbar('winPosY', 'AsquareCam... Trackbar',0,650, trackBar3)
while True:
    ignore, frame = cam.read()
    y = h*(inc+1)
    x = w*(inc + 1)
    if(incPx+x < 1400 and incPy+y < 725):
        a = x
        b = y
    rame = resize(frame,(a, b))
    imshow('AsquareCam',rame)
    #if(incPx+x < 1350 and incPy+y < 725):
        #moveWindow('AsquareCam',incPx,incPy)
    if(incPx+x < 1350):
        c = incPx
    if(incPy+y < 725):
        d = incPy
    moveWindow('AsquareCam',c,d)
    if(waitKey(1) & 0xff == ord('q')):
        break
cam.release()