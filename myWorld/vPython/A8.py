from vpython import *
myS = sphere(radius = .5, color = vector(1,1,0))
addR = .01
addG = .015
addB = .02
holdR = 0
holdG = 0
holdB = 0
while True:
    rate(10)
    holdR += addR
    holdG += addG
    holdB += addB
    if(holdR > 1 or holdR < 0):
        addR *= -1
    if(holdG > 1 or holdG < 0):
        addG *= -1
    if(holdB > 1 or holdB < 0):
        addB *= -1

    myS.color = vector(holdR,holdG,holdB)