from decimal import Decimal
from typing import overload

from pymath.geometry.d2.point import Point
from pymath.geometry.d2.segment import Segment
from pymath.geometry.d2.vector import Vector


class BaseLine:
    
    def __init__(self, a: 'Point', b: 'Point') -> None: ...
        
    def __repr__(self) -> str: ...
    
    # attrs
    @property
    def vec(self) -> 'Vector': ...
    
    @property
    def slope(self) -> Decimal: ...
    
    @property
    def intercept(self) -> Decimal: ...
