from decimal import Decimal
from typing import Self

from pymath.geometry.d2.point import Point
from pymath.geometry.d2.vector import Vector


class BaseLine:
    
    a: 'Point'
    b: 'Point'
    
    def __init__(self, a: 'Point', b: 'Point') -> None: ...
        
    def __repr__(self) -> str: ...
    
    # attrs
    @property
    def vec(self) -> 'Vector':
        """
        The vector from A to B.
        """
    
    @property
    def slope(self) -> Decimal: ...
    
    @property
    def intercept(self) -> Decimal: ...

    # methods
    def translate(self, vec: 'Vector') -> Self: ...
    
    def copy(self) -> 'BaseLine': ...
