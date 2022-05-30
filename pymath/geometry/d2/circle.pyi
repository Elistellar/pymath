from decimal import Decimal
from typing import List, Self, Tuple, overload

from pymath.geometry.d2.line import Line
from pymath.geometry.d2.point import Point
from pymath.geometry.d2.ray import Ray
from pymath.geometry.d2.rect import Rect
from pymath.geometry.d2.segment import Segment
from pymath.geometry.d2.vector import Vector


class Circle:
    
    def __init__(self, center: 'Point', radius: Decimal) -> None: ...
    
    def __repr__(self) -> str: ...
    
    # attrs 
    @property
    def center(self) -> 'Point': ...
    
    @property
    def radius(self) -> Decimal: ...
    
    @property
    def area(self) -> Decimal: ...
    
    # methods
    def intersect(self, other: 'Segment' |'Ray' | 'Line' | 'Circle' | 'Rect') -> bool:
        """
        Returns weather the circle intersects with the other object.
        """
        
    def count_intersections(self, other: 'Segment' |'Ray' | 'Line' | 'Circle' | 'Rect') -> Decimal:
        """
        Returns the number of intersections with the other object.
        """      
    
    @overload
    def get_intersection(self, other: 'Segment' | 'Ray' | 'Line') -> None | 'Point' | Tuple['Point', 'Point']:
        """
        Returns all intersections with the other object.
        """
        
    @overload
    def get_intersection(self, other: 'Circle') -> None | 'Point' | Tuple['Point', 'Point'] | 'Circle':
        """
        Returns all intersections with the other object.
        """
        
    @overload
    def get_intersection(self, other: 'Rect') -> None | List['Point']:
        """
        Returns all intersections with the other object.
        """
    
    def translate(self, vec: 'Vector') -> Self: ...
    
    def copy(self) -> 'Circle': ...
    
    # op
    def __contains__(self, other: 'Point' | 'Segment' | 'Circle' | 'Rect') -> bool: ...
               
    def __eq__(self, other: 'Circle') -> bool: ...
