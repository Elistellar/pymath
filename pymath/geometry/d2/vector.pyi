from decimal import Decimal
from typing import overload

from .point import Point


def det(v1: 'Vector', v2: 'Vector') -> Decimal: ...

class Vector:
    
    @overload
    def __init__(self, x: Decimal, y: Decimal) -> None: ...
    
    @overload
    def __init__(self, x: 'Point') -> None: ...
    
    def __repr__(self) -> str: ...
    
    # attrs
    @property
    def x(self) -> Decimal: ...
    
    @property
    def y(self) -> Decimal: ...
    
    @property
    def lenght(self) -> Decimal: ...
    
    @property
    def magnitude(self) -> Decimal: ...
    
    @property
    def square_lenght(self) -> Decimal: ...
    
    # methods
    def normalize(self) -> 'Vector':
        """
        Returns another vector with the same direction, but with a lenght of 1.
        """
    
    def det(self, other: 'Vector') -> Decimal: ...

    def angle(self, other: 'Vector') -> Decimal:
        """
        Returns the angle (self; other)
        """

    def project_on(self, other: 'Vector') -> 'Vector':
        """
        Returns the projection of self onto other
        """

    def rotate(self, angle: Decimal) -> 'Vector':
        """
        Rotates the vector counterclockwise by 'angle' radians.
        """

    def copy(self) -> 'Vector': ...

    # op
    def __add__(self, other: 'Vector') -> 'Vector': ...
    
    def __sub__(self, other: 'Vector') -> 'Vector': ...
    
    @overload
    def __mul__(self, other: 'Vector') -> Decimal: ...
    
    @overload
    def __mul__(self, other: Decimal) -> 'Vector': ...
    
    def __rmul__(self, other: Decimal) -> 'Vector': ...

    def __eq__(self, other: 'Point') -> bool: ...
