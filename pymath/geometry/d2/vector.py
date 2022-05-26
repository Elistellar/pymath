def _det(v1, v2):
    return v1.x * v2.y - v1.y * v2.x

class Vector:
    
    def __init__(self, x, y = None):
        if y:
            self.__x = x
            self.__y = y
        else:
            self.__x, self.__y = x.x, x.y
    
    def __repr__(self):
        return f'Vector({self.__x}, {self.__y})'
    
    # attrs
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    @property
    def lenght(self):
        return (self.__x ** 2 + self.__y ** 2).sqrt()
    
    # methods
    def normalize(self):
        return 1 / self.lenght * self
    
    def det(self, other):
        return self.__x * other.__y - self.__y * other.__x

    # op
    def __add__(self, other):
        return Vector(self.__x + other.x, self.__y + other.y)
    
    def __sub__(self, other):
        return Vector(self.__x - other.x, self.__y - other.y)
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            return self.__x * other.__x + self.__y * other.__y
        
        return Vector(self.__x * other, self.__y * other)
    
    def __rmul__(self, other):
        return Vector(self.__x * other, self.__y * other)

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y
