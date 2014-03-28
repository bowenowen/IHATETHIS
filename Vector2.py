import math

class Vector2:
    def __init__(self, x, y):
        self.x = float (x)
        self.y = float (y)
        self.magnitude = math.sqrt (x**2 + y**2)

    def __repr__ (self):
        return str ((self.x, self.y))

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __mul__ (self, other):
        if isinstance (other,float) == True or isinstance (other, int) == True:
            return Vector2(self.x * other, self.y * other)
        else:
             return float (self.x * other.x + self.y * other.y)

    def __rmul__ (self, other):
        if isinstance (other,float) == True or isinstance (other, int) == True:
            return Vector2(self.x * other, self.y * other)

    def __div__ (self, other):
        return Vector2(self.x / other, self.y / other)

    def __truediv__ (self, other):
        return Vector2(self.x / other, self.y / other)

    def __abs__ (self):
        return self.magnitude

    def Normalize (self):
        return Vector2(self.x / self.magnitude, self.y / self.magnitude)
