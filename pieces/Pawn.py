import pygame
from util import display

from pieces.Piece import Piece


class Pawn(Piece):
    def __init__(self, colour, pawn_id, x = 0, y = 0):
        super().__init__(colour, pawn_id, x, y)

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
        display.blit(piece_pic, (self.x, self.y))
        return piece_pic

    def update_position(self, x, y):
        self.x = x
        self.y = y



    # def valid_moves(self):
    #  red_pic = pygame.image.load("images\pred.bmp")
    # red_pic = pygame.transform.scale(red_pic, (320, 320))
