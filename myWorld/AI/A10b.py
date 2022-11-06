from pickletools import uint8
from cv2 import *
from numpy import *
w = 640
h = 360
evt = 0
x = 0
y = 0
def mouseClick(event,xPos,yPos,flags,params):
    global x 
    global y
    global evt
    if event == EVENT_LBUTTONDOWN:
        x = xPos
        y = yPos
        evt = event
    if event == EVENT_RBUTTONUP:
        x = xPos
        y = yPos
cam = VideoCapture(0,CAP_DSHOW)
cam.set(CAP_PROP_FRAME_WIDTH, w)
cam.set(CAP_PROP_FRAME_HEIGHT, h)
cam.set(CAP_PROP_FPS, 30)
cam.set(CAP_PROP_FOURCC, VideoWriter_fourcc(*'MJPG'))
namedWindow('Asquare')
setMouseCallback('Asquare',mouseClick)
while True:
    ignore, frame = cam.read()
    if evt ==1:
        small = zeros([200,200,3], dtype = uint8)
        cvt = cvtColor(frame, COLOR_BGR2HSV)
        POI = cvt[y][x]
        small[:,:] = POI
        putText(small,str(POI),(0,40),FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),1)
        imshow('small', small)
        moveWindow('small', w,0)
        evt = 0
    imshow('Asquare', frame)
    moveWindow('Asquare',0,0)
    if waitKey(1) & 0xff == ord('q'):
        break
cam.release()