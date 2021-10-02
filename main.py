import pygame
import sys

screen = pygame.display.set_mode((1080, 720))

show = True
mousePos = (0, 0)
i = 0
intervals = 40

circleTypes = [
    ((255, 0, 0), 0),
    ((255, 255, 255), 2),
    ((0, 255, 255), 2)
]


def distance(point1, point2):
    return ((point1.x - point2.y) ** 2 + (point1.x - point2.y) ** 2) ** 0.5


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

    def __init__(self, point0, point1, point2):
        self.point0 = point0
        self.point1 = point1
        self.point2 = point2

    def quadratic_bezier(self):
        line0 = Line(self.point0, self.point1)
        line1 = Line(self.point1, self.point2)
        point_list = []
        for x in range(intervals + 1):
            curve_point = (x % (intervals + 1)) / intervals
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
        for x in range(intervals):
            Line(point_list[x], point_list[x + 1]).show(surface)


class CubicBezier:
    point0 = Point(0, 0)
    point1 = Point(0, 0)
    point2 = Point(0, 0)
    point3 = Point(0, 0)

    def __init__(self, point0, point1, point2, point3):
        self.point0 = point0
        self.point1 = point1
        self.point2 = point2
        self.point3 = point3

    def cubic_bezier(self):
        bezier0 = QuadraticBezier(self.point0, self.point1, self.point2).quadratic_bezier()
        bezier1 = QuadraticBezier(self.point1, self.point2, self.point3).quadratic_bezier()

        point_list = []
        for x in range(intervals + 1):
            curve_point = (x % (intervals + 1)) / intervals
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
        for x in range(intervals):
            Line(point_list[x], point_list[x + 1]).show(surface)


pointList = [
    Point(100, 500),
    Point(500, 100),
    Point(500, 500),
    Point(900, 500),
]

cubic_bezier = CubicBezier(pointList[0], pointList[1], pointList[2], pointList[3])

while show:

    for events in pygame.event.get():
        # if events.type == pygame.MOUSEMOTION:
        #     mousePos = pygame.mouse.get_pos()
        #     smallest_dist, smallest_dist_index = 20, -1
        #     for x in range(len(pointList)):
        #         if pointList[x].kind == 2:
        #             pointList[x].kind = 0
        #         if pointList[x].kind == 0:
        #             temp_dist = distance(mousePos, pointList[x].coord)
        #             if temp_dist <= smallest_dist:
        #                 smallest_dist = temp_dist
        #                 smallest_dist_index = x
        #     if smallest_dist <= pointList[smallest_dist_index].size:
        #         pointList[smallest_dist_index].kind = 2
        if events.type == pygame.QUIT:
            sys.exit()
        #if events.type == pygame.MOUSEBUTTONDOWN:
            #mousePos = pygame.mouse.get_pos()


    pointList[0].show(screen)
    cubic_bezier.show(screen, True)

    i += 1

    pygame.time.wait(150)

    pygame.display.flip()
    screen.fill((0, 0, 0))

    # def mouse_on(self, mouse_pos):
    #     return distance(self.coord, mousePos) <= self.size
    #
    # def show(self, surface):
    #     pygame.draw.circle(surface, circleTypes[self.kind][0], self.coord, self.size, width=circleTypes[self.kind][1])
