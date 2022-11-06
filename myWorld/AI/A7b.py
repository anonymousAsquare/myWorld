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
POIX = 160
POIY = 90
POIXm = 320
POIYm = 180
addPOIX = 2
addPOIY = 1
while True:
    ignore, frame = cam.read()
    POI = frame[POIYm-int(POIY/2):POIYm+int(POIY/2),POIXm-int(POIX/2):POIXm+int(POIX/2)]
    imshow('Asquare1', POI)
    moveWindow('Asquare1', 650,0)
    grayFrame = cvtColor(frame, COLOR_BGR2GRAY)
    bgrFrame = cvtColor(grayFrame, COLOR_GRAY2BGR)
    bgrFrame[POIYm-int(POIY/2):POIYm+int(POIY/2),POIXm-int(POIX/2):POIXm+int(POIX/2)] = POI
    imshow('Asquare', bgrFrame)
    moveWindow('Asquare', 0,0)
    POIXm += addPOIX
    POIYm += addPOIY
    if (POIXm == width - int(POIX/2) or POIXm == 0 + int(POIX/2)):
        addPOIX *= -1
    if (POIYm == height - int(POIY/2) or POIYm == 0 + int(POIY/2)):
        addPOIY *= -1
    if waitKey(1) & 0xff == ord('q'):
        break
cam.release()