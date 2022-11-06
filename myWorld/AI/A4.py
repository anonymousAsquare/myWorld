from cv2 import *
import numpy as np
div = 0
y =1
while (y > 0):
    chec = input('What kind of checkers board do you want?\n A.10 X 10 \n B.8 X 8 \n')
    if(chec == 'A' or chec == 'a'):
        div = 10
        break
    if(chec == 'B' or chec == 'b'):
        div = 8
        break
    if(chec != 'A' or chec == 'a' or chec != 'B' or chec == 'b'):
        print("Error, Please select either 'A' or 'B' ")

pix = int(input('How many pixels do you want? '))

while True:
	frame = np.zeros([pix,pix,3], dtype= np.uint8)
	for i in range(0,div):
		if(i%2 == 0):
			for j in range(0,div):
				a = int((pix/div)*i)
				b = int((pix/div)*(i + 1))
				c = int((pix/div)*j)
				d = int((pix/div)*(j + 1))
				if(j%2 == 0):
					frame[a:b, c:d] = (0,0,255)

		if(i%2 == 1):
			for j in range(0,div):
				a = int((pix/div)*i)
				b = int((pix/div)*(i + 1))
				c = int((pix/div)*j)
				d = int((pix/div)*(j + 1))
				if(j%2 == 1):
					frame[a:b, c:d] = (0,0,255)
	imshow('Checkers', frame)

	if(waitKey(1) & 0xff == ord('q')):
		break