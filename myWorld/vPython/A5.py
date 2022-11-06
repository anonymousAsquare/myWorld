from vpython import *
import numpy as np
from time import *

thermoTh = 3
thermoD = 2
thermoW = 50
thermoH = 6
thermoC = color.white
thermoO = .8
myThermoL = box(pos = vector(thermoW/2,0,0), size = vector(thermoTh,thermoH,thermoD), color = thermoC, opacity = thermoO)
myThermoR = box(pos = vector(-thermoW/2,0,0), size = vector(thermoTh,thermoH,thermoD), color = thermoC, opacity = thermoO)
myThermoT = box(pos = vector(0,thermoH/2,0), size = vector(thermoW,thermoTh,thermoD), color = thermoC, opacity = thermoO)
myThermoT = box(pos = vector(0,-thermoH/2,0), size = vector(thermoW,thermoTh,thermoD), color = thermoC, opacity = thermoO)
myThermoT = box(pos = vector(0,0,-thermoD/2), size = vector(thermoW,thermoH,thermoTh), color = thermoC, opacity = thermoO)
fluid = cylinder(pos = vector(-thermoW/2,0,0), radius = 2, height = 1.5, color = color.magenta, opacity = 1)
for i in np.linspace(-25,25,50):
    myBox1= box(pos=vector(i,3,1), size = vector(.1,.4,.1), color = color.black,opacity = 1)

for i in np.linspace(-25,25,50):
    myBox1= box(pos=vector(i,-3,1), size = vector(.1,.4,.1), color = color.black,opacity = 1)

while True:
    for i in np.linspace(1.5,48.5,100):
        rate(2)
        fluid.length = i

    for i in np.linspace(48.5,1.5,100):
        rate(2)
        fluid.length = i

