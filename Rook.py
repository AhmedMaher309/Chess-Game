import pygame
from pygame.locals import *
import sys
pygame.init()

from Peices import Piece

class Rook(Piece):
   def __init__(self,colour,id):
       self.rook_colour=colour
       self.id = id
       self.is_active = 1

   def draw_peice(self):
       l=110
       w=90
       if self.rook_colour=="black":
           piece_pic = pygame.image.load("images\BlackRook.bmp")
       elif self.rook_colour=="white":
            piece_pic = pygame.image.load("images\WhiteRook.bmp")
       else:
            piece_pic = pygame.image.load("images\pred.bmp")
            l=80
            w=70
       piece_pic = pygame.transform.scale(piece_pic, (l, w))
       return piece_pic
 
   def update_position(self,x,y):
       self.x = x
       self.y = y

