from util import display
from pieces.Squares import Square
from pieces.Bishop import Bishop

class WhiteBishop(Bishop):
    def __init__(self, colour, piece_id, x, y):
        self.possibles =[]
        super(WhiteBishop, self).__init__(colour, piece_id, x, y)

    def draw_possible_moves(self,squares,selc_x,selc_y):
        sx = selc_x
        sy = selc_y
        for square in squares:
            x , y = square.get_coordinates()
            if sx +85 < x < sx + 170 and sy -140 < y < sy - 70:
                if square.get_piece() == None:
                    bishop = Bishop("none",self.piece_id, x,y)
                    bishop.draw_piece()
                    del bishop
                    self.possibles.append(square)
                    sx = x
                    sy = y
                elif square.get_piece() != None and square.get_piece().piece_id[0]=='b':
                    bishop = Bishop("none",self.piece_id, x,y)
                    bishop.draw_piece()
                    del bishop
                    self.possibles.append(square)
                    break
                elif square.get_piece() != None and square.get_piece().piece_id[0] == 'w':
                    break
        sx = selc_x
        sy = selc_y
        for square in squares:
            x , y = square.get_coordinates()
            if sx - 170 < x < sx - 85 and sy - 140 < y < sy - 70:
                if square.get_piece() == None:
                    bishop = Bishop("none",self.piece_id, x,y)
                    bishop.draw_piece()
                    del bishop
                    self.possibles.append(square)
                    sx = x
                    sy = y
                elif square.get_piece() != None and square.get_piece().piece_id[0]=='b':
                    bishop = Bishop("none",self.piece_id, x,y)
                    bishop.draw_piece()
                    del bishop
                    self.possibles.append(square)
                    break
                elif square.get_piece() != None and square.get_piece().piece_id[0] == 'w':
                    break
        sx = selc_x
        sy = selc_y
        for square in squares:
            x , y = square.get_coordinates()
            if sx + 85 < x < sx + 170 and sy + 70 < y < sy + 140:
                if square.get_piece() == None: 
                    bishop = Bishop("none",self.piece_id, x,y)
                    bishop.draw_piece()
                    del bishop
                    self.possibles.append(square)
                    sx = x
                    sy = y
                elif square.get_piece() != None and square.get_piece().piece_id[0]=='b':
                    bishop = Bishop("none",self.piece_id, x,y)
                    bishop.draw_piece()
                    del bishop
                    self.possibles.append(square)
                    break
                elif square.get_piece() != None and square.get_piece().piece_id[0] == 'w':
                    break
        sx = selc_x
        sy = selc_y
        for square in squares:
            x , y = square.get_coordinates()
            if sx -170 < x < sx - 85 and sy +70 < y < sy + 140:
                if square.get_piece() == None:
                    bishop = Bishop("none",self.piece_id, x,y)
                    bishop.draw_piece()
                    del bishop
                    self.possibles.append(square)
                    sx = x
                    sy = y
                elif square.get_piece() != None and square.get_piece().piece_id[0]=='b':
                    bishop = Bishop("none",self.piece_id, x,y)
                    bishop.draw_piece()
                    del bishop
                    self.possibles.append(square)
                    break
                elif square.get_piece() != None and square.get_piece().piece_id[0] == 'w':
                    break


    def set_None(self,squares): # make the piece of the square is equal to null 
        for square in squares:
            if square.get_piece() == self:
               square.set_piece(None)


    def move(self, click_x, click_y,squares): # move the piece to the square 
        moves_available = self.possibles
        for move in moves_available:
            x,y = move.get_coordinates()
            if x<= click_x <= x+85 and y <= click_y <= y+70:
                self.x = move.x-10
                self.y = move.y-15
                self.set_None(squares)
                move.set_piece(self)  


