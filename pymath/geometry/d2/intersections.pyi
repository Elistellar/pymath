from decimal import Decimal
from typing import List, Literal, Tuple

from pymath.geometry.d2.circle import Circle
from pymath.geometry.d2.line import Line
from pymath.geometry.d2.point import Point
from pymath.geometry.d2.ray import Ray
from pymath.geometry.d2.rect import Rect
from pymath.geometry.d2.segment import Segment


def sgn(d: Decimal) -> Literal[-1, 1]: ...

# intersect ?
def segment_intsersect_segment(segment1: 'Segment', segment2: 'Segment') -> bool:
    """
    Returns whether two segments intersect.
    """

def ray_intersect_segment(ray: 'Ray', segment: 'Segment') -> bool:
    """
    Returns whether a ray and a segment intersect.
    """

def ray_intersect_ray(ray1: 'Ray', ray2: 'Ray') -> bool:
    """
    Returns whether two rays intersect.
    """

def line_intersect_segment(line: 'Line', segment: 'Segment') -> bool:
    """
    Returns whether a line and a segment intersect.
    """

def line_intersect_ray(line: 'Line', ray: 'Ray') -> bool:
    """
    Returns whether a line and a ray intersect.
    """

def line_intersect_line(line1: 'Line', line2: 'Line') -> bool:
    """
    Returns whether two lines intersect.
    """

def circle_intersect_segment(circle: 'Circle', segment: 'Segment') -> bool:
    """
    Returns whether a circle and a segment intersect.
    """

def circle_intersect_ray(circle: 'Circle', ray: 'Ray') -> bool:
    """
    Returns whether a circle and a ray intersect.
    """

def circle_intersect_line(circle: 'Circle', line: 'Line') -> bool:
    """
    Returns whether a circle and a line intersect.
    """

def circle_intersect_circle(circle1: 'Circle', circle2: 'Circle') -> bool:
    """
    Returns whether two circles intersect.
    """

def rect_intersect_segment(rect: 'Rect', segment: 'Segment') -> bool:
    """
    Returns whether a rect and a segment intersect.
    """

def rect_intersect_ray(rect: 'Rect', ray: 'Ray') -> bool:
    """
    Returns whether a rect and a ray intersect.
    """

def rect_intersect_line(rect: 'Rect', line: 'Line') -> bool:
    """
    Returns whether a rect and a line intersect.
    """
def rect_intersect_circle(rect: 'Rect', circle: 'Circle') -> bool:
    """
    Returns whether a rect and a circle intersect.
    """

def rect_intersect_rect(rect1: 'Rect', rect2: 'Rect') -> bool:
    """
    Returns whether two rects intersect.
    """


# get number of intersections
def count_cicle_inter_segment(circle: 'Circle', segment: 'Segment') -> Decimal:
    """
    Returns the number of intersections between a circle and a segment.
    """

def count_cicle_inter_ray(circle: 'Circle', ray: 'Ray') -> Decimal:
    """
    Returns the number of intersections between a circle and a ray.
    """

def count_cicle_inter_line(circle: 'Circle', line: 'Line') -> Decimal:
    """
    Returns the number of intersections between a circle and a line.
    """

def count_cicle_inter_circle(circle1: 'Circle', circle2: 'Circle') -> Decimal:
    """
    Returns the number of intersections between two cricles.
    """

def count_rect_inter_segment(rect: 'Rect', segment: 'Segment') -> Decimal:
    """
    Returns the number of intersections between a rect and a segment.
    """

def count_rect_inter_ray(rect: 'Rect', ray: 'Ray') -> Decimal:
    """
    Returns the number of intersections between a rect and a ray.
    """

def count_rect_inter_line(rect: 'Rect', line: 'Line') -> Decimal:
    """
    Returns the number of intersections between a rect and a line.
    """

def count_rect_inter_circle(rect: 'Rect', circle: 'Circle') -> Decimal:
    """
    Returns the number of intersections between a rect and a circle.
    """

def count_rect_inter_rect(rect1: 'Rect', rect2: 'Rect') -> Decimal:
    """
    Returns the number of intersections between two rects.
    """


# get intersection
def get_segment_inter_segment(segment1: 'Segment', segment2: 'Segment') -> None | 'Point' |'Segment':
    """
    Returns the intersection of two segments.
    """
    
def get_ray_inter_segment(ray: 'Ray', segment: 'Segment') -> None | 'Point' | 'Segment':
    """
    Returns the intersection of a ray and a segment.
    """

def get_ray_inter_ray(ray1: 'Ray', ray2: 'Ray') -> None | 'Point' | 'Ray':
    """
    Returns the intersection of two rays.
    """

def get_line_inter_segment(line: 'Line', segment: 'Segment') -> None | 'Point' |'Segment':
    """
    Returns the intersection of a line and a segment.
    """

def get_line_inter_ray(line: 'Line', ray: 'Ray') -> None | 'Point' | 'Ray':
    """
    Returns the intersection of a line and a ray.
    """

def get_line_inter_line(line1: 'Line', line2: 'Line') -> None | 'Point' | 'Line':
    """
    Returns the intersection of two lines.
    """

def get_circle_inter_segment(circle: 'Circle', segment: 'Segment') -> None | 'Point' | Tuple['Point', 'Point']:
    """
    Returns the intersection of a circle and a segment.
    """

def get_circle_inter_ray(circle: 'Circle', ray: 'Ray') -> None | 'Point' | Tuple['Point', 'Point']:
    """
    Returns the intersection of a circle and a ray.
    """

def get_circle_inter_line(circle: 'Circle', line: 'Line') -> None | 'Point' | Tuple['Point', 'Point']:
    """
    Returns the intersection of a circle and a line.
    """

def get_circle_inter_circle(circle1: 'Circle', circle2: 'Circle') -> None | 'Point' | Tuple['Point', 'Point'] | 'Circle':
    """
    Returns the intersection of two circles.
    """

def get_rect_inter_segment(rect: 'Rect', segment: 'Segment') -> None | 'Point' | Tuple['Point', 'Point'] | 'Segment':
    """
    Returns the intersection of a rect and a segment.
    """

def get_rect_inter_ray(rect: 'Rect', ray: 'Ray') -> None | 'Point' | Tuple['Point', 'Point'] | 'Segment':
    """
    Returns the intersection of a rect and a ray.
    """

def get_rect_inter_line(rect: 'Rect', line: 'Line') -> None | 'Point' | Tuple['Point', 'Point'] | 'Segment':
    """
    Returns the intersection of a rect and a line.
    """

def get_rect_inter_circle(rect: 'Rect', circle: 'Circle') -> None | List['Point']:
    """
    Returns the intersection of a rect and a circle.
    """

def get_rect_inter_rect(rect1: 'Rect', rect2: 'Rect')-> None | 'Point' | Tuple['Point', 'Point'] | 'Segment' | Tuple['Segment', 'Segment'] | Tuple['Segment', 'Segment', 'Segment'] | 'Rect':
    """
    Returns the intersection of two rects.
    """
