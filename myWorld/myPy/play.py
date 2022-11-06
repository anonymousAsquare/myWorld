from vpython import *
from numpy import *
x = 0
l = 2
o = 2.1
sClockL = 2
mClockL = 1.7
hClockL = 1.2
mySphere = sphere(radius = .1, pos = vector(0,0,0),color = vector(0,0,0))

for i in linspace(0,2*pi,61):
    if(x == 0 or x == 30 or x == 15 or x == 45 or x == 5 or x == 10 or x == 20 or x == 25 or x == 35 or x == 40 or x == 50 or x == 55):
        myBox = box(axis = vector(l*sin(i),l*cos(i),0),pos = vector(l*sin(i),l*cos(i),0), size = vector(.4,.1,0), color = vector(0,0,0))
    else:
        myBox = box(axis = vector(o*sin(i),o*cos(i),0),pos = vector(o*sin(i),o*cos(i),0), size = vector(.2,.01,0), color = vector(0,0,0))
    x += 1
sClock = arrow(axis = vector(sClockL*sin(2*pi),sClockL*cos(2*pi),0), shaftwidth = .03, length = sClockL, color = color.red)  
mClock = arrow(axis = vector(mClockL*sin(2*pi),mClockL*cos(2*pi),0), shaftwidth = .04, lenght = mClockL, color = color.green)
hClock = arrow(axis = vector(hClockL*cos(2*pi),hClockL*sin(2*pi),0), shaftwidth = .06, lenght = hClockL, color = color.blue)
Clock1= cylinder(radius = 2.5, lenght = .01, axis = vector(cos(pi/2),0,sin(3*pi/2)), pos = vector(0,0,-.2), color = vector(0,.5,0))
Clock= cylinder(radius = 2.3, lenght = .01, axis = vector(cos(pi/2),0,sin(3*pi/2)), pos = vector(0,0,-.1), color = vector(1,1,1))
#Clock3= cylinder(radius = 1.7, lenght = .01, axis = vector(cos(pi/2),0,sin(3*pi/2)), pos = vector(0,0,-.1), color = vector(.5,.5,.5), opacity = .5) 

while True:
    for k in linspace(0,2*pi,12):
        for j in linspace(0,2*pi,61):
            for i in linspace(0,2*pi,61):
                rate(1)
                sClock.axis = vector(sClockL*sin(i),sClockL*cos(i),0)
            mClock.axis = vector(mClockL*sin(j),mClockL*cos(j),0)
        hClock.axis = vector(mClockL*sin(k),mClockL*cos(k),0)