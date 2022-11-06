class vector2():
    def __init__(self,p1,p2):
        self.x = p2[0]-p1[0]
        self.y = p2[1]-p1[1]
        
    def __str__(self):
        return "({},{})".format(self.x,self.y)
    def __repr__(self) -> str:
        return "({},{})".format(self.x,self.y)
    
    def get_magnitude(self):
        if self.x != 0 or self.y != 0:
            return ((self.x **2)+(self.y**2))**(1./2.)
        else:
            return 0
    def normalize(self):
        #if self.x != 0 and self.y != 0:
            magnitude = self.get_magnitude()
            self.x /= magnitude
            self.y /= magnitude
    def __add__(self,rhs):
        return (self.x + rhs.x,self.y + rhs.y)

A = (10.0, 20.0)
B = (30.0, 35.0)
C = (15.0, 45.0)
AB = vector2(A,B)
BC = vector2(B,C)
AC = vector2(A,C)
print(AC)
AC = AB + BC
print(AC)