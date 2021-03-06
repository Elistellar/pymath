from decimal import Decimal
from typing import Self

from pymath.geometry.d2.vector import Vector


class Point:
    
    def __init__(self, x: Decimal, y: Decimal): ...
    
    def __repr__(self) -> str: ...
    
    # attrs
    @property
    def x(self) -> Decimal: ...
    
    @property
    def y(self) -> Decimal: ...

    # methods
    def distance(self, other: 'Point') -> Decimal: ...
    
    def square_distance(self, other: 'Point') -> Decimal: ...
    
    def translate(self, vec: 'Vector') -> Self: ...
    
    def rotate(self, center: 'Point', angle: Decimal) -> Self:
        """
        Rotates the point counterclockwise around 'center' by 'angle' radians.
        """
    
    def copy(self) -> 'Point': ...

    # op
    def __add__(self, other: 'Point' | 'Vector') -> 'Point': ...
    
    def __sub__(self, other: 'Point' | 'Vector') -> 'Point': ...

    def __eq__(self, other: 'Point') -> bool: ...
