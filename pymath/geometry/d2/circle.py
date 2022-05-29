from decimal import Decimal
from math import pi

from pymath.geometry.d2.intersections import (circle_intersect_circle,
                                              circle_intersect_line,
                                              circle_intersect_ray,
                                              circle_intersect_segment,
                                              count_cicle_inter_circle,
                                              count_cicle_inter_line,
                                              count_cicle_inter_ray,
                                              count_cicle_inter_segment,
                                              get_circle_inter_circle,
                                              get_circle_inter_line,
                                              get_circle_inter_ray,
                                              get_circle_inter_segment)
from pymath.geometry.d2.line import Line
from pymath.geometry.d2.point import Point
from pymath.geometry.d2.ray import Ray
from pymath.geometry.d2.segment import Segment


__all__ = ['Circle']

class Circle:
    
    def __init__(self, center, radius):
        self.__center = center
        self.__radius = radius
       
    def __repr__(self):
        return f'Circle({self.__center}, {self.__radius})'
    
    # attrs 
    @property
    def center(self):
        return self.__center
    
    @property
    def radius(self):
        return self.__radius
    
    @property
    def area(self):
        return self.__radius ** 2 * Decimal(pi)
    
    # methods
    def intersect(self, other):
        if isinstance(other, Segment):
            return circle_intersect_segment(self, other)
        elif isinstance(other, Ray):
            return circle_intersect_ray(self, other)
        elif isinstance(other, Line):
            return circle_intersect_line(self, other)
        elif isinstance(other, Circle):
            return circle_intersect_circle(self, other)
        else:
            return other.intersect(self)
        
    def count_intersections(self, other):
        if isinstance(other, Segment):
            return count_cicle_inter_segment(self, other)
        elif isinstance(other, Ray):
            return count_cicle_inter_ray(self, other)
        elif isinstance(other, Line):
            return count_cicle_inter_line(self, other)
        elif isinstance(other, Circle):
            return count_cicle_inter_circle(self, other)
        else:
            return other.count_intersections(self)
    
    def get_intersection(self, other):
        if isinstance(other, Segment):
            return get_circle_inter_segment(self, other)
        elif isinstance(other, Ray):
            return get_circle_inter_ray(self, other)
        elif isinstance(other, Line):
            return get_circle_inter_line(self, other)
        elif isinstance(other, Circle):
            return get_circle_inter_circle(self, other)
        else:
            return other.get_intersection(self)
    
    def copy(self):
        return Circle(self.__center, self.__radius)
    
    # op
    def __contains__(self, other):
        if isinstance(other, Point):
            return self.__center.distance(other) <= self.__radius
        elif isinstance(other, Segment):
            return self.__center.distance(other.a) <= self.__radius \
               and self.__center.distance(other.b) <= self.__radius
        elif isinstance(other, Circle):
            return self.__center.distance(other.__center) + other.__radius <= self.__radius
               
    def __eq__(self, other):
        return self.__center == other.__center and self.__radius == other.__radius
