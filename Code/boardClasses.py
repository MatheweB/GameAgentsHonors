import board
import piece as Pieces
import boardRules as rules

class TTTBoard(board.Board):
    def __init__(self):
        super().__init__(3, 3)

    def userUpdate(self, playerNum):
        y = int(input("row: "))
        x = int(input("column: "))
        
        move = [y,x]
        self.fill(move, playerNum)
                   
class NimBoard(board.Board):
    def __init__(self, stackArray):
        super().__init__(1, 3)
        self.tiles = stackArray #user gives in BoardGUI
        self.n = len(stackArray)
        
    def fill(self, move, placeholder = None): #make modular!
        self.tiles[move[1]] -= move[0]

    def userUpdate(self):
        col = int(input("col: "))
        value = int(input("number: "))
        
        move = [value,col]
        self.fill(move)

class ChessBoard(board.Board):
    def __init__(self):
        super().__init__(5, 4)
        
        self.tiles = [[Pieces.Piece("C2", "2"),Pieces.Piece("Q2", "2"),Pieces.Piece("K2", "2"),Pieces.Piece("C2", "2")],\
                      [Pieces.Piece("P2", "2"),Pieces.Piece("P2", "2"),Pieces.Piece("P2", "2"),Pieces.Piece("P2", "2")],\
                      ["~", "~", "~", "~"],\
                      [Pieces.Piece("P1", "1"),Pieces.Piece("P1", "1"),Pieces.Piece("P1", "1"),Pieces.Piece("P1", "1")],\
                      [Pieces.Piece("C1", "1"),Pieces.Piece("Q1", "1"),Pieces.Piece("K1", "1"),Pieces.Piece("C1", "1")]]

        for y in range(0,self.m):
            for x in range(0,self.n):
                piece = self.tiles[y][x]
                if piece != "~":
                    piece.row = y
                    piece.col = x
        
        self.king1 = [4,2] #KEEP TRACK!!
        self.king2 = [0,2]

    def fill(self, move, placeholder = None):
        #We update our king's position/status first
        movingPiece = self.tiles[move[0][0]][move[0][1]] # Old
        targetPiece = self.tiles[move[1][0]][move[1][1]] # Desired

        if targetPiece != "~" and targetPiece.name == "K2":
            self.king2 = None
        elif targetPiece != "~" and targetPiece.name == "K1":
            self.king1 = None

        if movingPiece.name == "K2":
            self.king2 = [move[0][0], move[0][1]]
        elif movingPiece.name == "K1":
            self.king1 =[move[0][0], move[0][1]]

        if movingPiece.name == "P1" or movingPiece.name == "P2":
            if movingPiece.doneDouble == False:
                self.tiles[move[0][0]][move[0][1]].doneDouble = True


        #we take the old piece and move it to the desired spot
        self.tiles[move[1][0]][move[1][1]] = self.tiles[move[0][0]][move[0][1]]

        #we set the old spot to emoty/'~'
        self.tiles[move[0][0]][move[0][1]] = "~"

        # Update piece row and column variables for piece
        self.tiles[move[1][0]][move[1][1]].row = move[1][0]
        self.tiles[move[1][0]][move[1][1]].col = move[1][1]
        

    def userUpdate(self, playerNum):
        ChessRules = rules.Minichess()
        validMoves = ChessRules.validMoves(self,playerNum)

        allGood = False
        while not allGood:
            print("You are player " + str(playerNum) + ". Choose piece: ")

            valid = False
            while not valid:
                try:
                    prow = int(input("row: "))
                    pcol = int(input("col: "))
                    piece = self.tiles[prow][pcol]
                    pieceName = piece.name
                    if int(pieceName[1]) != int(playerNum):
                        print(pieceName + "? That's not your piece! Try again.")
                        print()
                    else:
                        valid = True
                except:
                    print("Empty piece!")
                    print("Try picking a piece again.")
            print("---------------")
            print()
            print("You chose " + pieceName + ". Choose new location: ")
            
            valid = False
            validMoveOverall = True
            while not valid:
                try:
                    row = int(input("row: "))
                    col = int(input("col: "))
                    move = [[prow,pcol],[row,col]]

                    if [[prow,pcol],[row,col]] in validMoves:
                        self.fill(move)
                        valid = True
                    else:
                        valid = True
                        validMoveOverall = False
                except:
                    print("Invalid new location, try again!")
                    print()

            if not validMoveOverall:
                print("Invalid move, try again!")
                print()
                self.printBoard()
                print()
            else:
                allGood = True
                
        print("---------------")
        print()
                
        

    def printBoard(self):
        for y in range(0, self.m):
            for x in range(0, self.n):
                try:
                    pieceName = self.tiles[y][x].name
                except:
                    pieceName = " □"

                print(str(pieceName) + " ", end="")
            print()
        print("________")
    
            
        
    
