from pymath.geometry.d2.base_line import BaseLine
from pymath.geometry.d2.intersections import (get_ray_inter_ray,
                                              get_ray_inter_segment,
                                              ray_intersect_ray,
                                              ray_intersect_segment)
from pymath.geometry.d2.segment import Segment
from pymath.geometry.d2.vector import Vector


__all__ = ['Ray']

class Ray(BaseLine):
    
    # methods
    def intersect(self, other):
        if isinstance(other, Segment):
            return ray_intersect_segment(self, other)
        elif isinstance(other, Ray):
            return ray_intersect_ray(self, other)
        else:
            return other.intersect(self)
    
    def get_intersection(self, other):
        if isinstance(other, Segment):
            return get_ray_inter_segment(self, other)
        elif isinstance(other, Ray):
            return get_ray_inter_ray(self, other)
        else:
            return other.get_intersection(self)
    
    # op
    def __contains__(self, other):
        if isinstance(other, Segment):
            return other.a in self and other.b in self
            
        else:
            s_vec = self.__vec
            o_vec = Vector(other - self.a)
            
            if s_vec.x == 0:
                return other.x == self.a.x and o_vec.y / s_vec.y > 0
            elif s_vec.y == 0:
                return other.y == self.a.y and o_vec.x / s_vec.x > 0
            else:
                return (k := o_vec.x / s_vec.x) == o_vec.y / s_vec.y and k > 0
    
    def __eq__(self, other):
        return self.a == other.a and self.__vec.normalize() == other.__vec.normalize()
