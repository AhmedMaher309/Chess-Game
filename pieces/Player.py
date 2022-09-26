import pygame
from pygame.locals import *
import sys


class Player:
    def __init__(self, turn, win_lose):
        self.MyTurn = turn
        self.win_lose = win_lose

    def SetTurn(self):
        self.MyTurn = 1

    def ResetTurn(self):
        self.MyTurn = 0

    def GetTurn(self):
        return self.MyTurn

    def SetWin(self):
        self.win_lose = 1

    def GetWIn(self):
        return self.win_lose
