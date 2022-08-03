import pygame
from pygame.locals import *
import sys
pygame.init()

from Peices import Piece

class Pawn(Piece):
   def __init__(self,colour,id):
       self.pawn_colour=colour
       self.id = id
       self.is_active = 1

   def draw_peice(self):
       l=120
       w=100
       if self.pawn_colour=="black":
           piece_pic = pygame.image.load("images\pawn.bmp")
       elif self.pawn_colour=="white":
            piece_pic = pygame.image.load("images\whitePawn.bmp")
       else:
            piece_pic = pygame.image.load("images\pred.bmp")
            l=80
            w=70
       piece_pic = pygame.transform.scale(piece_pic, (l, w))
       return piece_pic
 
   def update_position(self,x,y):
       self.x = x
       self.y = y


  # def valid_moves(self):
      #  red_pic = pygame.image.load("images\pred.bmp")
       # red_pic = pygame.transform.scale(red_pic, (320, 320))