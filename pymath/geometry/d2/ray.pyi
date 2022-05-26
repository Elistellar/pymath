from typing import overload

from pymath.geometry.d2.base_line import BaseLine
from pymath.geometry.d2.line import Line
from pymath.geometry.d2.point import Point
from pymath.geometry.d2.segment import Segment


class Ray(BaseLine):
    
    def __init__(self, a: 'Point', b: 'Point'): ...

    # methods
    def intersect(self, other: 'Segment' | 'Ray' | 'Line') -> bool: ...
    
    @overload
    def get_intersection(self, other: 'Segment') -> None | 'Point' | 'Segment': ...
    
    @overload
    def get_intersection(self, other: 'Ray') -> None | 'Point' | 'Ray': ...
    
    @overload
    def get_intersection(self, other: 'Line') -> None | 'Point' | 'Ray': ...
    
    # op
    def __contains__(self, other: 'Point' | 'Segment') -> bool: ...
    
    def __eq__(self, other: 'Ray') -> bool: ...
