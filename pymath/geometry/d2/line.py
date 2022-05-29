from pymath.geometry.d2.base_line import BaseLine
from pymath.geometry.d2.intersections import (get_line_inter_line,
                                              get_line_inter_ray,
                                              get_line_inter_segment,
                                              line_intersect_line,
                                              line_intersect_ray,
                                              line_intersect_segment)
from pymath.geometry.d2.point import Point
from pymath.geometry.d2.ray import Ray
from pymath.geometry.d2.segment import Segment
from pymath.geometry.d2.vector import Vector, det


__all__ = ['Line']

class Line(BaseLine):
        
    # methods
    def intersect(self, other):
        if isinstance(other, Segment):
            return line_intersect_segment(self, other)
        elif isinstance(other, Ray):
            return line_intersect_ray(self, other)
        elif isinstance(other, Line):
            return line_intersect_line(self, other)
        else:
            return other.intersect(self)
    
    def get_intersection(self, other):
        
        if isinstance(other, Segment):
            return get_line_inter_segment(self, other)
        elif isinstance(other, Ray):
            return get_line_inter_ray(self, other)
        elif isinstance(other, Line):
            return get_line_inter_line(self, other)
        else:
            return other.get_intersection(self)
    
    # op
    def __contains__(self, other):
        if isinstance(other, Point):
            vec = Vector(self.a - other)
        else:
            vec = other.vec
        return det(vec, self.__vec) == 0

    def __eq__(self, other):
        v1 = self.__vec.normalize()
        v2 = other.__vec.normalize()
        return v1 == v2 or v1 == -1 * v2
