import pygame


class Point:
    x = 100
    y = 100

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_cord(self, x, y):
        self.x = x
        self.y = y

    def get_cord(self):
        return self.x, self.y

    def show(self, surface):
        pygame.draw.circle(surface, (200, 200, 200), self.get_cord(), 5)


class Line:
    point0 = Point(100, 100)
    point1 = Point(100, 100)

    def __init__(self, point0, point1):
        self.point0 = point0
        self.point1 = point1

    def subpoint(self, t):
        x_c = self.point0.x + (self.point1.x - self.point0.x) * t
        y_c = self.point0.y + (self.point1.y - self.point0.y) * t
        return x_c, y_c

    def show(self, surface):
        pygame.draw.line(surface, (200, 200, 200), self.point0.get_cord(), self.point1.get_cord(), 2)


class QuadraticBezier:
    point0 = Point(0, 0)
    point1 = Point(0, 0)
    point2 = Point(0, 0)
    intervals = 1

    def __init__(self, point0, point1, point2, intervals=50):
        self.point0 = point0
        self.point1 = point1
        self.point2 = point2
        self.intervals = intervals

    def quadratic_bezier(self):
        line0 = Line(self.point0, self.point1)
        line1 = Line(self.point1, self.point2)
        point_list = []
        for x in range(self.intervals + 1):
            curve_point = (x % (self.intervals + 1)) / self.intervals
            p0 = line0.subpoint(curve_point)
            p1 = line1.subpoint(curve_point)
            point_list.append(Point(*Line(Point(*p0), Point(*p1)).subpoint(curve_point)))
        return point_list

    def show(self, surface, outer):
        if outer:
            Line(self.point0, self.point1).show(surface)
            Line(self.point1, self.point2).show(surface)
            self.point0.show(surface)
            self.point1.show(surface)
            self.point2.show(surface)
        point_list = self.quadratic_bezier()
        for x in range(self.intervals):
            Line(point_list[x], point_list[x + 1]).show(surface)


class CubicBezier:
    point0 = Point(0, 0)
    point1 = Point(0, 0)
    point2 = Point(0, 0)
    point3 = Point(0, 0)
    intervals = 1

    def __init__(self, point0, point1, point2, point3, intervals=50):
        self.point0 = point0
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3
        self.intervals = intervals

    def cubic_bezier(self):
        bezier0 = QuadraticBezier(self.point0, self.point1, self.point2).quadratic_bezier()
        bezier1 = QuadraticBezier(self.point1, self.point2, self.point3).quadratic_bezier()

        point_list = []
        for x in range(self.intervals + 1):
            curve_point = (x % (self.intervals + 1)) / self.intervals
            line0 = Line(bezier0[x], bezier1[x])
            p0 = line0.subpoint(curve_point)

            point_list.append(Point(*p0))
        return point_list

    def show(self, surface, outer):
        if outer:
            Line(self.point0, self.point1).show(surface)
            Line(self.point2, self.point3).show(surface)
            self.point0.show(surface)
            self.point1.show(surface)
            self.point2.show(surface)
            self.point3.show(surface)
        point_list = self.cubic_bezier()
        for x in range(self.intervals):
            Line(point_list[x], point_list[x + 1]).show(surface)
