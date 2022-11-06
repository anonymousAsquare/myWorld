from vpython import *
myS = sphere(radius = .5, color = vector(1,1,0))
addR = .001
addG = -.001
addB = .001
holdR = 1
holdG = 1
holdB = 0
applyR = 0
applyG = 0
applyB = 0
while True:
    rate(100)
    holdR += addR
    holdG += addG
    holdB += addB

    if(holdR <= 1):
        applyR = holdR
    if(holdR > 1):
        applyR = 1

    if(holdG <= 1):
        applyG = holdG
    if(holdG > 1):
        applyG = 1

    if(holdB <= 1):
        applyB = holdB
    if(holdB > 1):
        applyB = 1


    myS.color = vector(applyR,applyG,applyB)

    if(holdR >= 1.5 or holdR <= 0):
        addR *= -1
    if(holdG > 1.5 or holdG < 0):
        addG *= -1
    if(holdB > 1.5 or holdB < 0):
        addB *= -1

    print(applyG + applyB + applyR)