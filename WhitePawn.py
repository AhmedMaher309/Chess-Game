from util import display

from Pawn import Pawn


class WhitePawn(Pawn):

    def __init__(self, colour, pawn_id, x, y):
        super(WhitePawn, self).__init__(colour, pawn_id, x, y)

    def is_selected(self, click_x, click_y):
        return click_x >= self.x >= click_x - 100 and click_y - 20 >= self.y >= click_y - 100

    def draw_possible_moves(self):
        pawn = Pawn("none", self.piece_id, self.x + 18, self.y + 90)
        pawn.draw_piece()

    def move(self, click_x, click_y):
        if click_y == self.y or (self.y + 5 <= click_y <= self.y + 160):
            self.y = self.y + 73
