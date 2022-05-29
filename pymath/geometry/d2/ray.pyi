from typing import overload

from pymath.geometry.d2.base_line import BaseLine
from pymath.geometry.d2.line import Line
from pymath.geometry.d2.point import Point
from pymath.geometry.d2.segment import Segment
from pymath.geometry.d2.vector import Vector


class Ray(BaseLine):
    
    def __init__(self, a: 'Point', b: 'Point') -> None:
        """
        Represent the ray [A, B).
        """

    # methods
    def intersect(self, other: 'Segment' | 'Ray' | 'Line') -> bool:
        """
        Returns weather the ray intersects with the other object.
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
    def get_intersection(self, other: 'Line') -> None | 'Point' | 'Ray':
        """
        Returns the intersection with the other object.
        """
    
    def translate(self, vec: 'Vector') -> 'Ray': ...
    
    def copy(self) -> 'Ray': ...
    
    # op
    def __contains__(self, other: 'Point' | 'Segment') -> bool: ...
    
    def __eq__(self, other: 'Ray') -> bool: ...
