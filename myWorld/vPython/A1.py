from vpython import *
from time import *
myBox = box(pos = vector(3.5,0,0), size = vector(.1,7,7), color = color.white)
myBox = box(pos = vector(-3.5,0,0), size = vector(.1,7,7), color = color.white)
myBox = box(pos = vector(0,0,-3.5), size = vector(7,7,.1), color = color.white)
myBox = box(pos = vector(0,-3.5,0), size = vector(7,.1,7), color = color.white)
myBox = box(pos = vector(0,3.5,0), size = vector(7,.1,7), color = color.white)
marble = sphere(radius = .2, color = color.red)
bucket = 0
add = .1
while True:
    rate(10)
    bucket = bucket + add
    if (bucket > 3.35 or bucket < -3.31):
        add = add * -1
    marble.pos = vector(bucket,0,0)