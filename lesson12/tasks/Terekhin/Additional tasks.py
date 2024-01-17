import math


class Dot:
    def __init__(self, x, y, z):  # Координат точки
        self.x = x
        self.y = y
        self.z = z


class Line:
    def __init__(self, x1, y1, z1, x2, y2, z2):  # Прямая по координатам двух точек
        self.x1 = x1
        self.y1 = y1
        self.z1 = z1
        self.x2 = x2
        self.y2 = y2
        self.z2 = z2

        self.x = self.x2 - self.x1
        self.y = self.y2 - self.y1
        self.z = self.z2 - self.z1


class Plane:
    def __init__(self, a, b, c, d):  # Плоскость по коэффициентам уравнения ax + by + cz + d = 0
        self.a = a
        self.b = b
        self.c = c
        self.d = d


def distance_p_d(plane, dot):
    a = plane.a
    b = plane.b
    c = plane.c
    d = plane.d
    x = dot.x
    y = dot.y
    z = dot.z
    d = math.fabs(a * x + b * y + c * z + d) / math.sqrt(a ** 2 + b ** 2 + c ** 2)
    return d


def corner_p_l(plane, line):
    a = plane.a
    b = plane.b
    c = plane.c
    x = line.x
    y = line.y
    z = line.z
    corner = math.fabs((x*a + y*b + z*c)/(math.sqrt(x**2 + y**2 + z**2) * math.sqrt(a**2 + b**2 + c**2)))
    return math.degrees(min(math.asin(corner), math.acos(corner)))


def corner_l1_l2(line1, line2):
    x1 = line1.x
    y1 = line1.y
    z1 = line1.z
    x2 = line2.x
    y2 = line2.y
    z2 = line2.z
    corner = math.fabs(x1*x2 + y1*y2 + z1*z2)/(math.sqrt(x1**2 + y1**2 + z1**2) * math.sqrt(x2**2 + y2**2 + z2**2))
    return math.degrees(math.acos(corner))


line1 = Line(5, 5, 0, 0, 0, 0)
line2 = Line(5, 0, 0, 0, 0, 0)
print(corner_l1_l2(line1, line2))
line3 = Line(0, 5, 0, 0, 0, 0)
line4 = Line(5, 0, 0, 0, 0, 0)
print(corner_l1_l2(line3, line4))


def corner_p1_p2(plane1, plane2):
    a1 = plane1.a
    b1 = plane1.b
    c1 = plane1.c
    a2 = plane2.a
    b2 = plane2.b
    c2 = plane2.c
    corner = math.fabs(a1*a2 + b1*b2 + c1*c2)/(math.sqrt(a1**2 + b1**2 + c1**2) * math.sqrt(a2**2 + b2**2 + c2**2))
    return math.degrees(math.acos(corner))
