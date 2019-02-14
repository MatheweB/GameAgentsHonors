import copy
import interactions

class TTT:
    def is_indiff(self):
        return False
    
    def win(self,board, playerNum):
        
        if board.tiles[0][0] == playerNum and board.tiles[0][1] == playerNum and board.tiles[0][2] == playerNum:
            return True

        if board.tiles[1][0] == playerNum and board.tiles[1][1] == playerNum and board.tiles[1][2] == playerNum:
            return True

        if board.tiles[2][0] == playerNum and board.tiles[2][1] == playerNum and board.tiles[2][2] == playerNum:
            return True

        if board.tiles[0][0] == playerNum and board.tiles[1][0] == playerNum and board.tiles[2][0] == playerNum:
            return True

        if board.tiles[0][1] == playerNum and board.tiles[1][1] == playerNum and board.tiles[2][1] == playerNum:
            return True

        if board.tiles[0][2] == playerNum and board.tiles[1][2] == playerNum and board.tiles[2][2] == playerNum:
            return True

        if board.tiles[0][0] == playerNum and board.tiles[1][1] == playerNum and board.tiles[2][2] == playerNum:
            return True

        if board.tiles[0][2] == playerNum and board.tiles[1][1] == playerNum and board.tiles[2][0] == playerNum:
            return True

        return False

    def tie(self, board):
        full = True
        for y in board.tiles:
            for x in y:
                if x == "*":
                    full = False

        return full
        

    def goodMove(self, board, move, playerNum, mockNum, isRec = False):
        newBoard = copy.deepcopy(board)
        
        newBoard.fill(move, playerNum)
        
        selfWon = self.win(newBoard, playerNum)

        if selfWon:
            return True

        else:
            return False
        

    def validMoves(self, board, playerNum = None):
        validMoves = []
        for y in range(0,board.m):
            for x in range(0,board.n):
                if board.tiles[y][x] == "*":
                    validMoves.append([y,x])
        return validMoves
    
    def simMachine(self):
        return interactions.TTTInteract()



class Nim:
    
    def is_indiff(self):
        return True
    
    def win(self,board):
        for item in board.tiles:
            if item != 0:
                return False
            
        return True


    def nimWin(self, board, move, isRec):

        #if isRec:          
        testB = copy.deepcopy(board)
        testB.fill(move)

        justWon = True
        for item in testB.tiles:
            if item != 0:
                justWon = False

        return justWon

    def getNimVal(self, board, move):
        boardNew = copy.deepcopy(board)

        boardNew.fill(move)

        nimSum = 0
        for item in boardNew.tiles:
            nimSum ^= item

        return nimSum
            

    def goodMove(self, board, move, isRec = False):
            
        selfWon = self.nimWin(board, move, isRec)

        if selfWon:
            return True
        
        else:
            return False
        

    def validMoves(self, board, playerNum = None):
        validMoves = []
        for x in range(0, board.n):
            if board.tiles[x] != 0:
                for num in range(1, board.tiles[x]+1):
                    validMoves.append([num, x]) #taking "num" from pile "x"
        return validMoves
    

    def simMachine(self):
        return interactions.nimInteract()


class Minichess:
    
    def is_indiff(self):
        return False
    
    def win(self,board,playerNum):
        if playerNum == "1":
            if board.king2 == None:
                return True

        elif playerNum == "2":
            if board.king1 == None:
                return True

        else:
            return False
        

    def tie(self, board):
        return False
        

    def goodMove(self, board, move, playerNum, mockNum, isRec = False):
        newBoard = copy.deepcopy(board)
        
        newBoard.fill(move, playerNum)

        selfWon = self.win(newBoard, playerNum)

        if selfWon:
            return True

        else:
            return False
        

    def validMoves(self, board, playerNum):
        validMoves = []
        for y in range(0,board.m):
            for x in range(0,board.n):
                piece = board.tiles[y][x]
                if piece != "~":
                    moves = piece.getMoves(board, playerNum)
                    if moves != None and moves != []:
                        for move in moves:
                            validMoves.append(move) #Old location, New location

        return validMoves
                
    
    def simMachine(self):
        return interactions.TTTInteract()
        
