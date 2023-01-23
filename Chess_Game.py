from ast import And
from pickle import TRUE
import pygame
from pygame.locals import *
import sys
from pygame.sprite import Sprite
from pieces.Bishop import Bishop
from pieces.Rook import Rook
from pieces.Queen import Queen
from pieces.King import King
from pieces.whitePieces.WhiteHorse import WhiteHorse
from pieces.whitePieces.WhitePawn import WhitePawn
from pieces.blackPieces.BlackHorse import BlackHorse
from pieces.blackPieces.BlackPawn import BlackPawn
from pieces.blackPieces.BlackBishop import BlackBishop
from pieces.whitePieces.WhiteBishop import WhiteBishop
from pieces.blackPieces.BlackRook import BlackRook
from pieces.whitePieces.WhiteRook import WhiteRook
from pieces.blackPieces.BlackQueen import BlackQueen
from pieces.whitePieces.WhiteQueen import WhiteQueen
from pieces.blackPieces.BlackKing import BlackKing
from pieces.whitePieces.WhiteKing import WhiteKing
from pieces.Player import Player
from pieces.Squares import Square
from util import display

pygame.init()

FPS_CLOCK = pygame.time.Clock()
pygame.display.set_caption("Chess")
background_image = pygame.image.load("images\chess.bmp")
background_image = pygame.transform.scale(background_image, (800, 650))

counter = 0
clicks = []
location = ()

# The black Horses coordinates
black_horse_left_x = 120
black_horse_left_y = 530
black_horse_right_x = 570
black_horse_right_y = 530

# Black Bishops coordinates
black_bishop_left_x = 210
black_bishop_left_y = 530
black_bishop_right_x = 480
black_bishop_right_y = 530

# Black Rooks coordinates
black_rook_left_x = 30
black_rook_left_y = 530
black_rook_right_x = 660
black_rook_right_y = 530

# Black Queen coordinates
black_queen_x = 300
black_queen_y = 530

# Black king coordinates
black_king_x = 390
black_king_y = 530

# white horses coordinates
white_horse_left_x = 120
white_horse_left_y = 20
white_horse_right_x = 570
white_horse_right_y = 20

# white bishops coordinates
white_bishop_left_x = 210
white_bishop_left_y = 20
white_bishop_right_x = 480
white_bishop_right_y = 20

# white rooks coordinates
white_rook_left_x = 30
white_rook_left_y = 20
white_rook_right_x = 660
white_rook_right_y = 20

# White Queen coordinates
white_queen_x = 300
white_queen_y = 20

# White king coordinates
white_king_x = 390
white_king_y = 20

# pieces and squares declaration///////////

squares = []
sq_x = 45
sq_y = 545
sq_width = 85
sq_height = 70
pieces = []

BRL = BlackRook("black", "brl", black_rook_left_x, black_rook_left_y)
pieces.append(BRL)
squares.append(Square(sq_x, sq_y, sq_width, sq_height, BRL))
sq_x += 90
BHL = BlackHorse("black", "bhl", black_horse_left_x, black_horse_left_y)
pieces.append(BHL)
squares.append(Square(sq_x, sq_y, sq_width, sq_height, BHL))

sq_x += 90
BBL = BlackBishop("black", "bbl", black_bishop_left_x, black_bishop_left_y)
pieces.append(BBL)
squares.append(Square(sq_x, sq_y, sq_width, sq_height, BBL))
sq_x += 90
BQ = BlackQueen("black", "bq", black_queen_x, black_queen_y)
pieces.append(BQ)
squares.append(Square(sq_x, sq_y, sq_width, sq_height, BQ))
sq_x += 90
BK = BlackKing("black", "bk", black_king_x, black_king_y)
pieces.append(BK)
squares.append(Square(sq_x, sq_y, sq_width, sq_height, BK))
sq_x += 90
BBR = BlackBishop("black", "bbr", black_bishop_right_x, black_bishop_right_y)
pieces.append(BBR)
squares.append(Square(sq_x, sq_y, sq_width, sq_height, BBR))
sq_x += 90
BHR = BlackHorse("black", "bhr", black_horse_right_x, black_horse_right_y)
pieces.append(BHR)
squares.append(Square(sq_x, sq_y, sq_width, sq_height, BHR))
sq_x += 90
BRR = BlackRook("black", "brr", black_rook_right_x, black_rook_right_y)
pieces.append(BRR)
squares.append(Square(sq_x, sq_y, sq_width, sq_height, BRR))
sq_x += 90

sq_x = 45
sq_y = 472
for x in range(1, 9):
    BP = BlackPawn("black", "bp" + str(x), 30 + 90 * (x - 1), 460)
    squares.append(Square(sq_x, sq_y, sq_width, sq_height, BP))
    sq_x += 90
    pieces.append(BP)

sq_x = 45
sq_y = 400
for i in range(32):
    if i == 8 or i == 16 or i == 24:
        sq_y = sq_y - 73
        sq_x = 45
    squares.append(Square(sq_x, sq_y, sq_width, sq_height, None))
    sq_x += 90

sq_x = 45
sq_y = 108
for x in range(1, 9):
    WP = WhitePawn("white", "wp" + str(x), 30 + 90 * (x - 1), 90)
    pieces.append(WP)
    squares.append(Square(sq_x, sq_y, sq_width, sq_height, WP))
    sq_x += 90
    pieces.append(WP)

sq_x = 45
sq_y = 35
WRL = WhiteRook("white", "wrl", white_rook_left_x, white_rook_left_y)
pieces.append(WRL)
squares.append(Square(sq_x, sq_y, sq_width, sq_height, WRL))
sq_x += 90
WHL = WhiteHorse("white", "whl", white_horse_left_x, white_horse_left_y)
pieces.append(WHL)
squares.append(Square(sq_x, sq_y, sq_width, sq_height, WHL))
sq_x += 90
WBL = WhiteBishop("white", "wbl", white_bishop_left_x, white_bishop_left_y)
pieces.append(WBL)
squares.append(Square(sq_x, sq_y, sq_width, sq_height, WBL))
sq_x += 90
WQ = WhiteQueen("white", "wq", white_queen_x, white_queen_y)
pieces.append(WQ)
squares.append(Square(sq_x, sq_y, sq_width, sq_height, WQ))
sq_x += 90
WK = WhiteKing("white", "wk", white_king_x, white_king_y)
pieces.append(WK)
squares.append(Square(sq_x, sq_y, sq_width, sq_height, WK))
sq_x += 90
WBR = WhiteBishop("white", "wbr", white_bishop_right_x, white_bishop_right_y)
pieces.append(WBR)
squares.append(Square(sq_x, sq_y, sq_width, sq_height, WBR))
sq_x += 90
WHR = WhiteHorse("white", "whr", white_horse_right_x, white_horse_right_y)
pieces.append(WHR)
squares.append(Square(sq_x, sq_y, sq_width, sq_height, WHR))
sq_x += 90
WRR = WhiteRook("white", "wrr", white_rook_right_x, white_rook_right_y)
pieces.append(WRR)
squares.append(Square(sq_x, sq_y, sq_width, sq_height, WRR))
sq_x += 90

BlackPlayer = Player(0, 0)
WhitePlayer = Player(1, 0)


def draw_pieces():
    """
    Draw the chess pieces
    :return: nothing
    """
    for piece in pieces:
        piece.draw_piece()


def check_selected_object(click_x, click_y):
    """
    check whether the user selected a square
    :param click_x:
    :param click_y:
    :return: the selected square, otherwise None
    """
    for square in squares:
        if square.is_selected(click_x, click_y):
            return square
    return None


def draw_possible_moves(x, y):
    """
    Show the possible moves of selected piece
    :param x: mouse_click x_position
    :param y: mouse_click y_position
    :return:
    """
    selectedSquare = check_selected_object(x, y)
    if selectedSquare is not None:
        if selectedSquare.get_piece() is not None:
            selectedSquare.get_piece().draw_possible_moves(squares, selectedSquare.x, selectedSquare.y)


def move_piece(x, y, piece):
    """
    Changes the position of a piece to a new valid place
    :param x: x of new position
    :param y: y of new position
    :param piece: the moving piece
    :return: null
    """
    if piece is not None:
        piece.move(x, y, squares)


def white_king_checked():
    for square in squares:
        if square.get_piece() is not None and square.get_piece() == BQ:
            piece = square.get_piece()
            x, y = square.get_coordinates()
            if piece.see_king(squares, x, y):
                WK.is_checked = 1
                return True
            else:
                WK.is_checked = 0
                return False


def return_me(square, piece):
    piece.set_None(squares)
    piece.x = square.x - 20
    piece.y = square.y - 10
    square.set_piece(piece)


white_flag = 0  # flag for the white king if checked

while True:  # Game main loop
    display.blit(background_image, (1, 0))
    # squares[1].render(display,255,255,255)

    draw_pieces()
    # white_king_checked()
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:  # check if the mouse was pressed
            x, y = pygame.mouse.get_pos()
            draw_possible_moves(x, y)
            clicks.append(x)
            clicks.append(y)
            counter += 1
            #if counter == 2 and check_selected_object(clicks[0], clicks[1]).get_piece().piece_id is not None:
            if counter == 2 and check_selected_object(clicks[0], clicks[1]) is not None:
                id = check_selected_object(clicks[0], clicks[1]).get_piece().piece_id
                my_piece = check_selected_object(clicks[0], clicks[1]).get_piece()
                ##################
                for square in squares:
                    if square.get_piece() == my_piece:
                        x_prev, y_prev = square.get_coordinates()
                        whiteSquareOfMovedPiece = square  # get the square of the white piece before trying any moves
                                                       # in case check white happened

                if id[0] == 'w' and WhitePlayer.GetTurn() == 1:
                    move_piece(clicks[2], clicks[3], check_selected_object(clicks[0], clicks[1]).get_piece())
                    WhitePlayer.ResetTurn()
                    BlackPlayer.SetTurn()
                    white_king_checked()
                white_flag = white_king_checked()  # see if the white king is checked
                if white_flag == 1:
                    return_me(whiteSquareOfMovedPiece, my_piece)  # place the piece to its previous position
                    BlackPlayer.ResetTurn()
                    WhitePlayer.SetTurn()

                elif id[0] == 'b' and BlackPlayer.GetTurn() == 1:
                    move_piece(clicks[2], clicks[3], check_selected_object(clicks[0], clicks[1]).get_piece())
                    BlackPlayer.ResetTurn()
                    WhitePlayer.SetTurn()
                    white_king_checked()
                    white_flag = white_king_checked()
                clicks = []
                counter = 0

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    FPS_CLOCK.tick(30)
