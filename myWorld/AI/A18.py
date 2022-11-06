from cv2 import *
iw = 640
ih = 360
cam = VideoCapture(1,CAP_DSHOW)
cam.set(CAP_PROP_FRAME_WIDTH, iw)
cam.set(CAP_PROP_FRAME_HEIGHT, ih)
cam.set(CAP_PROP_FPS, 30)
cam.set(CAP_PROP_FOURCC, VideoWriter_fourcc(*'MJPG'))
eyeCascade = CascadeClassifier('haar/haarcascade_eye.xml')
while True:
    ignore, frame = cam.read()
    gFrame = cvtColor(frame,COLOR_BGR2GRAY)
    eyes=eyeCascade.detectMultiScale(gFrame,1.3,5)
    for eye in eyes:
        x,y,w,h = eye
        rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    print(eyes)
    imshow('Asquare', frame)
    moveWindow('Asquare',0,0)
    if waitKey(1) & 0xff == ord('q'):
        break
cam.release()