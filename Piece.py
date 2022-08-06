import pygame
from pygame.locals import *
import sys

pygame.init()


class Piece:

    def __init__(self, colour, piece_id, x, y):
        self.piece_id = piece_id
        self.colour = colour
        self.is_active = 1
        self.x = x
        self.y = y

    def is_active(self):
        if self.is_active == 1:
            return 1
        else:
            return 0

    def not_active_piece(self):
        self.is_active = 0

    def set_coordinates(self, x_pos, y_pos):
        self.x = x_pos
        self.y = y_pos
        return self.x, self.y

    def is_selected(self, click_x, click_y):
        return False
