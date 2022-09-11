from util import display
from pieces.Squares import Square
from pieces.Queen import Queen 

class WhiteQueen(Queen):
   def __init__(self, colour, piece_id, x, y):
        self.possibles = []
        super(WhiteQueen, self).__init__(colour, piece_id, x, y)

   def draw_possible_moves(self, squares, selc_x, selc_y):
        sx = selc_x
        sy = selc_y
        for square in squares:
            x, y = square.get_coordinates()
            if sx + 85 < x < sx + 170 and sy - 140 < y < sy - 70:
                if square.get_piece() is None:
                    queen = Queen("none", self.piece_id, x, y)
                    queen.draw_piece()
                    del queen
                    self.possibles.append(square)
                    sx = x
                    sy = y
                elif square.get_piece() is not None and square.get_piece().piece_id[0] == 'b':
                    queen = Queen("none", self.piece_id, x, y)
                    queen.draw_piece()
                    del queen
                    self.possibles.append(square)
                    break
                elif square.get_piece() is not None and square.get_piece().piece_id[0] == 'w':
                    break
        sx = selc_x
        sy = selc_y
        for square in squares:
            x, y = square.get_coordinates()
            if sx - 170 < x < sx - 85 and sy - 140 < y < sy - 70:
                if square.get_piece() is None:
                    queen = Queen("none", self.piece_id, x, y)
                    queen.draw_piece()
                    del queen
                    self.possibles.append(square)
                    sx = x
                    sy = y
                elif square.get_piece() is not None and square.get_piece().piece_id[0] == 'b':
                    queen = Queen("none", self.piece_id, x, y)
                    queen.draw_piece()
                    del queen
                    self.possibles.append(square)
                    break
                elif square.get_piece() is not None and square.get_piece().piece_id[0] == 'w':
                    break
        sx = selc_x
        sy = selc_y
        for square in reversed(squares):
            x, y = square.get_coordinates()
            if sx + 85 <= x <= sx + 170 and sy + 70 < y < sy + 140:
                if square.get_piece() is None:
                    queen = Queen("none", self.piece_id, x, y)
                    queen.draw_piece()
                    del queen
                    self.possibles.append(square)
                    sx = x
                    sy = y
                elif square.get_piece() is not None and square.get_piece().piece_id[0] == 'b':
                    queen = Queen("none", self.piece_id, x, y)
                    queen.draw_piece()
                    del queen
                    self.possibles.append(square)
                    break
                elif square.get_piece() is not None and square.get_piece().piece_id[0] == 'w':
                    break
        sx = selc_x
        sy = selc_y
        for square in reversed(squares):
            x, y = square.get_coordinates()
            if sx - 170 <= x <= sx - 85 and sy + 70 < y < sy + 140:
                if square.get_piece() is None:
                    queen = Queen("none", self.piece_id, x, y)
                    queen.draw_piece()
                    del queen
                    self.possibles.append(square)
                    sx = x
                    sy = y
                elif square.get_piece() is not None and square.get_piece().piece_id[0] == 'b':
                    queen = Queen("none", self.piece_id, x, y)
                    queen.draw_piece()
                    del queen
                    self.possibles.append(square)
                    break
                elif square.get_piece() is not None and square.get_piece().piece_id[0] == 'w':
                    break
        sy = selc_y
        sx = selc_x
        for square in squares:
            x, y = square.get_coordinates()
            if sx == x and sy - 140 < y < sy - 70:
                if square.get_piece() is None:
                    queen = Queen("none", self.piece_id, x, y)
                    queen.draw_piece()
                    del queen
                    self.possibles.append(square)
                    sy = y
                elif square.get_piece() is not None and square.get_piece().piece_id[0] == 'b':
                    queen = Queen("none", self.piece_id, x, y)
                    queen.draw_piece()
                    del queen
                    self.possibles.append(square)
                    break
                elif square.get_piece() is not None and square.get_piece().piece_id[0] == 'w':
                    break
        sy = selc_y
        for square in reversed(squares):
            x, y = square.get_coordinates()
            if sx == x and sy + 70 < y < sy + 140:
                if square.get_piece() is None:
                    queen = Queen("none", self.piece_id, x, y)
                    queen.draw_piece()
                    del queen
                    self.possibles.append(square)
                    sy = y
                elif square.get_piece() is not None and square.get_piece().piece_id[0] == 'b':
                    queen = Queen("none", self.piece_id, x, y)
                    queen.draw_piece()
                    del queen
                    self.possibles.append(square)
                    break
                elif square.get_piece() is not None and square.get_piece().piece_id[0] == 'w':
                    break
        sx = selc_x
        sy = selc_y
        for square in squares:
            x, y = square.get_coordinates()
            if sy == y and sx + 85 < x < sx + 170:
                if square.get_piece() is None:
                    queen = Queen("none", self.piece_id, x, y)
                    queen.draw_piece()
                    del queen
                    self.possibles.append(square)
                    sx = x
                elif square.get_piece() is not None and square.get_piece().piece_id[0] == 'b':
                    queen = Queen("none", self.piece_id, x, y)
                    queen.draw_piece()
                    del queen
                    self.possibles.append(square)
                    break
                elif square.get_piece() is not None and square.get_piece().piece_id[0] == 'w':
                    break
        sx = selc_x
        sy = selc_y
        for square in reversed(squares):
            x, y = square.get_coordinates()
            if sy == y and sx - 170 < x < sx - 85:
                if square.get_piece() is None:
                    queen = Queen("none", self.piece_id, x, y)
                    queen.draw_piece()
                    del queen
                    self.possibles.append(square)
                    sx = x
                elif square.get_piece() is not None and square.get_piece().piece_id[0] == 'b':
                    queen = Queen("none", self.piece_id, x, y)
                    queen.draw_piece()
                    del queen
                    self.possibles.append(square)
                    break
                elif square.get_piece() is not None and square.get_piece().piece_id[0] == 'w':
                    break

   def set_None(self, squares):  # make the piece of the square is equal to null
        for square in squares:
            if square.get_piece() == self:
                square.set_piece(None)

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


