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
    
    def get_piece(self):
        return self.piece


