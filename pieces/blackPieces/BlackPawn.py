from util import display
from pieces.Pawn import Pawn


class BlackPawn(Pawn):

    def __init__(self, colour, piece_id, x, y):
        self.possibles = []
        super(BlackPawn, self).__init__(colour, piece_id, x, y)

    def set_possible_moves(self, squares, selc_x, selc_y):
        self.possibles.clear()
        for square in squares:
            x, y = square.get_coordinates()
            if selc_y - 140 <= y <= selc_y - 70 and x == selc_x:
                if square.get_piece() is None:
                    self.possibles.append(square)
            if (selc_x + 85 <= x <= selc_x + 170 and selc_y - 140 <= y <= selc_y - 70) or \
                    (selc_x - 170 <= x <= selc_x - 85 and selc_y - 140 <= y <= selc_y - 70):
                if square.get_piece() is not None and square.get_piece().piece_id[0] == 'w':
                    self.possibles.append(square)

    def set_None(self, squares):
        for square in squares:
            if square.get_piece() == self:
                square.set_piece(None)

    def draw_possible_moves(self, squares, selc_x, selc_y):
        self.set_possible_moves(squares, selc_x, selc_y)
        for move in self.possibles:
            x, y = move.get_coordinates()
            pawn = Pawn("none", self.piece_id, x, y)
            pawn.draw_piece()
            del pawn

    def move(self, click_x, click_y, squares):
        moves_available = self.possibles
        for move in moves_available:
            x, y = move.get_coordinates()
            if x <= click_x <= x + 85 and y <= click_y <= y + 70:
                self.x = move.x - 10
                self.y = move.y - 15
                self.set_None(squares)
                if move.get_piece() is None:
                    move.set_piece(self)
                else:
                    move.piece.x += 1000
                    move.piece.not_active_piece()
                    move.set_piece(self)

    def see_king(self, squares, my_x, my_y):
        self.set_possible_moves(squares, my_x, my_y)
        for move in self.possibles:
            if move.get_piece() is not None and move.get_piece().piece_id == "wk":
                return True