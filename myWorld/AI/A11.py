from pickletools import uint8
from cv2 import *
from numpy import *

while True:
    color = zeros([255,720,3], dtype= uint8)
    for i in range(0,255):
        for j in range(0,720):
            color[i,j] = [int(j/4),i,255]
    color = cvtColor(color, COLOR_HSV2BGR)
    imshow('HUE', color)
    moveWindow('HUE',0,0)

    color2 = zeros([255,720,3], dtype= uint8)
    for i in range(0,255):
        for j in range(0,720):
            color2[i,j] = [int(j/4),255,i]
    color2 = cvtColor(color2, COLOR_HSV2BGR)
    imshow('HUE2', color2)
    moveWindow('HUE2',0,256)
    if waitKey(0) & 0xff == ord('q'):
        break
