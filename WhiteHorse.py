from util import display

from Horse import Horse

class WhiteHorse(Horse):

    def __init__(self, colour, piece_id, x, y):
        super(WhiteHorse, self).__init__(colour, piece_id, x, y)

    def draw_possible_moves(self):
        horse = Horse("none", self.piece_id, self.x + 105, self.y + 160)
        horse.draw_piece()
        horse.set_coordinates(self.x - 73, self.y + 160)
        horse.draw_piece()
        del horse

    def move(self, click_x, click_y):
        # TODO - to be implemented
        return None