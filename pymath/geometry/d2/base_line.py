from decimal import Decimal

from pymath.geometry.d2.vector import Vector


__all__ = ['BaseLine']

class BaseLine:
    
    def __init__(self, a, b):
        if a == b:
            raise ValueError(f'Cannon create a {self.__class__.__name__.lower()} with 2 identical points.')
        
        self.a = a
        self.b = b
        
    def __repr__(self):
        return f'{self.__class__.__name__}({self.a}, {self.b})'
    
    # attrs
    @property
    def vec(self):
        return Vector(self.b - self.a)
    
    @property
    def slope(self):
        vec = self.vec
        if vec.x == 0:
            return Decimal('NaN')
        else:
            return vec.y / vec.x
    
    @property
    def intercept(self):
        slope = self.slope
        if slope.is_finite():
            return self.a.y - slope * self.a.x
        else:
            return Decimal('NaN')
