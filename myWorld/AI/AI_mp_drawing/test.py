import cv2

window_width = 640
window_height = 480
fps = 30

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, window_width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, window_height)
cam.set(cv2.CAP_PROP_FPS, fps)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    __, frame = cam.read()
    cv2.line(frame,(10,10), (20,30),(0,255,0),2,)
    cv2.imshow('Test', frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break