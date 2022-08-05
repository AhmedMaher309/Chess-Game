from util import display

from Horse import Horse

class BlackHorse(Horse):

    def __init__(self, colour, piece_id):
        super(BlackHorse, self).__init__(colour, piece_id)

    def draw_possible_moves(self):
        horse = Horse("none", self.piece_id)
        display.blit(horse.draw_piece(), (horse.set_coordinates(self.x + 105, self.y - 130)))
        display.blit(horse.draw_piece(), (horse.set_coordinates(self.x - 70, self.y - 130)))