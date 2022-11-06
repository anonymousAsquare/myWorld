#INTERACTING WITH THE MOUSE AND CREATING A ROI
from tkinter import EventType
from cv2 import *
w = 640
h = 360
evt = 0
def mouseClick(event,xPos,yPos,flags,params):
    global evt
    global x1
    global y1
    global x2
    global y2
    if event == EVENT_LBUTTONDOWN:
        print('The event is ', event)
        print('The position is ', xPos, ' ', yPos)
        evt = event
        x1 = xPos
        y1 = yPos
    if event == EVENT_LBUTTONUP:
        print('The event is ', event)
        print('The position is ', xPos, ' ', yPos)
        evt = event
        x2 = xPos
        y2 = yPos
    if event == EVENT_RBUTTONUP:
        print('The event is ', event)
        print('The position is ', xPos, ' ', yPos)
        evt = event
cam = VideoCapture(0,CAP_DSHOW)
cam.set(CAP_PROP_FRAME_WIDTH, w)
cam.set(CAP_PROP_FRAME_HEIGHT, h)
cam.set(CAP_PROP_FPS, 30)
cam.set(CAP_PROP_FOURCC, VideoWriter_fourcc(*'MJPG'))
namedWindow('Asquare')
setMouseCallback('Asquare', mouseClick)
while True:
    ignore, frame = cam.read()

        
    if evt == 4:
        circle(frame,(x1,y1),3,(0,255,0),5)
        circle(frame,(x2,y2),3,(0,255,0),5)
        rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
        ROI = frame[y1:y2,x1:x2]
        imshow('ROI', ROI)
        moveWindow('ROI',650,0)

    if evt == 5:
        destroyWindow('ROI')
        evt = 0

    imshow('Asquare', frame)
    moveWindow('Asquare',0,0)
    if waitKey(1) & 0xff == ord('q'):
        break
cam.release()