from cv2 import *
import numpy as np
pix = int(input('How many pixels do you want? '))
while True:
	frame = np.zeros([pix,pix,3], dtype= np.uint8)
	for i in range(0,10):
		if(i%2 == 0):
			for j in range(0,10):
				a = int((pix/10)*i)
				b = int((pix/10)*(i + 1))
				c = int((pix/10)*j)
				d = int((pix/10)*(j + 1))
				if(j%2 == 0):
					frame[a:b, c:d] = (0,0,255)

		if(i%2 == 1):
			for j in range(0,10):
				a = int((pix/10)*i)
				b = int((pix/10)*(i + 1))
				c = int((pix/10)*j)
				d = int((pix/10)*(j + 1))
				if(j%2 == 1):
					frame[a:b, c:d] = (0,0,255)
	imshow('Checkers', frame)

	if(waitKey(1) & 0xff == ord('q')):
		break