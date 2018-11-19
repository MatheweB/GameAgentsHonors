import copy
import interactions
import runSim as Sim

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
        
        newBoard.fill(move, mockNum)
        
        oppWon = self.win(newBoard, mockNum)

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

            
##        if justWon == True:
##            return True
##        
##        else:
##            count = 0
##            for item in testB.tiles:
##                if item != 0:
##                    count += 1
##                    
##            if count%2 != 0:
##                return False
##            
##            else:
##                return True
            
##        else:
##            simRunner = Sim.runSim()
##            
##            gameRules = Nim()
##            thisBoard = copy.deepcopy(board)
##
##            numAgents = 1
##            simNum = 1
##            depth = 200
##            
##            turnNum = 2
##            done = None
##            
##            for x in range(0, turnNum):
##                if x == 0:
##                    thisBoard.fill(move)
##                    if self.win(thisBoard):
##                        return "won"
##                else:
##                    newBoard, bestMoves, done = simRunner.run_indiff(numAgents, simNum, Nim(), thisBoard, depth, isRec = True, printStuff = False)
##                    thisBoard = newBoard
##                    
##                    if bestMoves[0][2] == "lost":
##                        return "lost"                    
##                    if done == True:
##                        return "won"
##
##                newBoard, bestMoves, done, isCert = simRunner.run_indiff(numAgents, simNum, Nim(), thisBoard, depth, isRec = True, printStuff = False)
##                thisBoard = newBoard
##                if bestMoves[0][2] == "lost":
##                    return "won" 
##                if done == True:
##                    return "lost"
##
##            return "neutral"


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
        

    def validMoves(self, board):
        validMoves = []
        for x in range(0, board.n):
            if board.tiles[x] != 0:
                for num in range(1, board.tiles[x]+1):
                    validMoves.append([num, x]) #taking "num" from pile "x"
        return validMoves
    

    def simMachine(self):
        return interactions.nimInteract()
        
