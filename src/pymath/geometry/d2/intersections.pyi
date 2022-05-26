from pymath.geometry.d2.line import Line
from pymath.geometry.d2.point import Point
from pymath.geometry.d2.segment import Segment
from pymath.geometry.d2.ray import Ray


# intersect ?
def segment_intsersect_segment(segment1: 'Segment', segment2: 'Segment') -> bool: ...

def ray_intersect_segment(ray: 'Ray', segment) -> bool: ...

def ray_intersect_ray(ray1: 'Ray', ray2: 'Ray') -> bool: ...

def line_intersect_segment(line: 'Line', segment: 'Segment') -> bool: ...

def line_intersect_ray(line: 'Line', ray: 'Ray') -> bool: ...

def line_intersect_line(line1: 'Line', line2: 'Line') -> bool: ...

# get intersection
def get_segment_inter_segment(segment1: 'Segment', segment2: 'Segment') -> None | 'Point' |'Segment': ...
    
def get_ray_inter_segment(ray: 'Ray', segment: 'Segment') -> None | 'Point' | 'Segment': ...

def get_ray_inter_ray(ray1: 'Ray', ray2: 'Ray') -> None | 'Point' | 'Ray': ...

def get_line_inter_segment(line: 'Line', segment: 'Segment') -> None | 'Point' |'Segment': ...

def get_line_inter_ray(line: 'Line', ray: 'Ray') -> None | 'Point' | 'Ray': ...

def get_line_inter_line(line1: 'Line', line2: 'Line') -> None | 'Point' | 'Line': ...