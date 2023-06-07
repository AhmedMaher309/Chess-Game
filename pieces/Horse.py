import pygame
from util import display

from pieces.Piece import Piece


class Horse(Piece):
    def __init__(self, colour, horse_id, x = 0, y = 0):
        super().__init__(colour, horse_id, x, y)

    def draw_piece(self):
        l = 110
        w = 90
        if self.colour == "black":
            piece_pic = pygame.image.load("images/Horse.bmp")
        elif self.colour == "white":
            piece_pic = pygame.image.load("images/whiteHorse.bmp")
        else:
            piece_pic = pygame.image.load("images/pred.bmp")
            l = 80
            w = 70
        piece_pic = pygame.transform.scale(piece_pic, (l, w))
        display.blit(piece_pic, (self.x, self.y))
        return piece_pic

    def is_selected(self, click_x, click_y):
        return (self.x <= click_x - 10) and (self.x >= click_x - 100) and (self.y <= click_y - 30) \
               and (self.y >= click_y - 100)
