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

pieces = []

for x in range(1, 9):
    pieces.append(BlackPawn("black", "bp" + str(x), 30 + 90 * (x - 1), 460))

pieces.append(BlackHorse("black", "bhl", black_horse_left_x, black_horse_left_y))
pieces.append(BlackHorse("black", "bhr", black_horse_right_x, black_horse_right_y))
pieces.append(Bishop("black", "bbl", black_bishop_left_x, black_bishop_left_y))
pieces.append(Bishop("black", "bbr", black_bishop_right_x, black_bishop_right_y))
pieces.append(Rook("black", "brl", black_rook_left_x, black_rook_left_y))
pieces.append(Rook("black", "brr", black_rook_right_x, black_rook_right_y))
pieces.append(Queen("black", "bq", black_queen_x, black_queen_y))
pieces.append(King("black", "bk", black_king_x, black_king_y))

for x in range(1, 9):
    pieces.append(WhitePawn("white", "wp" + str(x), 30 + 90 * (x - 1), 90))

pieces.append(WhiteHorse("white", "whl", white_horse_left_x, white_horse_left_y))
pieces.append(WhiteHorse("white", "whr", white_horse_right_x, white_horse_right_y))
pieces.append(Bishop("white", "wbl", white_bishop_left_x, white_bishop_left_y))
pieces.append(Bishop("white", "wbr", white_bishop_right_x, white_bishop_right_y))
pieces.append(Rook("white", "wrl", white_rook_left_x, white_rook_left_y))
pieces.append(Rook("white", "wrr", white_rook_right_x, white_rook_right_y))
pieces.append(Queen("white", "wq", white_queen_x, white_queen_y))
pieces.append(King("white", "wk", white_king_x, white_king_y))


def draw_pieces():
    """
    Draw the chess pieces
    :return: nothing
    """
    # the black pawns /////////////
    for piece in pieces:
        piece.draw_piece()


def check_selected_object(click_x, click_y):
    """
    check whether the user selected a piece
    :param click_x:
    :param click_y:
    :return: the selected piece, otherwise None
    """
    for piece in pieces:
        if piece.is_selected(click_x, click_y):
            return piece

    return None


def draw_possible_moves(x, y):
    """
    Show the possible moves of selected piece
    :param x: mouse_click x_position
    :param y: mouse_click y_position
    :return:
    """
    selectedPiece = check_selected_object(x, y)
    if selectedPiece is not None:
        selectedPiece.draw_possible_moves()


def move_piece(x, y, piece):
    """
    Changes the position of a piece to a new valid place
    :param x: x of new position
    :param y: y of new position
    :param piece: the moving piece
    :return: null
    """
    if piece is not None:
        piece.move(x, y)


# we need a function that searches for objects near each piece movement
# that when i select a piece and call this function it should search in all possible squares of movement if there is any piece

while True:  # Game main loop
    display.blit(background_image, (1, 0))
    draw_pieces()
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:  # check if the mouse was pressed
            x, y = pygame.mouse.get_pos()
            draw_possible_moves(x, y)
            clicks.append(x)
            clicks.append(y)
            counter += 1
            if counter == 2:
                move_piece(clicks[2], clicks[3], check_selected_object(clicks[0], clicks[1]))
                clicks = []
                counter = 0

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    FPS_CLOCK.tick(30)
