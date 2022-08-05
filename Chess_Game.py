from ast import And
from pickle import TRUE
import pygame
from pygame.locals import *
import sys
from pygame.sprite import Sprite
from Bishop import Bishop
from Pawn import Pawn
from Horse import Horse
from Rook import Rook
from Queen import Queen
from King import King
pygame.init()

display = pygame.display.set_mode((1000, 700))
FPS_CLOCK = pygame.time.Clock()
pygame.display.set_caption("Chess")
background_image = pygame.image.load("images\chess.bmp")
background_image = pygame.transform.scale(background_image, (800, 650))

counter=0
clicks = []
location = ()

 # the black pawns objects//////////////////////////////
pawn_objects = [] # black pawns array

black_pawn1 = Pawn("black","bp1")
pawn_objects.append(black_pawn1)
black_pawn2 = Pawn("black","bp2")
pawn_objects.append(black_pawn2)
black_pawn3 = Pawn("black","bp3")
pawn_objects.append(black_pawn3)
black_pawn4 = Pawn("black","bp4")
pawn_objects.append(black_pawn4)
black_pawn5 = Pawn("black","bp5")
pawn_objects.append(black_pawn5)
black_pawn6 = Pawn("black","bp6")
pawn_objects.append(black_pawn6)
black_pawn7 = Pawn("black","bp7")
pawn_objects.append(black_pawn7)
black_pawn8 = Pawn("black","bp8")
pawn_objects.append(black_pawn8)

#the black horsses objects///////////////////
horse_objects = []  #black horses array //////////////
black_horse_left = Horse("black","bhl")
horse_objects.append(black_horse_left)
black_horse_right = Horse("black","bhr")
horse_objects.append(black_horse_right)

# Black Bishops objects ////////////////
black_bishop_objects = [] # black bishops array
black_bishop_left = Bishop("black","bbl")
black_bishop_objects.append(black_bishop_left)
black_bishop_right = Bishop("black","bbr")
black_bishop_objects.append(black_bishop_right)

# Black rooks objects /////////
black_rook_objects = []
black_rook_left = Rook("black","brl")
black_rook_objects.append(black_rook_left)
black_rook_right = Rook("black","brr")
black_rook_objects.append(black_rook_right)

# Black queen object
black_queen_object =[]
black_queen = Queen("black","bq")
black_queen_object.append(black_queen)

# Black king object
black_king_object =[]
black_king = King("black","bk")
black_king_object.append(black_king)




# the white pawns objects
white_pawn_objects = []
white_pawn1 = Pawn("white","wp1")
white_pawn_objects.append(white_pawn1)
white_pawn2 = Pawn("white","wp2")
white_pawn_objects.append(white_pawn2)
white_pawn3 = Pawn("white","wp3")
white_pawn_objects.append(white_pawn3)
white_pawn4 = Pawn("white","wp4")
white_pawn_objects.append(white_pawn4)
white_pawn5 = Pawn("white","wp5")
white_pawn_objects.append(white_pawn5)
white_pawn6 = Pawn("white","wp6")
white_pawn_objects.append(white_pawn6)
white_pawn7 = Pawn("white","wp7")
white_pawn_objects.append(white_pawn7)
white_pawn8 = Pawn("white","wp8")
white_pawn_objects.append(white_pawn8)

#the white horsses objects///////////////////
white_horse_left = Horse("white","whl")
horse_objects.append(white_horse_left)
white_horse_right = Horse("white","whr")
horse_objects.append(white_horse_right)


# White Bishops objects ////////////////
white_bishop_objects = [] # white bishops array
white_bishop_left = Bishop("white","bbl")
white_bishop_objects.append(black_bishop_left)
white_bishop_right = Bishop("white","bbr")
white_bishop_objects.append(white_bishop_right)

# white rooks objects ///////////
white_rook_objects = []
white_rook_left = Rook("white", "wrl")
white_rook_right =Rook("white", "wrr")

# white queen object //////////
white_queen_objects = []
white_queen = Queen("white", "wq")

# white king object //////////
white_king_objects = []
white_king = King("white", "wk")





# coordinates of each piece/////////////////////////////////////////////////////

# the pawns coordinates
black_pawn1_x=30
black_pawn1_y=460
black_pawn2_x = 120
black_pawn2_y = 460
black_pawn3_x = 210
black_pawn3_y = 460
black_pawn4_x = 300
black_pawn4_y = 460
black_pawn5_x = 390
black_pawn5_y = 460
black_pawn6_x = 480
black_pawn6_y = 460
black_pawn7_x = 570
black_pawn7_y = 460
black_pawn8_x = 660
black_pawn8_y = 460

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

# White pawns coordinates
white_pawn1_x = 30
white_pawn1_y = 90
white_pawn2_x = 120
white_pawn2_y = 90
white_pawn3_x = 210
white_pawn3_y = 90
white_pawn4_x = 300
white_pawn4_y = 90
white_pawn5_x = 390
white_pawn5_y = 90
white_pawn6_x = 480
white_pawn6_y = 90
white_pawn7_x = 570
white_pawn7_y = 90
white_pawn8_x = 660
white_pawn8_y = 90

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


def set_piece_position(): # Draw  the chess pieces in their initial positions
    # the black pawns /////////////
    black_pawn1.draw_piece()
    display.blit(black_pawn1.draw_piece(), (black_pawn1.set_coordinates(black_pawn1_x, black_pawn1_y)))  # first black pawn
    black_pawn2.draw_piece()
    display.blit(black_pawn2.draw_piece(), (black_pawn2.set_coordinates(black_pawn2_x, black_pawn2_y)))
    black_pawn3.draw_piece()
    display.blit(black_pawn3.draw_piece(), (black_pawn3.set_coordinates(black_pawn3_x, black_pawn3_y)))
    black_pawn4.draw_piece()
    display.blit(black_pawn4.draw_piece(), (black_pawn4.set_coordinates(black_pawn4_x, black_pawn4_y)))
    black_pawn5.draw_piece()
    display.blit(black_pawn5.draw_piece(), (black_pawn5.set_coordinates(black_pawn5_x, black_pawn5_y)))
    black_pawn6.draw_piece()
    display.blit(black_pawn6.draw_piece(), (black_pawn6.set_coordinates(black_pawn6_x, black_pawn6_y)))
    black_pawn7.draw_piece()
    display.blit(black_pawn7.draw_piece(), (black_pawn7.set_coordinates(black_pawn7_x, black_pawn7_y)))
    black_pawn8.draw_piece()
    display.blit(black_pawn8.draw_piece(), (black_pawn8.set_coordinates(black_pawn8_x, black_pawn8_y)))

    #the black horses ///////////////////////
    black_horse_left.draw_piece()
    display.blit(black_horse_left.draw_piece(), (black_horse_left.set_coordinates(black_horse_left_x, black_horse_left_y)))
    black_horse_right.draw_piece()
    display.blit(black_horse_right.draw_piece(), (black_horse_right.set_coordinates(black_horse_right_x, black_horse_right_y)))

    # Black Bishops //////////////////////////
    black_bishop_left.draw_piece()
    display.blit(black_bishop_left.draw_piece(), (black_bishop_left.set_coordinates(black_bishop_left_x, black_bishop_left_y)))
    black_bishop_right.draw_piece()
    display.blit(black_bishop_right.draw_piece(), (black_bishop_right.set_coordinates(black_bishop_right_x, black_bishop_right_y)))

    # Black Rooks ///////////////////
    black_rook_left.draw_piece()
    display.blit(black_rook_left.draw_piece(), (black_rook_left.set_coordinates(black_rook_left_x, black_rook_left_y)))
    black_bishop_right.draw_piece()
    display.blit(black_rook_right.draw_piece(), (black_rook_right.set_coordinates(black_rook_right_x, black_rook_right_y)))

    #Black queen ///////////////
    black_queen.draw_piece()
    display.blit(black_queen.draw_piece(), (black_queen.set_coordinates(black_queen_x, black_queen_y)))

    #Black king ///////////////
    black_king.draw_piece()
    display.blit(black_king.draw_piece(), (black_king.set_coordinates(black_king_x, black_king_y)))


    # the white pawns ///////////
    white_pawn1.draw_piece()
    display.blit(white_pawn1.draw_piece(), (white_pawn1.set_coordinates(white_pawn1_x, white_pawn1_y)))  # first white pawn
    white_pawn2.draw_piece()
    display.blit(white_pawn2.draw_piece(), (white_pawn2.set_coordinates(white_pawn2_x, white_pawn2_y)))
    white_pawn3.draw_piece()
    display.blit(white_pawn3.draw_piece(), (white_pawn3.set_coordinates(white_pawn3_x, white_pawn3_y)))
    white_pawn4.draw_piece()
    display.blit(white_pawn4.draw_piece(), (white_pawn4.set_coordinates(white_pawn4_x, white_pawn4_y)))
    white_pawn5.draw_piece()
    display.blit(white_pawn5.draw_piece(), (white_pawn5.set_coordinates(white_pawn5_x, white_pawn5_y)))
    white_pawn6.draw_piece()
    display.blit(white_pawn6.draw_piece(), (white_pawn6.set_coordinates(white_pawn6_x, white_pawn6_y)))
    white_pawn7.draw_piece()
    display.blit(white_pawn7.draw_piece(), (white_pawn7.set_coordinates(white_pawn7_x, white_pawn7_y)))
    white_pawn8.draw_piece()
    display.blit(white_pawn8.draw_piece(), (white_pawn8.set_coordinates(white_pawn8_x, white_pawn8_y)))

    #the white horses ///////////////////////
    white_horse_left.draw_piece()
    display.blit(white_horse_left.draw_piece(), (white_horse_left.set_coordinates(white_horse_left_x, white_horse_left_y)))
    black_horse_right.draw_piece()
    display.blit(white_horse_right.draw_piece(), (white_horse_right.set_coordinates(white_horse_right_x, white_horse_right_y)))

    # the white bishops///////////////////////
    white_bishop_left.draw_piece()
    display.blit(white_bishop_left.draw_piece(), (white_bishop_left.set_coordinates(white_bishop_left_x, white_bishop_left_y)))
    black_bishop_right.draw_piece()
    display.blit(white_bishop_right.draw_piece(), (white_bishop_right.set_coordinates(white_bishop_right_x, white_bishop_right_y)))

    # the white rooks///////////////////////
    white_rook_left.draw_piece()
    display.blit(white_rook_left.draw_piece(), (white_rook_left.set_coordinates(white_rook_left_x, white_rook_left_y)))
    black_rook_right.draw_piece()
    display.blit(white_rook_right.draw_piece(), (white_rook_right.set_coordinates(white_rook_right_x, white_rook_right_y)))

    #White queen ///////////////
    white_queen.draw_piece()
    display.blit(white_queen.draw_piece(), (white_queen.set_coordinates(white_queen_x, white_queen_y)))

    #White king ///////////////
    white_king.draw_piece()
    display.blit(white_king.draw_piece(), (white_king.set_coordinates(white_king_x, white_king_y)))



def check_object_selected(x,y):
    """
    check whether the user selected a piece
    :param x:
    :param y:
    :return: The id of a selected piece
    """
    s=""
    for i in range(8):
        if  pawn_objects[i].x <=x and pawn_objects[i].x >=x-100 and pawn_objects[i].y <=y+5 and pawn_objects[i].y>=y-70: 
            s = pawn_objects[i].piece_id
    for i in range(8):
        if  white_pawn_objects[i].x <=x and white_pawn_objects[i].x >=x-100 and white_pawn_objects[i].y <=y-20 and white_pawn_objects[i].y>=y-100: 
            s = white_pawn_objects[i].piece_id
    for i in range(4):
        if horse_objects[i].x <=x-10 and horse_objects[i].x >=x-100 and  horse_objects[i].y <=y-30 and horse_objects[i].y>=y-100: 
            s = horse_objects[i].piece_id
    return s


def identify_piece(x, y):
    """
    identify which piece the user has chosen and show the possible moves
    :param x:
    :param y:
    :return:
    """
    id_got = check_object_selected(x, y)
    if id_got == "bp1":
        pawn = Pawn("none", "bp1")
        display.blit(pawn.draw_piece(), (pawn.set_coordinates(black_pawn1_x + 18, black_pawn1_y - 60)))
        return x,y
    elif id_got =="bp2":
        pawn = Pawn("none","bp2")
        display.blit(pawn.draw_piece(), (pawn.set_coordinates(black_pawn2_x + 18, black_pawn2_y - 60)))
        return x,y
    elif id_got =="bp3":
        pawn = Pawn("none","bp3")
        display.blit(pawn.draw_piece(), (pawn.set_coordinates(black_pawn3_x + 18, black_pawn3_y - 60)))
        return x,y
    elif id_got =="bp4":
        pawn = Pawn("none","bp4")
        display.blit(pawn.draw_piece(), (pawn.set_coordinates(black_pawn4_x + 18, black_pawn4_y - 60)))
        return x,y
    elif id_got =="bp5":
        pawn = Pawn("none","bp5")
        display.blit(pawn.draw_piece(), (pawn.set_coordinates(black_pawn5_x + 18, black_pawn5_y - 60)))
        return x,y
    elif id_got =="bp6":
        pawn = Pawn("none","bp6")
        display.blit(pawn.draw_piece(), (pawn.set_coordinates(black_pawn6_x + 18, black_pawn6_y - 60)))
        return x,y
    elif id_got =="bp7":
        pawn = Pawn("none","bp7")
        display.blit(pawn.draw_piece(), (pawn.set_coordinates(black_pawn7_x + 18, black_pawn7_y - 60)))
        return x,y
    elif id_got =="bp8":
        pawn = Pawn("none","bp8")
        display.blit(pawn.draw_piece(), (pawn.set_coordinates(black_pawn8_x + 18, black_pawn8_y - 60)))
        return x,y
    elif id_got =="wp1":
        pawn = Pawn("none","wp1")
        display.blit(pawn.draw_piece(), (pawn.set_coordinates(white_pawn1_x + 18, white_pawn1_y + 90)))
        return x,y
    elif id_got =="wp2":
        pawn = Pawn("none","wp2")
        display.blit(pawn.draw_piece(), (pawn.set_coordinates(white_pawn2_x + 18, white_pawn2_y + 90)))
        return x,y
    elif id_got =="wp3":
        pawn = Pawn("none","wp3")
        display.blit(pawn.draw_piece(), (pawn.set_coordinates(white_pawn3_x + 18, white_pawn3_y + 90)))
        return x,y
    elif id_got =="wp3":
        pawn = Pawn("none","wp3")
        display.blit(pawn.draw_piece(), (pawn.set_coordinates(white_pawn3_x + 18, white_pawn3_y + 90)))
        return x,y
    elif id_got =="wp4":
        pawn = Pawn("none","wp4")
        display.blit(pawn.draw_piece(), (pawn.set_coordinates(white_pawn4_x + 18, white_pawn4_y + 90)))
        return x,y
    elif id_got =="wp5":
        pawn = Pawn("none","wp5")
        display.blit(pawn.draw_piece(), (pawn.set_coordinates(white_pawn5_x + 18, white_pawn5_y + 90)))
        return x,y
    elif id_got =="wp6":
        pawn = Pawn("none","wp6")
        display.blit(pawn.draw_piece(), (pawn.set_coordinates(white_pawn6_x + 18, white_pawn6_y + 90)))
        return x,y
    elif id_got =="wp7":
        pawn = Pawn("none","wp7")
        display.blit(pawn.draw_piece(), (pawn.set_coordinates(white_pawn7_x + 18, white_pawn7_y + 90)))
        return x,y
    elif id_got =="wp8":
        pawn = Pawn("none","wp8")
        display.blit(pawn.draw_piece(), (pawn.set_coordinates(white_pawn8_x + 18, white_pawn8_y + 90)))
        return x,y

    #Horses
    elif id_got =="bhl":
        horse = Horse("none","bhl")
        display.blit(horse.draw_piece(), (horse.set_coordinates(black_horse_left_x + 105, black_horse_left_y - 130)))
        display.blit(horse.draw_piece(), (horse.set_coordinates(black_horse_left_x - 70, black_horse_left_y - 130)))
    elif id_got =="bhr":
        horse = Horse("none","bhr")
        display.blit(horse.draw_piece(), (horse.set_coordinates(black_horse_right_x + 105, black_horse_right_y - 130)))
        display.blit(horse.draw_piece(), (horse.set_coordinates(black_horse_right_x - 70, black_horse_right_y - 130)))
    elif id_got =="whl":
        horse = Horse("none","whl")
        display.blit(horse.draw_piece(), (horse.set_coordinates(white_horse_left_x + 105, white_horse_left_y + 160)))
        display.blit(horse.draw_piece(), (horse.set_coordinates(white_horse_left_x - 73, white_horse_left_y + 160)))
    elif id_got =="whr":
        horse = Horse("none","whr")
        display.blit(horse.draw_piece(), (horse.set_coordinates(white_horse_right_x + 105, white_horse_right_y + 160)))
        display.blit(horse.draw_piece(), (horse.set_coordinates(white_horse_right_x - 73, white_horse_right_y + 160)))


def move_piece(x, y, id):
    # for pawns
    if id=="bp1":
        global black_pawn1_y 
        if y == black_pawn1_y or (y <= black_pawn1_y+5 and y >= black_pawn1_y-70):
            black_pawn1_y = black_pawn1_y-73
    if id=="bp2":
        global black_pawn2_y 
        if y == black_pawn2_y or (y <= black_pawn2_y+5 and y >= black_pawn2_y-70):
            black_pawn2_y = black_pawn2_y-73
    if id=="bp3":
        global black_pawn3_y 
        if y == black_pawn3_y or (y <= black_pawn3_y+5 and y >= black_pawn3_y-70):
            black_pawn3_y = black_pawn3_y-73
    if id=="bp4":
        global black_pawn4_y 
        if y == black_pawn4_y or (y <= black_pawn4_y+5 and y >= black_pawn4_y-70):
            black_pawn4_y = black_pawn4_y-73
    if id=="bp5":
        global black_pawn5_y 
        if y == black_pawn5_y or (y <= black_pawn5_y+5 and y >= black_pawn5_y-70):
            black_pawn5_y = black_pawn5_y-73
    if id=="bp6":
        global black_pawn6_y 
        if y == black_pawn6_y or (y <= black_pawn6_y+5 and y >= black_pawn6_y-70):
            black_pawn6_y = black_pawn6_y-73
    if id=="bp7":
        global black_pawn7_y 
        if y == black_pawn7_y or (y <= black_pawn7_y+5 and y >= black_pawn7_y-70):
            black_pawn7_y = black_pawn7_y-73
    if id=="bp8":
        global black_pawn8_y 
        if y == black_pawn8_y or (y <= black_pawn8_y+5 and y >= black_pawn8_y-70):
            black_pawn8_y = black_pawn8_y-73
    
     # the white pawns
    if id=="wp1":
        global white_pawn1_y 
        if y == white_pawn1_y or (y >= white_pawn1_y+5 and y <= white_pawn1_y+160):
            white_pawn1_y = white_pawn1_y+73
    if id=="wp2":
        global white_pawn2_y 
        if y == white_pawn2_y or (y >= white_pawn2_y+5 and y <= white_pawn2_y+160):
            white_pawn2_y = white_pawn2_y+73
    if id=="wp3":
        global white_pawn3_y 
        if y == white_pawn3_y or (y >= white_pawn3_y+5 and y <= white_pawn3_y+160):
            white_pawn3_y = white_pawn3_y+73
    if id=="wp4":
        global white_pawn4_y 
        if y == white_pawn4_y or (y >= white_pawn4_y+5 and y <= white_pawn4_y+160):
            white_pawn4_y = white_pawn4_y+73
    if id=="wp5":
        global white_pawn5_y 
        if y == white_pawn5_y or (y >= white_pawn5_y+5 and y <= white_pawn5_y+160):
            white_pawn5_y = white_pawn5_y+73
    if id=="wp6":
        global white_pawn6_y 
        if y == white_pawn6_y or (y >= white_pawn6_y+5 and y <= white_pawn6_y+160):
            white_pawn6_y = white_pawn6_y+73
    if id=="wp7":
        global white_pawn7_y 
        if y == white_pawn7_y or (y >= white_pawn7_y+5 and y <= white_pawn7_y+160):
            white_pawn7_y = white_pawn7_y+73
    if id=="wp8":
        global white_pawn8_y 
        if y == white_pawn8_y or (y >= white_pawn8_y+5 and y <= white_pawn8_y+160):
            white_pawn8_y = white_pawn8_y+73

    # Horses Movement
    if id=="bhl":
        global black_horse_left_x
        global black_horse_left_y
        if y == black_horse_left_y or (y <= black_horse_left_y - 90 and y >= black_horse_left_y - 130):
           if x==black_horse_left_x or(x<=black_horse_left_x + 180 and x>= black_horse_left_x + 90):
              black_horse_left_y = black_horse_left_y-145
              black_horse_left_x = black_horse_left_x+90
           elif x<=black_horse_left_x+10:
              black_horse_left_y = black_horse_left_y-145
              black_horse_left_x = black_horse_left_x-90
    if id=="bhr":
        global black_horse_right_x
        global black_horse_right_y
        if y == black_horse_right_y or (y <= black_horse_right_y - 90 and y >= black_horse_right_y - 130):
           if x==black_horse_right_x or(x<=black_horse_right_x + 180 and x>= black_horse_right_x + 90):
              black_horse_right_y = black_horse_right_y-145
              black_horse_right_x = black_horse_right_x+90
           elif x<=black_horse_right_x+10 and x>=black_horse_right_x -180:
              black_horse_right_y = black_horse_right_y-145
              black_horse_right_x = black_horse_right_x-90




# we need a function that searches for objects near each piece movement 
#that when i select a piece and call this function it should search in all possible squares of movement if there is any piece

while True:  # Game main loop
    display.blit(background_image,(1,0))
    set_piece_position()
    for event in pygame.event.get():
        if event.type == MOUSEBUTTONDOWN:  #check if the mouse was pressed
            x, y = pygame.mouse.get_pos()
            check_object_selected(x, y)
            identify_piece(x, y)
            location = (x, y)
            clicks.append(x)
            clicks.append(y)
            counter += 1
            if counter == 2:
                move_piece(clicks[2], clicks[3], check_object_selected(clicks[0], clicks[1]))
                clicks =[]
                counter = 0
            
            
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    FPS_CLOCK.tick(30)