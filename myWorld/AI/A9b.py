
from cv2 import *
def trackBar(val):
    width = val
    height = val * 9/16
    print(height)
    cam.set(CAP_PROP_FRAME_WIDTH, width)
    cam.set(CAP_PROP_FRAME_HEIGHT, height)
w = 1280
h = 720
cam = VideoCapture(0,CAP_DSHOW)
cam.set(CAP_PROP_FRAME_WIDTH, w)
cam.set(CAP_PROP_FRAME_HEIGHT, h)
cam.set(CAP_PROP_FPS, 30)
cam.set(CAP_PROP_FOURCC, VideoWriter_fourcc(*'MJPG'))
namedWindow('TrackBar')
resizeWindow('TrackBar',400,150)
moveWindow('TrackBar',1280,0)
createTrackbar('resize','TrackBar',1280,1280,trackBar)
while True:
    ignore, frame = cam.read()
    imshow('Asquare', frame)
    moveWindow('Asquare',0,0)
    if waitKey(1) & 0xff == ord('q'):
        break
cam.release()