from util import display

from Horse import Horse

class WhiteHorse(Horse):

    def __init__(self, colour, piece_id):
        super(WhiteHorse, self).__init__(colour, piece_id)

    def draw_possible_moves(self):
        horse = Horse("none", self.piece_id)
        display.blit(horse.draw_piece(), (horse.set_coordinates(self.x + 105, self.y + 160)))
        display.blit(horse.draw_piece(), (horse.set_coordinates(self.x - 73, self.y + 160)))