import boardRules
import random

class Mocker:
    def __init__(self):
        self.move = None #valid move based on board

    def getMove(self, board, mockNum, oppNum, rules): #TODO: IMPLEMENT RULES
        TTTRules = boardRules.TTT()
        
        validMoves = TTTRules.validMoves(board)

        if len(validMoves) > 0:
            smartMove = (self.makeSmartMove(validMoves, board, mockNum, oppNum))
            return smartMove
                
        else:
            print("INVALID MOVE ERROR in getMove MockAgent")

    def makeChanges(self, board):
        if self.change == True:
            self.coreMove = self.getMove(board)
        self.change = False
        self.move = None

    def makeSmartMove(self, validMoves, board, mockNum, oppNum):
        TTTRules = boardRules.TTT()
        goodMoves = []
        for move in validMoves:
            if TTTRules.goodMove(board, mockNum, oppNum, move):
                goodMoves.append(move)

        if len(goodMoves) > 0:
            return goodMoves[random.randint(0,len(goodMoves)-1)]
            
        else:
            return validMoves[random.randint(0,len(validMoves)-1)]
