from pymath.geometry.d2.base_line import BaseLine
from pymath.geometry.d2.intersections import (get_segment_inter_segment,
                                              segment_intersect_segment)


__all__ = ['Segment']

class Segment(BaseLine):
    
    def __init__(self, a, b):
        """
        Represent the segment [A, B].
        """
        super().__init__(a, b)
        
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
        if isinstance(other, Segment):
            return other.a in self and other.b in self
            
        else:
            if  min(self.a.x, self.b.x) <= other.x <= max(self.a.x, self.b.x) \
            and min(self.a.y, self.b.y) <= other.y <= max(self.a.y, self.b.y):
                if self.slope.is_finite():
                    return other.y == self.slope * other.x + self.intercept
                else:
                    return other.x == self.intercept
            else:
                return False

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b