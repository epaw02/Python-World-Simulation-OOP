import pygame
from itertools import product
class Board:
    def __init__(self, w, scr):
        self.world=w
        self.screen=scr
    
    def paint(self):
        org=self.world.get_organism()
        width=self.world.get_n()
        height=self.world.get_m()
        sizex = 500 / width
        sizey = 500 / height
        color=(250,250,250)
        sx=500 % sizex
        sy=500 % sizey
        sx=int(sx)
        sy=int(sy)
        for obj in org:
            x=obj.get_x()
            y=obj.get_y()
            c=obj.color()
            for xx, yy in product(range(500 - sx), range(500 - sy)):
                if x == (xx / sizex) and y == (yy / sizey):
                    pygame.draw.rect(self.screen, c, pygame.Rect(xx, yy, sizex, sizey))


