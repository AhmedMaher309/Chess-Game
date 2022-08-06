from util import display

from pieces.Pawn import Pawn


class BlackPawn(Pawn):

    def __init__(self, colour, pawn_id, x, y):
        super(BlackPawn, self).__init__(colour, pawn_id, x, y)

    def is_selected(self, click_x, click_y):
        return (self.x <= click_x) and (self.x >= click_x - 100) and (self.y <= click_y + 5) \
               and (self.y >= click_y - 70)

    def draw_possible_moves(self):
        pawn = Pawn("none", self.piece_id, self.x + 18, self.y - 60)
        pawn.draw_piece()
        del pawn

    def move(self, click_x, click_y):
        if click_y == self.y or (self.y + 5 >= click_y >= self.y - 70):
            self.y = self.y - 73
