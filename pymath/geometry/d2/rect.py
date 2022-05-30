from decimal import Decimal

from pymath.geometry.d2.circle import Circle
from pymath.geometry.d2.intersections import (count_rect_inter_circle,
                                              count_rect_inter_line,
                                              count_rect_inter_ray,
                                              count_rect_inter_rect,
                                              count_rect_inter_segment,
                                              get_rect_inter_circle,
                                              get_rect_inter_line,
                                              get_rect_inter_ray,
                                              get_rect_inter_rect,
                                              get_rect_inter_segment,
                                              rect_intersect_circle,
                                              rect_intersect_line,
                                              rect_intersect_ray,
                                              rect_intersect_rect,
                                              rect_intersect_segment)
from pymath.geometry.d2.line import Line
from pymath.geometry.d2.point import Point
from pymath.geometry.d2.ray import Ray
from pymath.geometry.d2.segment import Segment


__all__ = ['Rect']

class Rect:
    
    def __init__(self, topleft, topright, bottomright, bottomleft):
        
        #  TODO: ensure points are in the good order
         
        self.__topleft = topleft
        self.__topright = topright
        self.__bottomright = bottomright
        self.__bottomleft = bottomleft
        
    def __repr__(self):
        return f'Rect({self.__topleft}, {self.__topright}, {self.__bottomright}, {self.__bottomleft})'
    
    # attrs
    @property
    def topleft(self):
        return self.__topleft
    
    @property
    def topright(self):
        return self.__topright
    
    @property
    def bottomright(self):
        return self.__bottomright
    
    @property
    def bottomleft(self):
        return self.__bottomleft
    
    @property
    def width(self):
        return self.__topleft.distance(self.__topright)
    
    @property
    def height(self):
        return self.__topleft.distance(self.__bottomleft)
    
    @property
    def area(self):
        return self.width * self.height
    
    @property
    def center(self):
        return Segment(self.__topleft, self.__bottomright).middle

    # methods
    def intersect(self, other):
        if isinstance(other, Segment):
            return rect_intersect_segment(self, other)
        elif isinstance(other, Ray):
            return rect_intersect_ray(self, other)
        elif isinstance(other, Line):
            return rect_intersect_line(self, other)
        elif isinstance(other, Circle):
            return rect_intersect_circle(self, other)
        elif isinstance(other, Rect):
            return rect_intersect_rect(self, other)
        else:
            return other.intersect(self)
    
    def count_intersections(self, other):
        if isinstance(other, Segment):
            return count_rect_inter_segment(self, other)
        elif isinstance(other, Ray):
            return count_rect_inter_ray(self, other)
        elif isinstance(other, Line):
            return count_rect_inter_line(self, other)
        elif isinstance(other, Circle):
            return count_rect_inter_circle(self, other)
        elif isinstance(other, Rect):
            return count_rect_inter_rect(self, other)
        else:
            return other.intersect(self)
    
    def get_intersections(self, other):
        if isinstance(other, Segment):
            return get_rect_inter_segment(self, other)
        elif isinstance(other, Ray):
            return get_rect_inter_ray(self, other)
        elif isinstance(other, Line):
            return get_rect_inter_line(self, other)
        elif isinstance(other, Circle):
            return get_rect_inter_circle(self, other)
        elif isinstance(other, Rect):
            return get_rect_inter_rect(self, other)
        else:
            return other.intersect(self)
    
    def translate(self, vec):
        self.__topleft.translate(vec)
        self.__topright.translate(vec)
        self.__bottomright.translate(vec)
        self.__bottomleft.translate(vec)
        return self
    
    def rotate(self, center, angle):
        self.__topleft.rotate(center, angle)
        self.__topright.rotate(center, angle)
        self.__bottomright.rotate(center, angle)
        self.__bottomleft.rotate(center, angle)
        return self
    
    def copy(self):
        return Rect(self.__topleft, self.__topright, self.__bottomleft, self.__bottomright)
    
    # op
    def __contains__(self, other):
        if isinstance(other, Point):
            r = Ray(other, self.__topleft - Point(Decimal(1), Decimal(1)))
            n = self.count_intersections(r)
            if n == 1:
                return True
            elif n == 2:
                return other in Segment(self.__bottomleft, self.__bottomright) \
                    or other in Segment(self.__topright, self.__bottomright)
            else:
                return False
            
        elif isinstance(other, Segment):
            raise NotImplementedError()
        elif isinstance(other, Circle):
            raise NotImplementedError()
        elif isinstance(other, Rect):
            raise NotImplementedError()
    
    def __eq__(self, other):
        return self.__topleft     == other.__topleft   \
           and self.__topright    == other.__topright   \
           and self.__bottomright == other.__bottomright \
           and self.__bottomleft  == other.__bottomleft
