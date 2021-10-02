import sys

import pygame
import baseclasses as bc

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


pointList = [
    bc.Point(100, 500),
    bc.Point(500, 100),
    bc.Point(500, 500),
    bc.Point(900, 500),
]

cubic_bezier = bc.CubicBezier(pointList[0], pointList[1], pointList[2], pointList[3])

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
