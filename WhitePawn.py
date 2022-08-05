from Pawn import Pawn


class WhitePawn(Pawn):

    def __init__(self, colour, pawn_id):
        super(WhitePawn, self).__init__(colour, pawn_id)

    def is_selected(self, click_x, click_y):
        return click_x >= self.x >= click_x - 100 and click_y - 20 >= self.y >= click_y - 100
