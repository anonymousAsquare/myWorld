#CALCULATING THE FRAMES PER SECOND AND DISPLAYING IT TO THE USER
from turtle import width
from cv2 import *
from time import *
camera = 0
width = 640
height = 360
framePerSec = 30
cam = VideoCapture(camera, CAP_DSHOW)
cam.set(CAP_PROP_FRAME_WIDTH, width)
cam.set(CAP_PROP_FRAME_HEIGHT, height)
cam.set(CAP_PROP_FPS, framePerSec)
cam.set(CAP_PROP_FOURCC, VideoWriter_fourcc(*'MJPG'))
lastTime = time()
fpsFill = 30
sleep(.1)
while True:
    dT = time() - lastTime
    fps = 1/dT
    print(fps)
    fpsFill = fpsFill * .97 + fps * .03
    lastTime = time()
    ignore, frame = cam.read()
    rectangle(frame,(0,0),(120,50), (0,255,0), -1)
    putText(frame,str(int(fpsFill))+' fps',(0,35),FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
    rectangle(frame,(250,50),(410,90), (0,125,125), -1)
    putText(frame,'@Asquare',(250,80),FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    imshow('Asquare', frame)
    if (waitKey(1) & 0xff == ord('q')):
        break
cam.release()