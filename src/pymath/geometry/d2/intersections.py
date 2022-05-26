from pymath.geometry.d2.vector import Vector, det


__all__ = [
    'segment_intersect_segment',
    'ray_intersect_segment',
    'ray_intersect_ray',
    'line_intersect_segment',
    'line_intersect_ray',
    'line_intersect_line',
    
    'get_segment_inter_segment',
    'get_ray_inter_segment',
    'get_ray_inter_ray',
    'get_line_inter_segment', 
    'get_line_inter_ray',
    'get_line_inter_line',
]

# intersect ?
def segment_intersect_segment(segment1, segment2):
    """
    Return whether two segments intersect.
    """
    det = det(segment1.vec, segment2.vec)
        
    if det == 0:
        # overlapping
        return segment1.a in segment2 or segment1.b in segment2 \
            or segment2.a in segment1 or segment2.b in segment1
        
    else: # secant
        k1 = det(segment2.vec, Vector(segment1.a - segment2.a)) / det
        k2 = - det(segment1.vec, Vector(segment2.a - segment1.a)) / det

        return 0 <= k1 <= 1 and  0 <= k2 <= 1

def ray_intersect_segment(ray, segment):
    """
    Return whether a ray and a segment intersect.
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
    Return whether two rays intersect.
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
    Return whether a line and a segment intersect.
    """
    det = det(line.vec, segment.vec)
        
    if det == 0:
        return segment.a in line
        
    else: # secant
        k = - det(line.vec, Vector(segment.a - line.a)) / det
        
        return 0 <= k <= 1

def line_intersect_ray(line, ray):
    """
    Return whether a line and a ray intersect.
    """
    det = det(line.vec, ray.vec)
        
    if det == 0:
        return ray.a in line
        
    else: # secant
        k = - det(line.vec, Vector(ray.a - line.a)) / det
        
        return 0 < k

def line_intersect_line(line1, line2):
    """
    Return whether two lines intersect.
    """
    return det(line1.vec, line2.vec) != 0 or line2.a in line1

# get intersection
def get_segment_inter_segment(segment1, segment2):
    """
    Return the intersection of two segments.
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
    Return the intersection of a ray and a segment.
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
    Return the intersection of two rays.
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
    Return the intersection of a line and a segment.
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
    Return the intersection of a line and a ray.
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
    Return the intersection of two lines.
    """
    det = det(line1.vec, line2.vec)
        
    if det != 0:
        k = - det(line1.vec, Vector(line2.a - line1.a)) / det
        return line2.a + k * line2.vec
    
    else:
        if line2.a in line1:
            return line2
        return None
