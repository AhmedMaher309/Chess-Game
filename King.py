import pygame
from pygame.locals import *
import sys
pygame.init()

from util import display
from Piece import Piece


class King(Piece):
   def __init__(self, colour, king_id, x, y):
       super().__init__(colour, king_id, x, y)

   def draw_piece(self):
       l=120
       w=90
       if self.colour == "black":
            piece_pic = pygame.image.load("images\BlackKing.bmp")
       elif self.colour == "white":
            piece_pic = pygame.image.load("images\WhiteKing.bmp")
       else:
            piece_pic = pygame.image.load("images\pred.bmp")
            l=80
            w=70
       piece_pic = pygame.transform.scale(piece_pic, (l, w))
       display.blit(piece_pic, (self.x, self.y))
       return piece_pic

   def update_position(self,x,y):
       self.x = x
       self.y = y


