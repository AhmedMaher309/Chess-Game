from util import display
from pieces.Squares import Square
from pieces.Horse import Horse


class BlackHorse(Horse):

    def __init__(self, colour, piece_id, x, y):
        self.possibles = []
        super(BlackHorse, self).__init__(colour, piece_id, x, y)

    def set_possible_moves(self, squares, selc_x, selc_y):
        self.possibles.clear()
        for square in squares:
            x, y = square.get_coordinates()
            if (selc_x + 85 < x < selc_x + 170 and selc_y - 210 < y < selc_y - 140) or \
                    (selc_x - 170 <= x <= selc_x - 85 and selc_y - 210 <= y <= selc_y - 140) or \
                    (selc_x - 255 <= x <= selc_x - 170 and selc_y - 140 <= y <= selc_y - 70) or \
                    (selc_x + 170 <= x <= selc_x + 255 and selc_y - 140 <= y <= selc_y - 70) or \
                    (selc_x + 85 <= x <= selc_x + 170 and selc_y + 140 <= y <= selc_y + 210) or \
                    (selc_x - 170 <= x <= selc_x - 85 and selc_y + 140 <= y <= selc_y + 210) or \
                    (selc_x - 255 <= x <= selc_x - 170 and selc_y + 70 <= y <= selc_y + 140) or \
                    (selc_x + 170 <= x <= selc_x + 255 and selc_y + 70 <= y <= selc_y + 140):
                if square.get_piece() is None or (
                        square.get_piece() is not None and square.get_piece().piece_id[0] == 'w'):
                    self.possibles.append(square)

    def set_None(self, squares):
        for square in squares:
            if square.get_piece() == self:
                square.set_piece(None)

    def draw_possible_moves(self, squares, selc_x, selc_y):
        self.set_possible_moves(squares, selc_x, selc_y)
        for move in self.possibles:
            x, y = move.get_coordinates()
            horse = Horse("none", self.piece_id, x, y)
            horse.draw_piece()
            del horse

    def move(self, click_x, click_y, squares):  # move the piece to the square
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

                # print (square.piece.piece_id)

    def see_king(self, squares, my_x, my_y):
        self.set_possible_moves(squares, my_x, my_y)
        for move in self.possibles:
            if move.get_piece() is not None and move.get_piece().piece_id == "wk":
                return True
