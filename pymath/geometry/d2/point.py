from decimal import Decimal, getcontext
from math import cos, sin


class Point:
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def __repr__(self):
        return f'Point({self.__x.normalize()}, {self.__y.normalize()})'
    
    # attrs
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    # methods
    def distance(self, other):
        return ((self.__x - other.__x)**2 + (self.__y - other.__y)**2).sqrt()
    
    def square_distance(self, other):
        return (self.__x - other.__x)**2 + (self.__y - other.__y)**2
    
    def translate(self, vec):
        self.__x += vec.x
        self.__y += vec.y
        return self
        
    def rotate(self, center, angle):
        """
        Rotates the point counterclockwise around 'center' by 'angle' radians.
        """
        c = Decimal(round(cos(angle), getcontext().prec))
        s = Decimal(round(sin(angle), getcontext().prec))
        
        self.__x, self.__y = \
            c * (self.__x - center.__x) - s * (self.__y - center.__y) + center.__x, \
            s * (self.__x - center.__x) + c * (self.__y - center.__y) + center.__y
        return self
        
    def copy(self):
        return Point(self.__x, self.__y)
    
    # op
    def __add__(self, other):
        return Point(self.__x + other.x, self.__y + other.y)
    
    def __sub__(self, other):
        return Point(self.__x - other.x, self.__y - other.y)
    
    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y
