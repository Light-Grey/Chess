#from abc import ABC, abstractmethod

class Square:
    # Initialization function
    def __init__(self, material, x, y):
        self.material = material
        self.x = x
        self.y = y

    # Getters/Setters for material and coordinates
    def set_material(self, material):
        self.material = material
        
    def get_material(self):
        return self.material
    
    def set_x(self, x):
        self.x = x

    def get_x(self):
        return self.x

    def set_y(self, y):
        self.y = y

    def get_y(self):
        return self.y

# King Functionality
class King:
    # Initialization function
    def __init__(self, white):
        self.alive = True
        self.white = white

    # Getters/Setters for material and coordinates
    def set_white(self, white):
        self.white = white

    def get_white(self):
        return self.white

    def set_alive(self, alive):
        self.alive = alive

    def get_alive(self):
        return self.alive

    def valid_move(self, Square start, Square end):
        if end.get_material().get_white() == self.get_white():
            return False
        
        x_move = abs( end.get_x() - start.get_x() )
        y_move = abs( end.get_y() - start.get_y() )

        if x + y == 1:
            # IMPLEMENT: See if end destination would put king in check

            return True

        # IMPLEMENT: Castling functionality


# Queen functionality( Rook + Bishop )
class Queen:
    def __init__(self, white):
        self.alive = True
        self.white = white

    # Getters/Setters for color and life status
    def set_white(self, white):
        self.white = white

    def get_white(self):
        return self.white

    def set_alive(self, alive):
        self.alive = alive

    def get_alive(self):
        return self.alive

    # Checks for moving in diagonal or straight lines
    def valid_move(self, Square start, Square end):
        if end.get_material().get_white() == self.get_white():
            return False
        
        x_move = abs( end.get_x() - start.get_x() )
        y_move = abs( end.get_y() - start.get_y() )
        return x * y == 0 or x == y

        # IMPLEMENT: Check for collision of other pieces


# Rook functionality
class Rook:
    def __init__(self, white):
        self.alive = True
        self.white = white

    def set_white(self, white):
        self.white = white

    def get_white(self):
        return self.white

    def set_alive(self, alive):
        self.alive = alive

    def get_alive(self):
        return self.alive

    def valid_move(self, Square start, Square end):
        if end.get_material().get_white() == self.get_white():
            return False
        
        x_move = abs( end.get_x() - start.get_x() )
        y_move = abs( end.get_y() - start.get_y() )
        return x * y == 0

        # IMPLEMENT: Check for collision of other pieces


# Bishop functionality
class Bishop:
    def __init__(self, white):
        self.alive = True
        self.white = white

    def set_white(self, white):
        self.white = white

    def get_white(self):
        return self.white

    def set_alive(self, alive):
        self.alive = alive

    def get_alive(self):
        return self.alive

    def valid_move(self, Square start, Square end):
        if end.get_material().get_white() == self.get_white():
            return False
        
        x_move = abs( end.get_x() - start.get_x() )
        y_move = abs( end.get_y() - start.get_y() )
        return x == y

        # IMPLEMENT: Check for collision of other pieces


# Knight functionality
class Knight:
    def __init__(self, white):
        self.alive = True
        self.white = white

    def set_white(self, white):
        self.white = white

    def get_white(self):
        return self.white

    def set_alive(self, alive):
        self.alive = alive

    def get_alive(self):
        return self.alive

    def valid_move(self, Square start, Square end):
        if end.get_material().get_white() == self.get_white():
            return False
        
        x_move = abs( end.get_x() - start.get_x() )
        y_move = abs( end.get_y() - start.get_y() )
        return x * y == 2
        
        


# Pawn functionality
class Pawn:
    def __init__(self, white):
        self.alive = True
        self.white = white

    def set_white(self, white):
        self.white = white

    def get_white(self):
        return self.white

    def set_alive(self, alive):
        self.alive = alive

    def get_alive(self):
        return self.alive

    def valid_move(self, Square start, Square end):
        if end.get_material().get_white() == self.get_white():
            return False

        x_move = end.get_x() - start.get_x()
        y_move = abs( end.get_y() - start.get_y() )

        # Checks for moving forward one space
        if get_white():
            # Allows move by two if moving from initial position, otherwise move by one
            if x_move == 2 and start.get_x == 1:
                return True
            if x_move == 1 and y_move == 0:
                return True
            return False
        else:
            # Allows move by two if moving from initial position, otherwise move by one
            if x_move == -2 and start.get_x == 6:
                return True
            if x_move == -1 and y_move == 0:
                return True
            return False

        # IMPLEMENT: Check for collision of other pieces

class Board:
    def __init__(self):
        rows, cols = (8, 8)
        self.spaces = [[Square(None,0,0)] * 8 for _ in range(rows)]
        self.createBoard(self.spaces)

    def get_spaces(self, i, j):
        return self.spaces[i][j]
    

    def createBoard(self, spaces):
        # Boolean variable to change color of pieces (expels repeated code)
        white = True

        # Creates non-pawn pieces for both sides
        for i in range(0,8,7):
            spaces[i][0] = Square(Rook(white),   i, 0)
            spaces[i][1] = Square(Knight(white), i, 1)
            spaces[i][2] = Square(Bishop(white), i, 2)
            spaces[i][3] = Square(Queen(white),  i, 3)
            spaces[i][4] = Square(King(white),   i, 4)
            spaces[i][5] = Square(Bishop(white), i, 5)
            spaces[i][6] = Square(Knight(white), i, 6)
            spaces[i][7] = Square(Rook(white),   i, 7)
            white = not white
            #print( self.get_spaces(i, 0).get_x(), ",", self.get_spaces(i, 0).get_y() )
         
               # Creates pawn pieces for both sides
        for i in range(1,7,5):
            for j in range(8):
                spaces[i][j] = Square(Pawn(white), i, j)
            white = not white

        # Creates Squares on the board without pieces
        for i in range(2,6):
            for j in range(0,8):
                spaces[i][j] = Square(None, i, j)

       


        

b = Board()
'''
for i in range(0, 8):
    for j in range(0, 8):
        print( b.get_spaces(i, j).get_material(),  )

'''
