from decimal import Decimal, getcontext
from math import acos

from pymath.geometry.d2.point import Point


__all__ = ['Vector', 'det']

def det(v1, v2):
    return v1.x * v2.y - v1.y * v2.x

class Vector:
    
    def __init__(self, x, y = None):
        if y is None:
            self.__x, self.__y = x.x, x.y
        else:
            self.__x = x
            self.__y = y
    
    def __repr__(self):
        return f'Vector({self.__x.normalize()}, {self.__y.normalize()})'
    
    # attrs
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def lenght(self):
        return (self.__x ** 2 + self.__y ** 2).sqrt()
    
    @property
    def magnitude(self):        
        return (self.__x ** 2 + self.__y ** 2).sqrt()
    
    @property
    def square_lenght(self):
        return self.__x ** 2 + self.__y ** 2
    
    # methods
    def normalize(self):
        getcontext().prec += 2
        m = 1 / self.lenght
        getcontext().prec -= 2
        return m * self
    
    def det(self, other):
        return self.__x * other.__y - self.__y * other.__x
    
    def angle(self, other):
        getcontext().prec += 2
        a = acos(self * other / (self.lenght_square * other.lenght_square).sqrt())
        getcontext().prec -= 2
        return a

    def project_on(self, other):
        return (self * other) / other.square_lenght * other
    
    def rotate(self, angle):
        p = Point(self.__x, self.__y)
        p.rotate(Point(Decimal(0), Decimal(0)), angle)
        self.__x, self.__y = p.x, p.y
        return self
    
    def copy(self):
        return Vector(self.__x, self.__y)

    # op
    def __add__(self, other):
        return Vector(self.__x + other.x, self.__y + other.y)
    
    def __sub__(self, other):
        return Vector(self.__x - other.x, self.__y - other.y)
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.__x * other.__x + self.__y * other.__y
        
        return Vector(self.__x * other, self.__y * other)
    
    def __rmul__(self, other):
        return Vector(self.__x * other, self.__y * other)

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y
