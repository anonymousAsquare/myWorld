import cv2
import numpy as np
width = 640
height = 360
fps = 30
camera = 0
cam = cv2.VideoCapture(camera,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
winName = '@anonymousAsquare'
while True:
    ignore, frame = cam.read()
    cv2.imshow(winName, frame)
    cv2.moveWindow(winName, 0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()