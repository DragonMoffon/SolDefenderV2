class Vec2:

    def __init__(self, x, y=None):
        self.values = (x, x) if y is None else (x, y)

    def dot(self, other):
        return self.x*other.x + self.y*other.y

    def cross(self, other):
        if isinstance(other, Vec2):
            return self.x*other.y-self.y*other.x
        else:
            return Vec2(other * self.y, -other * self.x)

    def cross_left(self, other):
        return Vec2(-other * self.y, other * self.x)

    @property
    def x(self):
        return self.values[0]

    @x.setter
    def x(self, value):
        self.values = (value, self.y)

    @property
    def y(self):
        return self.values[1]

    @y.setter
    def y(self, value):
        self.values = (self.x, value)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Vec2({self.x}, {self.y})"

    def __mul__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x*other.x, self.y*other.y)
        else:
            return Vec2(self.x*other, self.y*other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __add__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x+other.x, self.y+other.y)
        else:
            return Vec2(self.x+other, self.y+other)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, Vec2):
            return Vec2(self.x - other.x, self.y - other.y)
        else:
            return Vec2(self.x - other, self.y - other)

    def __rsub__(self, other):
        if isinstance(other, Vec2):
            return Vec2(other.x - self.x, other.y - self.y)
        else:
            return Vec2(other - self.x, other - self.y)