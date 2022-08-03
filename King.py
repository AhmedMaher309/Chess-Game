import pygame
from pygame.locals import *
import sys
pygame.init()

from Peices import Piece

class King(Piece):
   def __init__(self,colour,id):
       self.king_colour=colour
       self.id = id
       self.is_active = 1

   def draw_peice(self):
       l=120
       w=90
       if self.king_colour=="black":
            piece_pic = pygame.image.load("images\BlackKing.bmp")
       elif self.king_colour=="white":
            piece_pic = pygame.image.load("images\WhiteKing.bmp")
       else:
            piece_pic = pygame.image.load("images\pred.bmp")
            l=80
            w=70
       piece_pic = pygame.transform.scale(piece_pic, (l, w))
       return piece_pic
 
   def update_position(self,x,y):
       self.x = x
       self.y = y


