from util import display

from pieces.Horse import Horse

class WhiteHorse(Horse):

    def __init__(self, colour, piece_id, x, y):
        self.possibles =[]
        super(WhiteHorse, self).__init__(colour, piece_id, x, y)

    def draw_possible_moves(self,squares,selc_x,selc_y):
        for square in squares:
            x , y = square.get_coordinates()
            if selc_x+85 < x < selc_x + 170 and selc_y - 210 < y < selc_y - 140  :
                if square.get_piece() == None or square.get_piece().piece_id[0]=='b':
                    horse = Horse("none", self.piece_id, x , y )
                    horse.draw_piece()
                    del horse
                    self.possibles.append(square)

            if selc_x - 170 <= x <= selc_x - 85  and selc_y-210 <= y <= selc_y - 140:
                if square.get_piece() == None or square.get_piece().piece_id[0]=='b':
                    horse = Horse("none", self.piece_id, x , y )
                    horse.draw_piece()
                    del horse
                    self.possibles.append(square)

            if selc_x - 255 <= x <= selc_x - 170 and  selc_y - 140 <= y <= selc_y - 70:
                if square.get_piece() == None or square.get_piece().piece_id[0]=='b':
                    horse = Horse("none", self.piece_id, x , y )
                    horse.draw_piece()
                    del horse
                    self.possibles.append(square)

            if selc_x + 170 <= x <= selc_x + 255 and selc_y-140 <= y <= selc_y-70:
                if square.get_piece() == None or square.get_piece().piece_id[0]=='b':
                    horse = Horse("none", self.piece_id, x , y )
                    horse.draw_piece()
                    del horse
                    self.possibles.append(square)

            if selc_x + 85 <= x <= selc_x + 170 and selc_y + 140 <= y <= selc_y + 210:
                if square.get_piece() == None or square.get_piece().piece_id[0]=='b':
                    horse = Horse("none", self.piece_id, x , y )
                    horse.draw_piece()
                    del horse
                    self.possibles.append(square)

            if selc_x - 170 <= x <= selc_x -85 and selc_y + 140 <= y <= selc_y + 210:
                if square.get_piece() == None or square.get_piece().piece_id[0]=='b':
                    horse = Horse("none", self.piece_id, x , y )
                    horse.draw_piece()
                    del horse
                    self.possibles.append(square)

            if selc_x - 255 <= x <= selc_x - 170 and selc_y + 70 <= y <= selc_y + 140:
                if square.get_piece() == None or square.get_piece().piece_id[0]=='b':
                    horse = Horse("none", self.piece_id, x , y )
                    horse.draw_piece()
                    del horse
                    self.possibles.append(square)

            if selc_x + 170 <= x <= selc_x + 255 and selc_y + 70 <= y <= selc_y + 140:
                if square.get_piece() == None or square.get_piece().piece_id[0]=='b':
                    horse = Horse("none", self.piece_id, x , y )
                    horse.draw_piece()
                    del horse
                    self.possibles.append(square)

    def set_None(self,squares):
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