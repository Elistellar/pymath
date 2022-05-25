class Point:
    
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def __repr__(self):
        return f'Point({self.__x}, {self.__y})'
    
    # attrs
    @property
    def x(self):
        return self.__x
    
    @property
    def y(self):
        return self.__y
    
    # op
    def __add__(self, other):
        return Point(self.__x + other.x, self.__y + other.y)
    
    def __sub__(self, other):
        return Point(self.__x - other.x, self.__y - other.y)
