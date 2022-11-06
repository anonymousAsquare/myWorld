from cv2 import *
cam1 = VideoCapture(0)
while True:
    ignore, frame1 = cam1.read()
    gFarme = cvtColor(frame1,COLOR_RGB2GRAY)
    imshow('cam1', frame1)
    moveWindow('cam1',0,0)
    imshow('cam2', gFarme)
    moveWindow('cam2',640,0)
    imshow('cam3', gFarme)
    moveWindow('cam3',0,320)
    imshow('cam4', frame1)
    moveWindow('cam4',640,320)
    if waitKey(1) & 0xff == ord('q'):
        break
cam1.release()