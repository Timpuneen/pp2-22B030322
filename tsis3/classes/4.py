from math import sqrt as kvadrat

class Point:
    def __init__(self):
        self.x = 0
        self.y = 0

    def show(self):
        print ({"x coord ": self.x, "y coord ": self.y})

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self,x1,y1,x2,y2):
        return kvadrat((x2 - x1)**2+(y2 - y1)**2)
 
to4ka = Point()
to4ka.show()
to4ka.move(12,12)
to4ka.show()
print(to4ka.dist(1,1,5,5))