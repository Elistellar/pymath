from pymath.geometry.d2.vector import Vector


# intersect ?
def line_intersect_line(line1, line2):
    """
    Return whether two lines intersect.
    """
    return line1.vec.det(line2.vec) != 0 or line2.a in line1

def line_intersect_segment(line, segment):
    """
    Return whether a line and a segment intersect.
    """
    det = line.vec.det(segment.vec)
        
    if det == 0:
        return segment.a in line
        
    else: # secant
        k = - line.vec.det(Vector(segment.a - line.a)) / det
        
        return 0 <= k <= 1
    
def segment_intsersect_segment(segment1, segment2):
    """
    Return whether two segments intersect.
    """
    det = segment1.vec.det(segment2.vec)
        
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
                    return True
                else:
                    first_point = segment1.b
            
            end_point = None
            if segment2.a in segment1:
                end_point = segment2.a
            if segment2.b in segment1:
                if end_point:
                    return True
                else:
                    end_point = segment2.b
                    
            return end_point and first_point
            
        # parallel
        else:
            return False
        
    else: # secant
        k1 = segment2.vec.det(Vector(segment1.a.x - segment2.a.x, segment1.a.y - segment2.a.y)) / det
        k2 = - segment1.vec.det(Vector(segment2.a.x - segment1.a.x, segment2.a.y - segment1.a.y)) / det

        return 0 <= k1 <= 1 and  0 <= k2 <= 1

# get intersection
def get_line_inter_line(line1, line2):
    """
    Return the intersection of two lines.
    """
    det = line1.vec.det(line2.vec)
        
    if det != 0:
        k = - line1.vec.det(Vector(line2.a - line1.a)) / det
        return line2.a + k * line2.vec
    
    else:
        if line2.a in line1:
            return line2
        return None
    
def get_line_inter_segment(line, segment):
    """
    Return the intersection of a line and a segment.
    """
    det = line.vec.det(segment.vec)
        
    if det == 0:
        # overlapping
        if segment.a in line:
            return segment
        # parallel
        else:
            return None
        
    else: # secant
        k = - line.vec.det(Vector(segment.a - line.a)) / det
        
        if 0 <= k <= 1:
            return segment.a + k * segment.vec
        else:
            return None
    
def get_segment_inter_segment(segment1, segment2):
    """
    Return the intersection of two segments.
    """
    det = segment1.vec.det(segment2.vec)
        
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
        k1 = segment2.vec.det(Vector(segment1.a.x - segment2.a.x, segment1.a.y - segment2.a.y)) / det
        k2 = - segment1.vec.det(Vector(segment2.a.x - segment1.a.x, segment2.a.y - segment1.a.y)) / det

        if 0 <= k1 <= 1 and  0 <= k2 <= 1:
            return segment1.a + k1 * segment1.vec
        else:
            return None
