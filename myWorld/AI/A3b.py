from cv2 import *
w = 1280/2
h = 720/2

cam = VideoCapture(1, CAP_DSHOW)
cam.set(CAP_PROP_FRAME_WIDTH, w)
cam.set(CAP_PROP_FRAME_HEIGHT, h)
cam.set(CAP_PROP_FPS, 30)
cam.set(CAP_PROP_FOURCC, VideoWriter_fourcc(*'MJPG'))

rows = int(input('How many rows do you want? '))
column = int(input('How input do you want? '))
while True:
    ignore, frame = cam.read() 
    rowSize = int(h/column)
    ColumnSize = int(w/column)
    frame = resize(frame,(ColumnSize, rowSize))
    for i in range(0,rows):
        for j in range(0, column):
            winName = 'window ' + str(i) + ' x ' + str(j)
            imshow(winName, frame)
            moveWindow(winName, (ColumnSize) * j, (rowSize + 30) * i)
    if waitKey(1) & 0xff == ord('q'):
        break
cam.release()