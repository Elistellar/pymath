from typing import overload

from pymath.geometry.d2.base_line import BaseLine
from pymath.geometry.d2.point import Point
from pymath.geometry.d2.ray import Ray
from pymath.geometry.d2.segment import Segment
from pymath.geometry.d2.vector import Vector


class Line(BaseLine):
    
    def __init__(self, a: 'Point', b: 'Point') -> None:
        """
        Represent the line (A, B).
        """
    
    # methods
    def intersect(self, other: 'Segment' | 'Line') -> bool:
        """
        Returns weather the line intersects with the other object.
        """
    
    @overload
    def get_intersection(self, other: 'Segment') -> None | 'Point' | 'Segment':
        """
        Returns the intersection with the other object.
        """
    
    @overload
    def get_intersection(self, other: 'Ray') -> None | 'Point' | 'Ray':
        """
        Returns the intersection with the other object.
        """
    
    @overload
    def get_intersection(self, other: 'Line') -> None | 'Point' | 'Line':
        """
        Returns the intersection with the other object.
        """
    
    def translate(self, vec: 'Vector') -> 'Line': ...
    
    def copy(self) -> 'Line': ...
    
    # op
    def __contains__(self, other: 'Point' | 'Segment' | 'Ray') -> bool: ...

    def __eq__(self, other: 'Line') -> bool: ...
