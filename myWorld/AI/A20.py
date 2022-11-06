import cv2
camera = 1
frameWidth = 640
frameHeight = 360
fps = 30
cam = cv2.VideoCapture(camera, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, frameWidth)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, frameHeight)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
frameWindowName = 'Asquare'
faceCascade = cv2.CascadeClassifier('haar/haarcascade_frontalface_default.xml')
while True:
    ignore, frame = cam.read()
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(grayFrame)
    for face in faces:
        x,y,w,h = face
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),1,)
    cv2.imshow(frameWindowName, frame)
    cv2.moveWindow(frameWindowName,0,0)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
cam.release()