import pygame
from pygame.locals import *
import sys
pygame.init()

class Piece:
    
    def __init__(self,colour):
        self.id
        self.peice_colour = colour
        self.is_active = 1
        self.x = 0
        self.y = 0

    def is_actuve(self):
        if self.is_active ==1:
            return 1
        else:
            return 0

    def not_active_peice(self):
        self.is_active = 0

    def set_coordinates(self,x_pos,y_pos):
        self.x =x_pos
        self.y =y_pos
        return self.x,self.y



