import pygame
from pygame.locals import *
import sys

pygame.init()

class Square:
    def __init__(self,x,y,width,height,piece):
        self.piece = piece
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        #self.image = pygame.image.load("images\pred.bmp")
        #self.rect = self.image.get_rect()
        self.rect = pygame.Rect(x,y,width,height)

    def render(self,display,r,g,b):
        pygame.draw.rect(display,(r,g,b),self.rect)
    
    def set_piece(self,piece):
        self.piece = piece

    def get_piece(self):
       if self.piece != None:
         return self.piece
       else:
           return None
            #print ("NOOOOne")

    def is_selected(self, click_x, click_y):
        return (self.x <= click_x - 10) and (self.x >= click_x - 100) and (self.y <= click_y - 30) \
               and (self.y >= click_y - 100)

    def get_coordinates(self):
        return self.x, self.y


