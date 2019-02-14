class Piece:
    def __init__(self, name, player):
        self.name = name
        self.player = player
        self.row = None
        self.col = None
        self.doneDouble = False
    
    def getMoves(self, board, playerNum):

        if self.name == "P1" and self.player == "1" and playerNum == "1":
            return self.pawnMoves1(board)

        elif self.name == "P2" and self.player == "2" and playerNum == "2":
            return self.pawnMoves2(board)

        elif self.name == "K1" and self.player == "1" and playerNum == "1":
            return self.kingMoves(board)

        elif self.name == "K2" and self.player == "2" and playerNum == "2":
            return self.kingMoves(board)

        elif self.name == "Q1" and self.player == "1" and playerNum == "1":
            return self.queenMoves(board)

        elif self.name == "Q2" and self.player == "2" and playerNum == "2":
            return self.queenMoves(board)

        elif self.name == "C1" and self.player == "1" and playerNum == "1":
            return self.castleMoves(board)

        elif self.name == "C2" and self.player == "2" and playerNum == "2":
            return self.castleMoves(board)


    def pawnMoves1(self, board): #bottom_up
        tryMoves = [[self.row-1,self.col-1],[self.row-1,self.col],[self.row-1,self.col+1]]
        doubleMove = [self.row-2,self.col]
        validMoves = []
        
        for move in tryMoves:
            if (move[0] > -1 and move[0] < board.m) and (move[1] > -1 and move[1] < board.m):
                try:
                    piece = board.tiles[move[0]][move[1]]
                except:
                    piece = None


                if piece != None:
                    if self.col == move[1]: #we're moving straight
                        if piece == "~":
                            if self.doneDouble == False:
                                try:
                                    doublePiece = board.tiles[doubleMove[0], doubleMove[1]]
                                except:
                                    doublePiece = None
                                if doublePiece != None and doublePiece == "~":
                                    validMoves.append([[self.row, self.col],[doubleMove[0], doubleMove[1]]])
                                    
                            validMoves.append([[self.row, self.col],[move[0], move[1]]])
                    else:
                        if piece != "~" and piece.player != self.player:
                            validMoves.append([[self.row, self.col],[move[0], move[1]]])
                            
        return validMoves
                        
                

    def pawnMoves2(self, board): #top_down
        tryMoves = [[self.row+1,self.col-1],[self.row+1,self.col],[self.row+1,self.col+1]]
        doubleMove = [self.row+2,self.col]
        validMoves = []
        for move in tryMoves:
            if (move[0] > -1 and move[0] < board.m) and (move[1] > -1 and move[1] < board.m):
                try:
                    piece = board.tiles[move[0]][move[1]]
                except:
                    piece = None

                if piece != None:
                    if self.col == move[1]: #we're moving straight
                        if piece == "~":
                            if self.doneDouble == False:
                                try:
                                    doublePiece = board.tiles[doubleMove[0], doubleMove[1]]
                                except:
                                    doublePiece = None
                                if doublePiece != None and doublePiece == "~":
                                    validMoves.append([[self.row, self.col],[doubleMove[0], doubleMove[1]]])
                                    
                            validMoves.append([[self.row, self.col],[move[0], move[1]]])
                    else:
                        if piece != "~" and piece.player != self.player:
                            validMoves.append([[self.row, self.col],[move[0], move[1]]])
                    
        return validMoves
            

    def castleMoves(self, board):
        validMoves = []
        for x in range(0,4):
            if x == 0:
                addArray = [0,1]
            elif x == 1:
                addArray = [1,0]
            elif x == 2:
                addArray = [0,-1]
            elif x == 3:
                addArray = [-1,0]

            done = False
            move = [self.row, self.col]
                
            while not done:
                move[0] += addArray[0]
                move[1] += addArray[1]
                if (move[0] > -1 and move[0] < board.m) and (move[1] > -1 and move[1] < board.m):
                    try:
                        piece = board.tiles[move[0]][move[1]]
                    except:
                        piece = None
                        done = True

                    if piece != None:
                        if piece != "~" and piece.player != self.player:
                            validMoves.append([[self.row, self.col],[move[0], move[1]]])
                            done = True
                        elif piece == "~":
                            validMoves.append([[self.row, self.col],[move[0], move[1]]])
                        else:
                            done = True
                else:
                    done = True
                    
        return validMoves
                        

    def queenMoves(self, board):
        validMoves = []
        for x in range(0,4):
            if x == 0:
                addArray = [1,1]
            elif x == 1:
                addArray = [1,-1]
            elif x == 2:
                addArray = [-1,1]
            else:
                addArray = [-1,-1]
                
            done = False
            move = [self.row, self.col]
                
            while not done:
                move[0] += addArray[0]
                move[1] += addArray[1]
                if (move[0] > -1 and move[0] < board.m) and (move[1] > -1 and move[1] < board.m):
                    try:
                        piece = board.tiles[move[0]][move[1]]
                    except:
                        piece = None
                        done = True

                    if piece != None:
                        if piece != "~" and piece.player != self.player:
                            validMoves.append([[self.row, self.col],[move[0], move[1]]])
                            done = True
                        elif piece == "~":
                            validMoves.append([[self.row, self.col],[move[0], move[1]]])
                        else:
                            done = True
                else:
                    done = True

        castleMoves = self.castleMoves(board)
        if castleMoves != []:
            for move in castleMoves:
                validMoves.append(move)


        return validMoves


    def kingMoves(self, board):
        tryMoves = [[self.row+1,self.col+1],[self.row+1,self.col-1],[self.row+1,self.col],[self.row-1,self.col+1],\
                    [self.row-1,self.col-1],[self.row-1,self.col],[self.row,self.col+1],[self.row,self.col-1]]
        validMoves = []

        for move in tryMoves:
            if (move[0] > -1 and move[0] < board.m) and (move[1] > -1 and move[1] < board.m):
                try:
                    piece = board.tiles[move[0]][move[1]]
                except:
                    piece = None

                if piece != None:
                    if piece != "~" and piece.player != self.player:
                        validMoves.append([[self.row, self.col],[move[0], move[1]]])
                    elif piece == "~":
                        validMoves.append([[self.row, self.col],[move[0], move[1]]])
        return validMoves
