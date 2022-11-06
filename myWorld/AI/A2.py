import cv2
from cv2 import COLOR_RGB2GRAY
cam1 = cv2.VideoCapture(0)
while True:
    ignore, frame1 = cam1.read()
    gFarme = cv2.cvtColor(frame1,COLOR_RGB2GRAY)
    cv2.imshow('cam1', frame1)
    cv2.moveWindow('cam1',0,0)
    cv2.imshow('cam2', gFarme)
    cv2.moveWindow('cam2',640,0)
    cv2.imshow('cam3', gFarme)
    cv2.moveWindow('cam3',0,320)
    cv2.imshow('cam4', frame1)
    cv2.moveWindow('cam4',640,320)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam1.release()