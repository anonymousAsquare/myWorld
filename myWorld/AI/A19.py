from cv2 import *
import time
iw = 640
ih = 360
cam = VideoCapture(0,CAP_DSHOW)
cam.set(CAP_PROP_FRAME_WIDTH, iw)
cam.set(CAP_PROP_FRAME_HEIGHT, ih)
cam.set(CAP_PROP_FPS, 60)
cam.set(CAP_PROP_FOURCC, VideoWriter_fourcc(*'MJPG'))
faceCascade = CascadeClassifier('haar/haarcascade_frontalface_alt.xml')
eyeCascade = CascadeClassifier('haar/haarcascade_eye.xml')
delayT = time.time()
fps = 60
time.sleep(.1)
while True:
    sec = time.time()-delayT
    Fps = 1/sec
    fps = fps*.97 + Fps * .03
    delayT= time.time()
    ignore, frame = cam.read()
    rectangle(frame,(0,0),(100,50), (0,0,0), -1)
    putText(frame,str(int(fps)) + 'fps',(0,35),FONT_HERSHEY_COMPLEX,1,(255,255,255),1)
    #putText(frame,'@anonymousAsquare',(0,200),FONT_HERSHEY_COMPLEX,1,(0,0,0),1)
    gFrame = cvtColor(frame,COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gFrame)
    for face in faces:
        fx,fy,fw,fh = face
        rectangle(frame,(fx,fy),(fx+fw,fy+fh),(0,255,0),3)
        putText(frame,"Human",(fx+10,fy-10),FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        faceFrame = frame[fy:fy+fh,fx:fx+fw]
        gFaceFrame = cvtColor(faceFrame,COLOR_BGR2GRAY)
        eyes = eyeCascade.detectMultiScale(gFaceFrame)
        for eye in eyes:
            ex,ey,ew,eh = eye
            rectangle(frame[fy:fy+fh,fx:fx+fw],(ex,ey),(ex+ew,ey+eh),(0,255,0),3)

    imshow('Asquare', frame)
    moveWindow('Asquare',0,0)
    if waitKey(1) & 0xff == ord('q'):
        break
cam.release()