from vpython import *
import numpy as np
import time

clockR = 2
clockL = clockR/15

majorTW = clockR/5
majorTL = clockR/40
majorTD = clockL*1.3

minorTW = clockR/10
minorTL = clockR/45
minorTD = clockL*1.3

secHL = clockR * 0.9
secHW = clockL * 0.3

minHL = clockR * 0.8
minHW = clockL * 0.45

hourHL = clockR * 0.6
hourHW = clockL * 0.6

nubL = clockL*2.5
nubR = clockR/25
for i in np.linspace(0,2*np.pi,13):
    majorT = box(axis = vector(clockR*np.sin(i),clockR*np.cos(i),0), size = vector(majorTW,majorTL,majorTD), pos = vector((clockR-majorTW/2)*np.sin(i),(clockR-majorTW/2)*np.cos(i),0), color = color.black)

for i in np.linspace(0,2*np.pi,61):
    minorT = box(axis = vector(clockR*np.sin(i),clockR*np.cos(i),0), size = vector(minorTW,minorTL,minorTD), pos = vector((clockR-minorTW/2)*np.sin(i),(clockR-minorTW/2)*np.cos(i),0), color = color.black)
myTextH = clockR/4
myClock = cylinder(axis = vector(0,0,1), length = clockL, radius = clockR, color = vector(0,1,0), pos = vector(0,0,-clockL/2))
secH = arrow(axis = vector(0,1,0), length = secHL, shaftwidth =secHW, pos = vector(0,0,clockL+secHW*3.5), color = color.red)
minH = arrow(axis = vector(1,0,0), length = minHL, shaftwidth =minHW, pos = vector(0,0,clockL+minHW*1.5), color = color.red)
hourH = arrow(axis = vector(0,np.pi/2,0), length = hourHL, shaftwidth =hourHW, pos = vector(0,0,clockL), color = color.red)
nub = cylinder(axis = vector(0,0,1), length = nubL, radius = nubR, pos = vector(0,0,0), color = color.black)
mytext = text(text = 'Nigerian Time', align='center',pos = vector(0,clockR*1.1,-clockL/2), height = myTextH, depth = clockL)
labH = clockR/7
lab = text(text = 'A',align='center',pos = vector(0,-labH/2,0),height = labH)
x = 0
for i in np.linspace(0,2*np.pi,13):
    if(x > 0):
        lab = text(text = str(x),align='center',pos=vector((clockR-majorTW-labH/2)*np.sin(i),((clockR-majorTW-labH/2)*np.cos(i))-labH/2,0),height = labH,depth = clockL,color= color.black)
    x += 1
while True:
    rate(10)
    myTime = time.localtime(time.time())
    secc = myTime[5]
    sec = secc*(2*np.pi/60)
    minn = myTime[4] 
    min = minn + (secc/60)
    min = min*(2*np.pi/60)
    hour = myTime[3] + (minn/60)
    hour = hour*(2*np.pi/12)
    secH.axis=vector(secHL*np.sin(sec),secHL*np.cos(sec),0)
    minH.axis=vector(minHL*np.sin(min),minHL*np.cos(min),0)
    hourH.axis=vector(hourHL*np.sin(hour),hourHL*np.cos(hour),0)