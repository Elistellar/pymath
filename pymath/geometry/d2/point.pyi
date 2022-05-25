from decimal import Decimal

from pymath.geometry.d2.vector import Vector


class Point:
    
    def __init__(self, x: Decimal, y: Decimal): ...
    
    def __repr__(self) -> str: ...
    
    # attrs
    @property
    def x(self) -> Decimal: ...
    
    @property
    def y(self) -> Decimal: ...

    # op
    def __add__(self, other: 'Point' | 'Vector') -> 'Point': ...
    
    def __sub__(self, other: 'Point' | 'Vector') -> 'Point': ...
