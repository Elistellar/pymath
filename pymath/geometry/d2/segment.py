from decimal import Decimal

from pymath.geometry.d2.intersections import (get_segment_inter_segment,
                                              segment_intersect_segment)
from pymath.geometry.d2.vector import Vector


class Segment:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __repr__(self):
        return f'Segment({self.a}, {self.b})'
    
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
    
    # methods
    def intersect(self, other):
        if isinstance(other, Segment):
            return segment_intersect_segment(self, other)
        else:
            return other.intersect(self)
    
    def get_intersection(self, other):
        if isinstance(other, Segment):
            return get_segment_inter_segment(self, other)
        else:
            return other.get_intersection(self)
    
    # op
    def __contains__(self, other):
        return Vector(self.a - other).det(self.vec) == 0
