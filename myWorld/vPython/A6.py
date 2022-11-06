from vpython import *
import numpy as np
from threading import Thread
thermoR = .2
thermoH = 2
thermoC = color.white
thermoO = .3
myThermo = sphere(pos = vector(-1,0,0), radius = .5, color = thermoC, opacity = thermoO)
fluidB = sphere(pos = vector(-1,0,0), radius = .45, color = color.magenta, opacity = 1)
myThermo = cylinder(pos = vector(-0.7,0,0), radius = thermoR, length = thermoH, color = thermoC, opacity = thermoO)
fluid = cylinder(pos = vector(-0.7,0,0), radius = .18, length = .1, color = color.magenta, opacity = 1)
for i in np.linspace(-0.7,1.25,20):
    myBox = box(pos=vector(i,0,.2), size = vector(.01,.04,.01), color = color.white,opacity = 1)
    
while True:
    for i in np.linspace(.1,2,100):
        rate(10)
        fluid.length = i

    for i in np.linspace(2,.1,100):
        rate(10)
        fluid.length = i