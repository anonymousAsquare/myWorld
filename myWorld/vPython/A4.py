from vpython import *
import numpy as np
from time import *
from threading import Thread

mySphere = sphere(radius = .1, color = color.magenta, opacity = .1)

def mySphereR():
    while True:
        for i in np.linspace(.1,1,10):
            rate(2)
            mySphere.radius = i

        for i in np.linspace(1,.1,10):
            rate(2)
            mySphere.radius = i

def mySphereO():
    while True:
        for i in np.linspace(.1,1,10):
            rate(2)
            mySphere.opacity = i

        for i in np.linspace(1,.1,10):
            rate(2)
            mySphere.opacity = i

T1 = Thread(target = mySphereR)
T2 = Thread(target = mySphereO)
T1.daemon = True
T2.daemon = True
T1.start()
T2.start()
while True:
    pass