from time import *
from threading import Thread

def name():
    while True:
        print('Alainengiya George Junior')
        sleep(3)
def Nname():
    while True:
        print('AnonymousAquare')
        sleep(1)
        print('Astro-Bob')
        sleep(1)
        print('Jungle')
        sleep(1)

myNameThread =Thread(target = name )
myNnameThread = Thread(target = Nname)
myNameThread.daemon = True
myNnameThread.daemon = True
myNameThread.start()
myNnameThread.start()
while True:
    pass 