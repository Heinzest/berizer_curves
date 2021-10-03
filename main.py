import sys
import math

import pygame
import baseclasses as bc

screen = pygame.display.set_mode((1080, 720))

show = True
mousePos = (0, 0)
iteration = 0


def distance(point0, point1):
    return ((point0[0] - point1[0]) ** 2 + (point0[1] - point1[1]) ** 2) ** 0.5


def points_move(selected_point, mouse_pos, m_type):
    current_point = pointList[chosen_point].get_cord()
    offset = (mouse_pos[0]-current_point[0], mouse_pos[1]-current_point[1])
    # Left mouse button
    if m_type == 1:
        # Red point
        if pointList[selected_point].view == 0:
            if selected_point != 0:
                pointList[chosen_point-1].set_cord(offset_x=offset[0], offset_y=offset[1])
            pointList[chosen_point].set_cord(*mouse_pos)
            if selected_point != len(pointList)-1:
                pointList[chosen_point+1].set_cord(offset_x=offset[0], offset_y=offset[1])
        # White point
        else:
            anchor = chosen_point - 1 if pointList[chosen_point-1].view == 0 else chosen_point + 1
            second_point = chosen_point - 2 if pointList[chosen_point-1].view == 0 else chosen_point + 2
            second_point_distance = distance(pointList[anchor].get_cord(), pointList[second_point].get_cord())
            pointList[chosen_point].set_cord(*mouse_pos)
            cp_cord = pointList[chosen_point].get_cord()
            an_cord = pointList[anchor].get_cord()
            cp_dist = distance(cp_cord, an_cord)
            ofs = cp_cord[0]-an_cord[0], cp_cord[1]-an_cord[1]
            ofs = ofs[0]*(second_point_distance/cp_dist), ofs[1]*(second_point_distance/cp_dist)
            pointList[second_point].set_cord(x=an_cord[0], y=an_cord[1], offset_x=-ofs[0], offset_y=-ofs[1])
    # Right mouse button
    if m_type == 3:
        pointList[chosen_point].set_cord(*mouse_pos)
    return


pointList = [
    bc.Point(100, 300),
    bc.Point(200, 300, 0),
    bc.Point(300, 300),
    bc.Point(600, 400),
    bc.Point(500, 500, 0),
    bc.Point(400, 600),
    bc.Point(300, 700),
    bc.Point(400, 700, 0),
    bc.Point(500, 700),
]

bezierList = [
    bc.CubicBezier(pointList[1], pointList[2], pointList[3], pointList[4]),
    bc.CubicBezier(pointList[4], pointList[5], pointList[6], pointList[7])
]
chosen_point = -1
mouse_type = -1

while show:

    for events in pygame.event.get():
        if events.type == pygame.MOUSEMOTION:
            if chosen_point != -1:
                mousePos = pygame.mouse.get_pos()
                points_move(chosen_point, mousePos, mouse_type)
        elif events.type == pygame.MOUSEBUTTONDOWN:
            mouse_type = events.button
            print(mouse_type)
            mousePos = pygame.mouse.get_pos()
            for x in range(len(pointList)):
                dist = distance(mousePos, pointList[x].get_cord())
                if dist <= 10:
                    chosen_point = x
        elif events.type == pygame.MOUSEBUTTONUP:
            chosen_point = -1
            mouse_type = -1
        elif events.type == pygame.QUIT:
            print("quit")
            sys.exit()

    for x in range(len(pointList)):
        if pointList[x].view == 0:
            bc.Line(pointList[x], pointList[x + 1]).show(screen)
            bc.Line(pointList[x], pointList[x - 1]).show(screen)
        pointList[x].show(screen)
    for x in bezierList:
        x.show(screen)
    pointList[0].show(screen)
    pointList[-1].show(screen)

    iteration += 1
    pygame.time.wait(40)
    pygame.display.flip()
    screen.fill((10, 10, 10))

    # def mouse_on(self, mouse_pos):
    #     return distance(self.coord, mousePos) <= self.size
