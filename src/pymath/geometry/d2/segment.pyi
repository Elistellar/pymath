from typing import overload
from pymath.geometry.d2.base_line import BaseLine
from pymath.geometry.d2.line import Line
from pymath.geometry.d2.point import Point
from pymath.geometry.d2.segment import Segment
from pymath.geometry.d2.ray import Ray


class Segment(BaseLine):
    
    def __init__(self, a: 'Point', b: 'Point') -> None: ...
        
    # methods
    def intersect(self, other: 'Segment' | 'Ray' | 'Line') -> bool: ...
    
    def get_intersection(self, other: 'Segment' | 'Ray' | 'Line') -> None | 'Point' | 'Segment': ...
    
    # op
    def __contains__(self, other: 'Point' | 'Segment') -> bool: ...

    def __eq__(self, other: 'Segment') -> bool: ...
