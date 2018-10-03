import copy
import interactions

class TTT:
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
        

    def goodMove(self, board, playerNum, oppNum, move):
        newBoard = copy.deepcopy(board)
        
        newBoard.fill(move, playerNum)
        
        selfWon = self.win(newBoard, playerNum)
        
        newBoard.fill(move, oppNum)
        
        oppWon = self.win(newBoard, oppNum)

        if selfWon:
            return True
        
        if oppWon:
            return True
        
        else:
            return False
        

    def validMoves(self, board):
        validMoves = []
        for y in range(0,board.n):
            for x in range(0,board.m):
                if board.tiles[y][x] == "*":
                    validMoves.append([y,x])
        return validMoves
    
    def simMachine(self):
        return interactions.TTTInteract()



class Nim:
    
    def win(self,board, placeholder = None): #make modular!
        for item in board.tiles:
            if item != 0:
                return False
            
        return True


    def nimWin(self, board, move):
        winCount = 0
        zeroColCount = 0
        for item in board.tiles:
            if item != 0:
                zeroColCount += 1
                if (item-move[0]) == 0:
                    winCount += 1
            
        if zeroColCount == 1 and winCount == 1:
            return True
        
        else:
            return False
        

    def goodMove(self, board, playerNum, oppNum, move):
        
        selfWon = self.nimWin(board, move)

        if selfWon:
            return True
        
        else:
            return False
        

    def validMoves(self, board):
        validMoves = []
        for x in range(0, board.n):
            if board.tiles[x] != 0:
                for num in range(1, board.tiles[x]+1):
                    validMoves.append([num, x]) #taking "num" from pile "x"
        return validMoves
    

    def simMachine(self):
        return interactions.nimInteract()
        
        
                    

    
        
