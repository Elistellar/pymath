from decimal import Decimal
from typing import List, Self, Tuple, overload

from pymath.geometry.d2.circle import Circle
from pymath.geometry.d2.line import Line
from pymath.geometry.d2.point import Point
from pymath.geometry.d2.ray import Ray
from pymath.geometry.d2.segment import Segment
from pymath.geometry.d2.vector import Vector


class Rect:
    
    def __init__(self, topleft: 'Point', topright: 'Point', bottomright: 'Point', bottomleft: 'Point') -> None: ...
        
    def __repr__(self) -> str: ...
    
    # attrs
    @property
    def topleft(self) -> 'Point': ...
    
    @property
    def topright(self) -> 'Point': ...
    
    @property
    def bottomright(self) -> 'Point': ...
    
    @property
    def bottomleft(self) -> 'Point': ...
    
    @property
    def width(self) -> Decimal: ...
    
    @property
    def height(self) -> Decimal: ...
    
    @property
    def area(self) -> Decimal: ...
    
    @property
    def center(self) -> 'Point': ...

    # methods
    def intersect(self, other: 'Segment' | 'Ray' | 'Line' | 'Circle' | 'Rect') -> bool: ...
    
    def count_intersections(self, other: 'Segment' | 'Ray' | 'Line' | 'Circle' | 'Rect') -> Decimal: ...
    
    @overload
    def get_intersections(self, other: 'Segment' | 'Ray' | 'Line') -> None | 'Point' | Tuple['Point', 'Point'] | 'Segment': ...
    
    @overload
    def get_intersections(self, other: 'Circle') -> None | List['Point']: ...
    
    @overload
    def get_intersections(self, other: 'Rect') \
        -> None | 'Point' | Tuple['Point', 'Point'] | 'Segment' | Tuple['Segment', 'Segment'] | Tuple['Segment', 'Segment', 'Segment'] | 'Rect': ...
    
    def translate(self, vec: 'Vector') -> Self: ...
    
    def rotate(self, center: 'Point', angle: Decimal) -> Self: ...
    
    def copy(self) -> 'Rect': ...
    
    # op
    def __contains__(self, other: 'Point' | 'Segment' | 'Circle' | 'Rect') -> bool: ...
    
    def __eq__(self, other: 'Rect') -> bool: ...
