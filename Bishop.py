import pygame
from pygame.locals import *
import sys
pygame.init()

from Pieces import Piece

class Bishop(Piece):
   def __init__(self,colour, bishop_id):
       super().__init__(colour, bishop_id)

   def draw_piece(self):
       l=110
       w=90
       if self.colour == "black":
           piece_pic = pygame.image.load("images\BlackBishop.bmp")
       elif self.colour == "white":
            piece_pic = pygame.image.load("images\WhiteBishop.bmp")
       else:
            piece_pic = pygame.image.load("images\pred.bmp")
            l=80
            w=70
       piece_pic = pygame.transform.scale(piece_pic, (l, w))
       return piece_pic
 
   def update_position(self,x,y):
       self.x = x
       self.y = y
