from decimal import Decimal

from pymath.geometry.d2.point import Point
from pymath.geometry.d2.segment import Segment
from pymath.geometry.d2.vector import Vector


class Line:
    
    def __init__(self, a: 'Point', b: 'Point') -> None: ...
        
    def __repr__(self) -> str: ...
    
    # attrs
    @property
    def vec(self) -> 'Vector': ...
    
    @property
    def slope(self) -> Decimal: ...
    
    @property
    def intercept(self) -> Decimal: ...
    
    # methods
    def intersect(self, other: 'Segment' | 'Line') -> bool: ...
    
    def get_intersection(self, other: 'Segment' | 'Line') -> None | 'Point' | 'Segment' | 'Line': ...
    
    # op
    def __contains__(self, other: 'Point' | 'Segment') -> bool: ...
