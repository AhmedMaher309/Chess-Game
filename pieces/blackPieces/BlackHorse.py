from util import display
from pieces.Squares import Square
from pieces.Horse import Horse
 

class BlackHorse(Horse):

    def __init__(self, colour, piece_id, x, y):
        super(BlackHorse, self).__init__(colour, piece_id, x, y)

    def draw_possible_moves(self):
        horse = Horse("none", self.piece_id, self.x + 105, self.y - 130)
        horse.draw_piece()
        horse.set_coordinates(self.x - 70, self.y - 130)
        horse.draw_piece()
        horse.set_coordinates(self.x - 160, self.y - 58)
        horse.draw_piece()
        horse.set_coordinates(self.x + 193, self.y - 58)
        horse.draw_piece()
        horse.set_coordinates(self.x - 160, self.y + 85)
        horse.draw_piece()
        horse.set_coordinates(self.x + 193, self.y + 85)
        horse.draw_piece()
        del horse

    def move(self, click_x, click_y):
        if click_y == self.y or (self.y - 90 >= click_y >= self.y - 130):
            if click_x == self.x or (self.x + 180 >= click_x >= self.x + 90):
                self.y = self.y - 145
                self.x = self.x + 90
            elif click_x <= self.x + 10:
                self.y = self.y - 145
                self.x = self.x - 90