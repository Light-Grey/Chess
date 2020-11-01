#!/usr/bin/env python3
import os

# Functionality for a Square on the board
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

# King piece Functionality
class King:
    # Initialization function
    def __init__(self, white):
        self.alive = True
        self.white = white
        if white:
            self.code = "\u2654"
        else:
            self.code = "\u265A"

    # Getters/Setters for material and coordinates
    def set_white(self, white):
        self.white = white

    def get_white(self):
        return self.white

    def set_alive(self, alive):
        self.alive = alive

    def get_alive(self):
        return self.alive

    def get_name(self):
        return "King"
    
    def get_code(self):
        return self.code

    def valid_move(self, start, end):
        if end.get_material().get_white() == self.get_white():
            return False
        
        x_move = abs( end.get_x() - start.get_x() )
        y_move = abs( end.get_y() - start.get_y() )

        if x_move < 2 and y_move < 2:
            return True

        # IMPLEMENT: Castling functionality


# Queen piece functionality( Rook + Bishop )
class Queen:
    def __init__(self, white):
        self.alive = True
        self.white = white
        if white:
            self.code = "\u2655"
        else:
            self.code = "\u265B"

    # Getters/Setters for color and life status
    def set_white(self, white):
        self.white = white

    def get_white(self):
        return self.white

    def set_alive(self, alive):
        self.alive = alive

    def get_alive(self):
        return self.alive

    def get_name(self):
        return "Queen"

    def get_code(self):
        return self.code
    
    # Checks for moving in diagonal or straight lines
    def valid_move(self, start, end):
        if end.get_material() != None:
            if end.get_material().get_white() == self.get_white():
                return False
            
        x_move = abs( end.get_x() - start.get_x() )
        y_move = abs( end.get_y() - start.get_y() )
        return x_move * y_move == 0 or x_move == y_move

        # IMPLEMENT: Check for collision of other pieces


# Rook piece functionality
class Rook:
    def __init__(self, white):
        self.alive = True
        self.white = white
        if white:
            self.code = "\u2656"
        else:
            self.code = "\u265C"

    def set_white(self, white):
        self.white = white

    def get_white(self):
        return self.white

    def set_alive(self, alive):
        self.alive = alive

    def get_alive(self):
        return self.alive

    def get_name(self):
        return "Rook"

    def get_code(self):
        return self.code

    def valid_move(self, start, end):
        if end.get_material() != None:
            if end.get_material().get_white() == self.get_white():
                return False
        
        x_move = abs( end.get_x() - start.get_x() )
        y_move = abs( end.get_y() - start.get_y() )
        return x_move * y_move == 0


# Bishop piece functionality
class Bishop:
    def __init__(self, white):
        self.alive = True
        self.white = white
        if white:
            self.code = "\u2657"
        else:
            self.code = "\u265D"

    def set_white(self, white):
        self.white = white

    def get_white(self):
        return self.white

    def set_alive(self, alive):
        self.alive = alive

    def get_alive(self):
        return self.alive

    def get_name(self):
        return "Bishop"

    def get_code(self):
        return self.code

    def valid_move(self, start, end):
        if end.get_material() != None:
            if end.get_material().get_white() == self.get_white():
                return False

        # Find difference in x&y positions
        x_move = end.get_x() - start.get_x()
        y_move = end.get_y() - start.get_y()
        
        return abs(x_move) == abs(y_move)

# Night piece functionality
class Night:
    def __init__(self, white):
        self.alive = True
        self.white = white
        if white:
            self.code = "\u2658"
        else:
            self.code = "\u265E"

    def set_white(self, white):
        self.white = white

    def get_white(self):
        return self.white

    def set_alive(self, alive):
        self.alive = alive

    def get_alive(self):
        return self.alive

    def get_name(self):
        return "Night"
    
    def get_code(self):
        return self.code

    def valid_move(self, start, end):
        if end.get_material() != None:
            if end.get_material().get_white() == self.get_white():
                return False
        
        x_move = abs( end.get_x() - start.get_x() )
        y_move = abs( end.get_y() - start.get_y() )
        return x_move * y_move == 2
        
        

# Pawn piece functionality
class Pawn:
    def __init__(self, white):
        self.alive = True
        self.white = white
        self.hasMoved = False
        if white:
            self.code = "\u2659"
        else:
            self.code = "\u265F"

    def set_white(self, white):
        self.white = white

    def get_white(self):
        return self.white

    def set_alive(self, alive):
        self.alive = alive

    def get_alive(self):
        return self.alive
    
    def set_hasMoved(self):
        self.hasMoved = True

    def get_hasMoved(self):
        return self.hasMoved
    
    def get_name(self):
        return "Pawn"

    def get_code(self):
        return self.code

    def valid_move(self, start, end):
        if end.get_material() != None:
            if end.get_material().get_white() == self.get_white():
                return False

        x_move = end.get_x() - start.get_x()
        y_move = abs(end.get_y() - start.get_y())

        # For white pawns
        if self.get_white():
            if not self.get_hasMoved():
                # Moves forward two spaces
                if x_move == 2 and y_move == 0:
                    return True

            # Moves forward one space
            elif x_move == 1 and y_move == 0:
                return True
            # Takes piece
            elif x_move == 1 and y_move == 1 and end.get_material != None:
                return True
        # For black pawns
        else:
            if not get_hasMoved():
                # Moves forward two spaces
                if x_move == -2 and y_move == 0:
                    return True

            # Moves forward one space
            elif x_move == -1 and y_move == 0:
                return True
            # Takes piece
            elif x_move == -1 and y_move == 1 and end.get_material != None:
                return True

        return False


# Functionality for the board itself
class Board:
    def __init__(self):
        rows, cols = (8, 8)
        self.spaces = [[Square(None,0,0)] * 8 for _ in range(rows)]
        self.createBoard(self.spaces)

    def get_spaces(self, i, j):
        return self.spaces[i][j]

    def set_spaces(self, i, j, material):
        self.spaces[i][j] = Square(material, i, j)
    

    def createBoard(self, spaces):
        # Boolean variable to change color of pieces (expels repeated code)
        white = True

        # Creates non-pawn pieces for both sides
        for i in range(0,8,7):
            spaces[i][0] = Square(Rook(white),   i, 0)
            spaces[i][1] = Square(Night(white), i, 1)
            spaces[i][2] = Square(Bishop(white), i, 2)
            spaces[i][3] = Square(Queen(white),  i, 3)
            spaces[i][4] = Square(King(white),   i, 4)
            spaces[i][5] = Square(Bishop(white), i, 5)
            spaces[i][6] = Square(Night(white), i, 6)
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

       
##List of things we need in game
##1: Start the game and give player ability to move CHECK
##2: Ensure only white can move on white's turn, vice versa CHECK
##3: Check for interference when moving (e.g. a piece in the way of where a rook wants to move)
##4: ???
# The actual game setup!
class Game:
    def __init__(self):
        self.whiteTurn = True
        self.gameStatus = "Active"
        self.board = Board()

    # Functions regarding game status (Active, or many states of over)
    def gameOver(self):
        return self.gameStatus != "Active"

    def setStatus(self, status):
        self.gameStatus = status

    # Functions regarding switching turns, and preventing out of turn moves
    def switchTurn(self):
        self.whiteTurn = not self.whiteTurn

    def inTurn(self, materialColor):
        if( whiteTurn == materialColor):
            return True
        return False

    # Checks if a player can make this move
    # start and end will both be lists with two elements (the coordinates)
    def playerMove(self, start, end):
        # Checks if the square has material occupying it at all
        startMove = self.board.get_spaces(int(start[0]), int(start[1])).get_material()
        if (startMove == None):
            return False

        # Gets the starting and ending square from the board 
        startSquare = self.board.get_spaces(int(start[0]),int(start[1]))
        endSquare = self.board.get_spaces(int(end[0]),int(end[1]))

        return self.makeMove(startSquare, endSquare)

    
    # Validates if move is possible including:
    #   If valid color
    #   If pieces are in way
    #   if king will be put in check
    def makeMove (self, startSquare, endSquare):
        # Checks if piece to be moved matches current player
        if (startSquare.get_material().get_white() != self.whiteTurn):
            return False

        # Checks if the piece can move according to the material's internal rules
        if (not startSquare.get_material().valid_move(startSquare, endSquare)):
            return False

        # Checks for pieces that cannot hop over pieces, if there is a piece in the way
        materialName = startSquare.get_material().get_name()
        if (materialName == "Night"):
            return True
        elif (materialName == "Pawn"):
            # implement
            if(endSquare.get_x() - startSquare.get_x() == 2):
                if(self.board.get_spaces(startSquare.get_x() + 1, startSquare.get_y() != None)):
                   return False
                
               
            return True
        elif (materialName == "Bishop"):
            # Find difference in x&y positions
            x_move = endSquare.get_x() - startSquare.get_x()
            y_move = endSquare.get_y() - startSquare.get_y()
            
            # Makes sure the move is legal, and then ensures there aren't
            # any intermediary pieces blocking the action
            
            if x_move > 0:
                xPosDiff = 1
            else:
                xPosDiff = -1

            if y_move > 0:
                yPosDiff = 1
            else:
                yPosDiff = -1

            yPosTemp = startSquare.get_y() + yPosDiff

            for i in range(startSquare.get_x() + xPosDiff, endSquare.get_x(), xPosDiff):
                if(self.board.get_spaces(i, yPosTemp).get_material != None):
                    return False
                yPosTemp += yPosDiff

            # Passed every check, is legal!
            return True

        # Finished! I hope c:
        elif (materialName == "Rook"):
            # Checks initially if moved within it's collumn
            if ( endSquare.get_x() - startSquare.get_x() != 0 ):
                iterator = 0
                if (endSquare.get_x() - startSquare.get_x() > 0):
                    iterator = 1
                else:
                    iterator = -1

                # Iterates through squares, looking for material. If found, returns false
                for i in range(startSquare.get_x(), endSquare.get_x(), iterator):
                    if(self.board.get_spaces(i, startSquare.get_y()).get_material() != None):
                        return False
                return True

            # else, it moved within its row
            elif ( endSquare.get_y() - startSquare.get_y() != 0 ):
                iterator = 0
                if (endSquare.get_y() - startSquare.get_y() > 0):
                    iterator = 1
                else:
                    iterator = -1

                # Iterates through squares, looking for material. If found, returns false
                for i in range(startSquare.get_y(), endSquare.get_y(), iterator):
                    if(self.board.get_spaces(startSquare.get_x(), i).get_material() != None):
                        return False
                return True
            else:
                return False

        # Done, copied code from rook and bishop, may need more testing
        elif (materialName == "Queen"):
            # implement
            x_move = abs( endSquare.get_x() - startSquare.get_x() )
            y_move = abs( endSquare.get_y() - startSquare.get_y() )
            return x * y == 0 or x == y

            # Moved like a bishop
            if( x_move == y_move):
                # Find difference in x&y positions
                x_move = endSquare.get_x() - startSquare.get_x()
                y_move = endSquare.get_y() - startSquare.get_y()
                
                # Makes sure the move is legal, and then ensures there aren't
                # any intermediary pieces blocking the action
                
                if x_move > 0:
                    xPosDiff = 1
                else:
                    xPosDiff = -1

                if y_move > 0:
                    yPosDiff = 1
                else:
                    yPosDiff = -1

                yPosTemp = startSquare.get_y() + yPosDiff

                for i in range(startSquare.get_x() + xPosDiff, end.get_x(), xPosDiff):
                    if(self.board.get_spaces(i, yPosTemp).get_material != None):
                        return False
                    yPosTemp += yPosDiff

                # Passed every check, is legal!
                return True
                
                
            # Moved like a rook
            else:

                # Checks initially if moved within it's collumn
                if ( endSquare.get_x() - startSquare.get_x() != 0 ):
                    iterator = 0
                    if (endSquare.get_x() - startSquare.get_x() > 0):
                        iterator = 1
                    else:
                        iterator = -1

                    # Iterates through squares, looking for material. If found, returns false
                    for i in range(startSquare.get_x(), endSquare.get_x(), iterator):
                        if(self.board.get_spaces(i, startSquare.get_y()).get_material() != None):
                            return False
                    return True

                # else, it moved within its row
                elif ( endSquare.get_y() - startSquare.get_y() != 0 ):
                    iterator = 0
                    if (endSquare.get_y() - startSquare.get_y() > 0):
                        iterator = 1
                    else:
                        iterator = -1

                    # Iterates through squares, looking for material. If found, returns false
                    for i in range(startSquare.get_y(), endSquare.get_y(), iterator):
                        if(self.board.get_spaces(startSquare.get_x(), i).get_material() != None):
                            return False
                    return True
                else:
                    return False

        elif (materialName == "King"):
            # implement
            # I think the internal king function covers all movement, but
            # still need to implement Check checking
            return True


    
g = Game()


# keep going!
#Main game loop?
while not g.gameOver():
    
    validMove = False
    repeat = False
    while(not validMove):
        os.system('cls') # Windows
        # Prints current gameboard
        if repeat:
            print("Invalid move. Please pick a valid move.")
            print()
        print("  A B C D E F G H")
        for i in range(7, -1, -1):
            print(i + 1, end=" ")
            for j in range(0, 8):
                if(g.board.get_spaces(i,j).get_material() == None):
                    print(".", end=" ")
                else:
                    #print(g.board.get_spaces(i,j).get_material().get_code(), end=" ")
                    # Gets piece letter
                    name = g.board.get_spaces(i,j).get_material().get_name()
                    if(g.board.get_spaces(i,j).get_material().get_white()):
                        #print("W", end="" )
                        name = name
                    else:
                        #print("B", end="" )
                        name = name.lower()
                    
                    print(name[0], end=" ")
            print()

        # Prompts player for move
        playInitial = input("Enter the starting square: ")
        playFinal = input("Enter the ending square: ")


        # Does some conversions from normal chess move name to 2d array setup
        if( playInitial[0].lower() == 'a'):
            playInitial = "0" + playInitial[1]
        elif( playInitial[0].lower() == 'b'):
            playInitial = "1" + playInitial[1]
        elif( playInitial[0].lower() == 'c'):
            playInitial = "2" + playInitial[1]
        elif( playInitial[0].lower() == 'd'):
            playInitial = "3" + playInitial[1]
        elif( playInitial[0].lower() == 'e'):
            playInitial = "4" + playInitial[1]
        elif( playInitial[0].lower() == 'f'):
            playInitial = "5" + playInitial[1]
        elif( playInitial[0].lower() == 'g'):
            playInitial = "6" + playInitial[1]
        elif( playInitial[0].lower() == 'h'):
            playInitial = "7" + playInitial[1]

        playInitial = playInitial[0] + str( int(playInitial[1]) - 1 )
        
        if( playFinal[0].lower() == 'a'):
            playFinal = "0" + playFinal[1]
        elif( playFinal[0].lower() == 'b'):
            playFinal = "1" + playFinal[1]
        elif( playFinal[0].lower() == 'c'):
            playFinal = "2" + playFinal[1]
        elif( playFinal[0].lower() == 'd'):
            playFinal = "3" + playFinal[1]
        elif( playFinal[0].lower() == 'e'):
            playFinal = "4" + playFinal[1]
        elif( playFinal[0].lower() == 'f'):
            playFinal = "5" + playFinal[1]
        elif( playFinal[0].lower() == 'g'):
            playFinal = "6" + playFinal[1]
        elif( playFinal[0].lower() == 'h'):
            playFinal = "7" + playFinal[1]

        playFinal = playFinal[0] + str( int(playFinal[1]) - 1 )


        playInitial = playInitial[1] + playInitial[0]
        playFinal = playFinal[1] + playFinal[0]

        
        validMove = g.playerMove(playInitial, playFinal)
        repeat = True
    # Moves piece, sets initial square to null
    g.board.set_spaces( int(playFinal[0]),int(playFinal[1]),
                            g.board.get_spaces(int(playInitial[0]),
                                               int(playInitial[1])).get_material())
                        
    g.board.set_spaces( int(playInitial[0]),int(playInitial[1]), None)
    g.switchTurn()

    
    
        

'''
for i in range(0, 8):
    for j in range(0, 8):
        if(g.board.get_spaces(i,j).get_material() == None):
            print("XX", end=" ")
        else:
            #print(g.board.get_spaces(i,j).get_material().get_code(), end=" ")
            
            if(g.board.get_spaces(i,j).get_material().get_white()):
                print("W", end="" )
            else:
                print("W", end="" )
            name = g.board.get_spaces(i,j).get_material().get_name()
            print(name[0], end=" ")
    print()
'''
