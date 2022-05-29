from decimal import Decimal

from pymath.geometry.d2.point import Point
from pymath.geometry.d2.vector import Vector, det


__all__ = [
    # intersect ?
    'segment_intersect_segment',
    'ray_intersect_segment',
    'ray_intersect_ray',
    'line_intersect_segment',
    'line_intersect_ray',
    'line_intersect_line',
    'circle_intersect_segment',
    'circle_intersect_ray',
    'circle_intersect_line',
    'circle_intersect_circle',
    
    # get number of intersections
    'count_cicle_inter_segment',
    'count_cicle_inter_ray',
    'count_cicle_inter_line',
    'count_cicle_inter_circle',
    
    # get intersection
    'get_segment_inter_segment',
    'get_ray_inter_segment',
    'get_ray_inter_ray',
    'get_line_inter_segment', 
    'get_line_inter_ray',
    'get_line_inter_line',
    'get_circle_inter_segment',
    'get_circle_inter_ray',
    'get_circle_inter_line',
    'get_circle_inter_circle',
]

def sgn(d):
    return 1 if d > 0 else -1

# intersect ?
def segment_intersect_segment(segment1, segment2):
    """
    Returns whether two segments intersect.
    """
    det = det(segment1.vec, segment2.vec)
        
    if det == 0:
        # overlapping
        return segment1.a in segment2 or segment1.b in segment2 \
            or segment2.a in segment1 or segment2.b in segment1
        
    else: # secant
        k1 = det(segment2.vec, Vector(segment1.a - segment2.a)) / det
        k2 = - det(segment1.vec, Vector(segment2.a - segment1.a)) / det

        return 0 <= k1 <= 1 and 0 <= k2 <= 1

def ray_intersect_segment(ray, segment):
    """
    Returns whether a ray and a segment intersect.
    """
    det = det(ray.vec, segment.vec)
    
    if det == 0: # parallel
        return segment.a in ray or segment.b in ray
    
    else:
        k1 = det(segment.vec, Vector(ray.a - segment.a)) / det
        k2 = - det(ray.vec, Vector(segment.a - ray.a)) / det

        return 0 <= k1 <= 1 and 0 < k2

def ray_intersect_ray(ray1, ray2):
    """
    Returns whether two rays intersect.
    """
    det = det(ray1.vec, ray2.vec)
    
    if det == 0: # parallel
        return ray2.a in ray1 or ray2.b in ray1
    
    else:
        k1 = det(ray2.vec, Vector(ray1.a - ray2.a)) / det
        k2 = - det(ray1.vec, Vector(ray2.a - ray1.a)) / det

        return 0 < k1 and 0 < k2

def line_intersect_segment(line, segment):
    """
    Returns whether a line and a segment intersect.
    """
    det = det(line.vec, segment.vec)
        
    if det == 0:
        return segment.a in line
        
    else: # secant
        k = - det(line.vec, Vector(segment.a - line.a)) / det
        
        return 0 <= k <= 1

def line_intersect_ray(line, ray):
    """
    Returns whether a line and a ray intersect.
    """
    det = det(line.vec, ray.vec)
        
    if det == 0:
        return ray.a in line
        
    else: # secant
        k = - det(line.vec, Vector(ray.a - line.a)) / det
        
        return 0 < k

def line_intersect_line(line1, line2):
    """
    Returns whether two lines intersect.
    """
    return det(line1.vec, line2.vec) != 0 or line2.a in line1

def circle_intersect_segment(circle, segment):
    """
    Returns whether a circle and a segment intersect.
    """
    if segment.a in circle and segment.b in circle:
        return False
    
    u = Vector(circle.center - segment.a)
    u1 = u.project_on(segment.vec)
    u2 = u - u1
    d = u2.lenght
    
    return d <= circle.radius

def circle_intersect_ray(circle, ray):
    """
    Returns whether a circle and a ray intersect.
    """
    u = Vector(circle.center - ray.a)
    u1 = u.project_on(ray.vec)
    u2 = u - u1
    
    return u2.lenght <= circle.radius

def circle_intersect_line(circle, line):
    """
    Returns whether a circle and a line intersect.
    """
    
    dx = line.b.x - line.a.x
    dy = line.b.y - line.a.y
    dr_2 = dx**2 + dy**2
    D = line.a.x * line.b.y - line.b.x * line.a.y
    dis = circle.radius**2 * dr_2 - D**2
    
    return dis >= 0

def circle_intersect_circle(circle1, circle2):
    """
    Returns whether two circles intersect.
    """
    return circle1.center.distance(circle2.center) <= circle1.radius + circle2.radius

# get number of intersections
def count_cicle_inter_segment(circle, segment):
    """
    Returns the number of intersections between a circle and a segment.
    """
    if segment.a in circle and segment.b in circle:
        return Decimal(0)
    
    u = Vector(circle.center - segment.a)
    u1 = u.project_on(segment.vec)
    u2 = u - u1
    d = u2.lenght
    
    if d <= circle.radius:
        if segment.a in circle \
        or segment.b in circle \
        or d == circle.radius:
            return Decimal(1)
        else:
            return Decimal(2)
    
    else:
        return Decimal(0)

def count_cicle_inter_ray(circle, ray):
    """
    Returns the number of intersections between a circle and a ray.
    """
    
    if ray.a in circle:
        return Decimal(1)
    else:
        u = Vector(circle.center - ray.a)
        u1 = u.project_on(ray.vec)
        u2 = u - u1
        d = u2.lenght
        
        if d < circle.radius:
            return Decimal(2)
        elif d == circle.radius:
            return Decimal(1)
        else:
            return Decimal(0)

def count_cicle_inter_line(circle, line):
    """
    Returns the number of intersections between a circle and a line.
    """
    dx = line.b.x - line.a.x
    dy = line.b.y - line.a.y
    dr_2 = dx**2 + dy**2
    D = line.a.x * line.b.y - line.b.x * line.a.y
    dis = circle.radius**2 * dr_2 - D**2
    
    if dis < 0:
        return Decimal(0)
    elif dis == 0:
        return Decimal(1)
    else:
        return Decimal(2)

def count_cicle_inter_circle(circle1, circle2):
    """
    Returns the number of intersections between two cricles.
    """
    d = circle1.center.distance(circle2.center)
    if d > circle1.radius + circle2.radius:
        return Decimal(0)
    if d == circle1.radius + circle2.radius:
        return Decimal(1)
    elif d == 0:
        return Decimal('+Infinity')
    else:
        return Decimal(2)

# get intersection
def get_segment_inter_segment(segment1, segment2):
    """
    Returns the intersection of two segments.
    """
    det = det(segment1.vec, segment2.vec)
        
    if det == 0:
        # overlapping
        intercept1 = segment1.intercept
        intercept2 = segment2.intercept
        if intercept1 == intercept2 \
        or (not intercept1.is_finite() and not intercept2.is_finite()): # if both vertical
            
            first_point = None
            if segment1.a in segment2:
                first_point = segment1.a
            if segment1.b in segment2:
                if first_point:
                    return segment1
                else:
                    first_point = segment1.b
            
            end_point = None
            if segment2.a in segment1:
                end_point = segment2.a
            if segment2.b in segment1:
                if end_point:
                    return segment2
                else:
                    end_point = segment2.b
                    
            if end_point and first_point:
                return type(segment1)(first_point, end_point)
            else:
                return None
            
        # parallel
        else:
            return None
        
    else: # secant
        k1 = det(segment2.vec, Vector(segment1.a - segment2.a)) / det
        k2 = - det(segment1.vec, Vector(segment2.a - segment1.a)) / det

        if 0 <= k1 <= 1 and 0 <= k2 <= 1:
            return segment1.a + k1 * segment1.vec
        else:
            return None

def get_ray_inter_segment(ray, segment):
    """
    Returns the intersection of a ray and a segment.
    """
    det = det(ray.vec, segment.vec)
        
    if det == 0:
        # overlapping
        intercept1 = ray.intercept
        intercept2 = segment.intercept
        if intercept1 == intercept2 \
        or (not intercept1.is_finite() and not intercept2.is_finite()): # if both vertical
            
            first_point = None
            if ray.a in segment:
                first_point = ray.a
            if ray.b in segment:
                if first_point:
                    return ray
                else:
                    first_point = ray.b
            
            end_point = None
            if segment.a in ray:
                end_point = segment.a
            if segment.b in ray:
                if end_point:
                    return segment
                else:
                    end_point = segment.b
                    
            if end_point and first_point:
                return type(segment)(first_point, end_point)
            else:
                return None
            
        # parallel
        else:
            return None
        
    else: # secant
        k1 = det(segment.vec, Vector(ray.a - segment.a)) / det
        k2 = - det(ray.vec, Vector(segment.a - ray.a)) / det

        if 0 <= k1 <= 1 and 0 < k2:
            return ray.a + k1 * ray.vec
        else:
            return None

def get_ray_inter_ray(ray1, ray2):
    """
    Returns the intersection of two rays.
    """
    det = det(ray1.vec, ray2.vec)
        
    if det == 0:
        # overlapping
        if ray1.a in ray2:
            return ray1
        elif ray2.a in ray1:
            return ray2
        # parallel
        else:
            return None
        
    else: # secant
        k1 = det(ray2.vec, Vector(ray1.a - ray2.a)) / det
        k2 = - det(ray1.vec, Vector(ray2.a - ray1.a)) / det

        if 0 < k1 and 0 < k2:
            return ray1.a + k1 * ray1.vec
        else:
            return None

def get_line_inter_segment(line, segment):
    """
    Returns the intersection of a line and a segment.
    """
    det = det(line.vec, segment.vec)
        
    if det == 0:
        # overlapping
        if segment.a in line:
            return segment
        # parallel
        else:
            return None
        
    else: # secant
        k = - det(line.vec, Vector(segment.a - line.a)) / det
        
        if 0 <= k <= 1:
            return segment.a + k * segment.vec
        else:
            return None

def get_line_inter_ray(line, ray):
    """
    Returns the intersection of a line and a ray.
    """
    det = det(line.vec, ray.vec)
        
    if det == 0:
        # overlapping
        if ray.a in line:
            return ray
        # parallel
        else:
            return None
        
    else: # secant
        k = - det(line.vec, Vector(ray.a - line.a)) / det
        
        if 0 < k:
            return ray.a + k * ray.vec
        else:
            return None

def get_line_inter_line(line1, line2):
    """
    Returns the intersection of two lines.
    """
    det = det(line1.vec, line2.vec)
        
    if det != 0:
        k = - det(line1.vec, Vector(line2.a - line1.a)) / det
        return line2.a + k * line2.vec
    
    else:
        if line2.a in line1:
            return line2
        return None

def get_circle_inter_segment(circle, segment):
    """
    Returns the intersection of a circle and a segment.
    """
    if segment.a in circle and segment.b in circle:
        return None
    
    u = Vector(circle.center - segment.a)
    u1 = u.project_on(segment.vec)
    u2 = u - u1
    d = u2.lenght
    
    if d <= circle.radius:
        m = (circle.radius **2 - u2.square_lenght).sqrt()

        if d == circle.radius:
            return segment.a + u1
        
        if segment.a in circle:
            return segment.a + u1 + m * segment.vec.normalize()
        elif segment.b in circle:
            return segment.a + u1 - m * segment.vec.normalize()
        else:
            return (
                segment.a + u1 + m * segment.vec.normalize(),
                segment.a + u1 - m * segment.vec.normalize(),
            )
    
    else:
        return None

def get_circle_inter_ray(circle, ray):
    """
    Returns the intersection of a circle and a ray.
    """ 
    u = Vector(circle.center - ray.a)
    u1 = u.project_on(ray.vec)
    u2 = u - u1
    d = u2.lenght
        
    if d <= circle.radius:
        m = (circle.radius **2 - u2.square_lenght).sqrt()

        if d == circle.radius:
            return ray.a + u1
        elif ray.a in circle:
            return ray.a + u1 + m * ray.vec.normalize()
        else:
            return (
                ray.a + u1 + m * ray.vec.normalize(),
                ray.a + u1 - m * ray.vec.normalize(),
            )
        
    else:
        return None

def get_circle_inter_line(circle, line):
    """
    Returns the intersection of a circle and a line.
    """
    dx = line.b.x - line.a.x
    dy = line.b.y - line.a.y
    dr_2 = dx**2 + dy**2
    D = line.a.x * line.b.y - line.b.x * line.a.y
    dis = circle.radius**2 * dr_2 - D**2
        
    if dis < 0:
        return None
    
    elif dis == 0:
        return Point(
            (D * dy) / dr_2,
            (- D * dx) / dr_2
        )
    
    else:
        p1 = Point(
            (D * dy + sgn(dy) * dx * dis.sqrt()) / dr_2,
            (- D * dx + abs(dy) * dis.sqrt()) / dr_2
        )
        
        p2 = Point(
            (D * dy - sgn(dy) * dx * dis.sqrt()) / dr_2,
            (- D * dx - abs(dy) * dis.sqrt()) / dr_2
        )
        
        return (p1, p2)

def get_circle_inter_circle(circle1, circle2):
    """
    Returns the intersection of two circles.
    """       
    d = circle1.center.distance(circle2.center)
    
    if d == 0:
        return circle1
    elif d > circle1.radius + circle2.radius:
        return None    
    
    else:
        
        # Let two circles centered at (0,0) and (d,0)
        x = (d**2 + circle1.radius**2 - circle2.radius**2) / (Decimal(2) * d)
        
        y_2 = circle1.radius**2 - x**2
        a = Vector(circle2.center - circle1.center).angle(Vector(Decimal(1), Decimal(0)))
        
        # Translate and rotate the intersections to the real position
        if d == (circle1.radius + circle2.radius):
            p = Point(x, y_2.sqrt())
            p.translate(Vector(-circle1.center.x, -circle1.center.y))
            p.rotate(circle1.center, a)
            return p
        
        else: # 2 pts
            p1 = Point(x, y_2.sqrt())
            p1.translate(Vector(-circle1.center.x, -circle1.center.y))
            p1.rotate(circle1.center, a)
            
            p2 = Point(x, -y_2.sqrt())
            p2.translate(Vector(-circle1.center.x, -circle1.center.y))
            p2.rotate(circle1.center, a)
            
            return (p1, p2)
