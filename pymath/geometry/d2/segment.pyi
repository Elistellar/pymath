from decimal import Decimal
from typing import Self, Tuple, overload

from pymath.geometry.d2.base_line import BaseLine
from pymath.geometry.d2.circle import Circle
from pymath.geometry.d2.line import Line
from pymath.geometry.d2.point import Point
from pymath.geometry.d2.ray import Ray
from pymath.geometry.d2.rect import Rect
from pymath.geometry.d2.segment import Segment
from pymath.geometry.d2.vector import Vector


class Segment(BaseLine):
    
    def __init__(self, a: 'Point', b: 'Point') -> None:
        """
        Represent the segment [A, B].
        """
    
    # attrs
    @property
    def length(self) -> Decimal: ...
    
    @property
    def square_lenght(self) -> Decimal: ...
    
    @property
    def middle(self) -> 'Point': ...
    
    # methods
    def intersect(self, other: 'Segment' | 'Ray' | 'Line' | 'Circle' | 'Rect') -> bool:
        """
        Returns weather the segment intersects with the other object.
        """
    
    @overload
    def get_intersection(self, other: 'Segment' | 'Ray' | 'Line') -> None | 'Point' | 'Segment':
        """
        Returns the intersection with the other object.
        """
    
    @overload
    def get_intersection(self, other: 'Circle') -> None | 'Point' | Tuple['Point', 'Point']:
        """
        Returns the intersection with the other object.
        """
    
    @overload
    def get_intersection(self, other: 'Rect') -> None | 'Point' | Tuple['Point', 'Point'] | 'Segment':
        """
        Returns the intersection with the other object.
        """
    
    def translate(self, vec: 'Vector') -> Self: ...
    
    def copy(self) -> 'Segment': ...
    
    # op
    def __contains__(self, other: 'Point' | 'Segment') -> bool: ...

    def __eq__(self, other: 'Segment') -> bool: ...
