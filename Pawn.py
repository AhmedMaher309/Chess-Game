import pygame
from pygame.locals import *
import sys

pygame.init()

from Pieces import Piece


class Pawn(Piece):
    def __init__(self, colour, pawn_id):
        super().__init__(colour, pawn_id)

    def draw_piece(self):
        l = 120
        w = 100
        if self.colour == "black":
            piece_pic = pygame.image.load("images\pawn.bmp")
        elif self.colour == "white":
            piece_pic = pygame.image.load("images\whitePawn.bmp")
        else:
            piece_pic = pygame.image.load("images\pred.bmp")
            l = 80
            w = 70
        piece_pic = pygame.transform.scale(piece_pic, (l, w))
        return piece_pic

    def update_position(self, x, y):
        self.x = x
        self.y = y

    def is_selected(self, click_x, click_y):
        return (self.x <= click_x) and (self.x >= click_x - 100) and (self.y <= click_y + 5)\
               and (self.y >= click_y - 70)

# def valid_moves(self):
#  red_pic = pygame.image.load("images\pred.bmp")
# red_pic = pygame.transform.scale(red_pic, (320, 320))
