from decimal import Decimal

from pymath.geometry.d2.intersections import (get_line_inter_line,
                                              get_line_inter_segment,
                                              line_intersect_line,
                                              line_intersect_segment)
from pymath.geometry.d2.point import Point
from pymath.geometry.d2.segment import Segment
from pymath.geometry.d2.vector import Vector


class Line:
    
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def __repr__(self):
        return f'Line({self.a}, {self.b})'
    
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
        if isinstance(other, Line):
            return line_intersect_line(self, other)
        elif isinstance(other, Segment):
            return line_intersect_segment(self, other)
        else:
            return other.intersect(self)
    
    def get_intersection(self, other):
        if isinstance(other, Line):
            return get_line_inter_line(self, other)
        elif isinstance(other, Segment):
            return get_line_inter_segment(self, other)
        else:
            return other.get_intersection(self)
    
    # op
    def __contains__(self, other):
        if isinstance(other, Point):
            vec = Vector(self.a - other)
        else:
            vec = other.vec
        return vec.det(self.vec) == 0
