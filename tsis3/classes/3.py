class Shape:
    def area(self):
        return 0

class Rectagle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

pr9mougolnik = Rectagle(10, 20)
print(pr9mougolnik.area())