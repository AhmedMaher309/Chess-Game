import pygame
from pygame.locals import *
import sys
pygame.init()

from Peices import Piece

class Horse(Piece):
   def __init__(self,colour,id):
       self.horse_colour=colour
       self.id = id
       self.is_active =1

   def draw_peice(self):
        l=110
        w=90
        if self.horse_colour=="black":
           piece_pic = pygame.image.load("images\Horse.bmp")
        elif self.horse_colour =="white":
            piece_pic = pygame.image.load("images\whiteHorse.bmp")
        else:
            piece_pic = pygame.image.load("images\pred.bmp")
            l=80
            w=70
        piece_pic = pygame.transform.scale(piece_pic, (l, w))
        return piece_pic
