from vpython import *
import numpy as np

thermo1 = cylinder(radius = .2, color= color.white,opacity = .3, length = 1)
thermo1d = sphere(pos = vector(-.2,0,0), radius = .4,color = color.white, opacity = .3)
fluid1 = cylinder(radius = .17, color= color.magenta, length = .9)
fluid1d = sphere(pos = vector(-.2,0,0), radius = .37,color = color.magenta)
for i in np.linspace(.1,.97,15):
    myBox1= box(pos=vector(i,0,.2), size = vector(.01,.04,.01), color = color.white,opacity = 1)

thermo2 = cylinder(radius = .2, color= color.white,opacity = .3, length = 1,pos = vector(0,1,0))
thermo2d = sphere(pos = vector(-.2,1,0), radius = .4,color = color.white, opacity = .3)
fluid2 = cylinder(radius = .17, color= color.magenta, length = .9, pos = vector(0,1,0))
fluid2d = sphere(pos = vector(-.2,1,0), radius = .37,color = color.magenta)
for i in np.linspace(.1,.97,15):
    myBox2= box(pos=vector(i,1,.2), size = vector(.01,.04,.01), color = color.black,opacity = 1 )

fluid1Add = .01
fluid2Add = .02
fluid1Pos = .2
fluid2Pos = .2

while True:
    rate(30)
    fluid1Pos = fluid1Pos + fluid1Add
    fluid2Pos = fluid2Pos + fluid2Add
    fluid1.length = fluid1Pos
    fluid2.length = fluid2Pos
    if(fluid1Pos <= .15 or fluid1Pos >= .99):
        fluid1Add = fluid1Add * -1
    if(fluid2Pos <= .15 or fluid2Pos >= .99):
        fluid2Add = fluid2Add * -1