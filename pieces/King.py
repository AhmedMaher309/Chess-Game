import pygame
from pygame.locals import *
import sys

pygame.init()

from util import display
from pieces.Piece import Piece


class King(Piece):
    def __init__(self, colour, king_id, x, y):
        self.piece_pic = pygame.image.load("images/BlackKing.bmp")
        self.is_checked = 0
        super().__init__(colour, king_id, x, y)

    def draw_piece(self):
        l = 120
        w = 90
        c = 0
        d = 0
        if self.colour == "black":
            self.piece_pic = pygame.image.load("images/BlackKing.bmp")
        elif self.colour == "white" and self.is_checked == 0:
            self.piece_pic = pygame.image.load("images/WhiteKing.bmp")
        elif self.colour == "white" and self.is_checked == 1:
            self.piece_pic = pygame.image.load("images/checked_white.bmp")
            l = 85
            w = 73
            c = 13
            d = 10
        else:
            self.piece_pic = pygame.image.load("images/pred.bmp")
            l = 80
            w = 70
        piece_pic = pygame.transform.scale(self.piece_pic, (l, w))
        display.blit(piece_pic, (self.x + c, self.y + d))
        return piece_pic

    def update_position(self, x, y):
        self.x = x
        self.y = y
