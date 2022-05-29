from typing import overload

from pymath.geometry.d2.base_line import BaseLine
from pymath.geometry.d2.point import Point
from pymath.geometry.d2.ray import Ray
from pymath.geometry.d2.segment import Segment


class Line(BaseLine):
    
    def __init__(self, a: 'Point', b: 'Point') -> None: ...
    
    # methods
    def intersect(self, other: 'Segment' | 'Line') -> bool: ...
    
    @overload
    def get_intersection(self, other: 'Segment') -> None | 'Point' | 'Segment': ...
    
    @overload
    def get_intersection(self, other: 'Ray') -> None | 'Point' | 'Ray': ...
    
    @overload
    def get_intersection(self, other: 'Line') -> None | 'Point' | 'Line': ...
    
    def copy(self) -> 'Line': ...
    
    # op
    def __contains__(self, other: 'Point' | 'Segment' | 'Ray') -> bool: ...

    def __eq__(self, other: 'Line') -> bool: ...
