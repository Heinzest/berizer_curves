import sys

import pygame
import baseclasses as bc

screen = pygame.display.set_mode((1080, 720))

show = True
mousePos = (0, 0)
i = 0

circleTypes = [
    ((255, 0, 0), 0),
    ((255, 255, 255), 2),
    ((0, 255, 255), 2)
]


def distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5


pointList = [
    bc.Point(100, 500),
    bc.Point(500, 100),
    bc.Point(900, 500),
    bc.Point(500, 500),
]

cubic_bezier = bc.CubicBezier(pointList[0], pointList[1], pointList[2], pointList[3])
chosen_point = -1

while show:

    for events in pygame.event.get():
        if events.type == pygame.MOUSEMOTION:
            if chosen_point != -1:
                mousePos = pygame.mouse.get_pos()
                pointList[chosen_point].set_cord(*mousePos)
        if events.type == pygame.QUIT:
            sys.exit()
        if events.type == pygame.MOUSEBUTTONDOWN:
            mousePos = pygame.mouse.get_pos()
            for x in range(len(pointList)):
                dist = distance(mousePos, pointList[x].get_cord())
                if dist <= 10:
                    chosen_point = x
        if events.type == pygame.MOUSEBUTTONUP:
            chosen_point = -1

    cubic_bezier.show(screen, True)

    i += 1
    pygame.time.wait(40)
    pygame.display.flip()
    screen.fill((0, 0, 0))

    # def mouse_on(self, mouse_pos):
    #     return distance(self.coord, mousePos) <= self.size
    #
    # def show(self, surface):
    #     pygame.draw.circle(surface, circleTypes[self.kind][0], self.coord, self.size, width=circleTypes[self.kind][1])
