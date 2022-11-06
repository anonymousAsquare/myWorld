#CREATING A ROI 
from turtle import width
from cv2 import *
width = 640
height = 360
camera = 0
fps = 30
cam = VideoCapture(camera, CAP_DSHOW)
cam.set(CAP_PROP_FRAME_WIDTH, width)
cam.set(CAP_PROP_FRAME_HEIGHT, height)
cam.set(CAP_PROP_FPS, fps)
cam.set(CAP_PROP_FOURCC, VideoWriter_fourcc(*'MJPG'))
movePOIX1 = 0
movePOIY1 = 0
movePOIX2 = 160
movePOIY2 = 90
addPOIX = 2
addPOIY = 1
while True:
    ignore, frame = cam.read()
    POI = frame[movePOIY1:movePOIY2,movePOIX1:movePOIX2]
    imshow('Asquare1', POI)
    moveWindow('Asquare1', 650,0)
    grayFrame = cvtColor(frame, COLOR_BGR2GRAY)
    bgrFrame = cvtColor(grayFrame, COLOR_GRAY2BGR)
    bgrFrame[movePOIY1:movePOIY2,movePOIX1:movePOIX2] = POI
    imshow('Asquare', bgrFrame)
    moveWindow('Asquare', 0,0)
    movePOIX1 += addPOIX
    movePOIX2 += addPOIX
    movePOIY1 += addPOIY
    movePOIY2 += addPOIY
    if (movePOIX2 == width or movePOIX1 == 0 ):
        addPOIX *= -1
    if (movePOIY2 == height or movePOIY1 == 0):
        addPOIY *= -1
    if waitKey(1) & 0xff == ord('q'):
        break
cam.release()