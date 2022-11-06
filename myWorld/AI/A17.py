from cv2 import *
import time
iw = 640
ih = 360
cam = VideoCapture(0,CAP_DSHOW)
cam.set(CAP_PROP_FRAME_WIDTH, iw)
cam.set(CAP_PROP_FRAME_HEIGHT, ih)
cam.set(CAP_PROP_FPS, 30)
cam.set(CAP_PROP_FOURCC, VideoWriter_fourcc(*'MJPG'))
faceCascade = CascadeClassifier('haar/haarcascade_frontalface_default.xml')
delayT = time.time()
fps = 30
time.sleep(.1)
while True:
    sec = time.time()-delayT
    Fps = 1/sec
    fps = fps*.9 + Fps * .1
    delayT= time.time()
    ignore, frame = cam.read()
    rectangle(frame,(0,0),(120,50), (0,0,0), -1)
    putText(frame,str(int(fps)) + 'fps',(0,35),FONT_HERSHEY_COMPLEX,1,(125,125,0),2)
    gFrame = cvtColor(frame,COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gFrame)
    print(faces)
    for face in faces:
        x,y,w,h = face
        rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
        putText(frame,"Human",(x+10,y-10),FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
    imshow('Asquare', frame)
    moveWindow('Asquare',0,0)
    if waitKey(1) & 0xff == ord('q'):
        break
cam.release()