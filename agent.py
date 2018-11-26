import boardRules as rules
import random

class Agent:
    def __init__(self):
        self.move = None #valid move based on board

        self.change = False #if bad thing happens, change=True and change the coreMove

        self.coreMove = None #move of this given turn

        self.didLose = False

        self.didWin = False

        self.neutral = False

        self.moveNum = 0

    def getMove(self, board, rules):
        
        validMoves = rules.validMoves(board)
        
        if len(validMoves) > 0:
            
            return validMoves[random.randint(0,len(validMoves)-1)]
        
        else:
            print("INVALID MOVE ERROR in getMove")

    def getMoveItem(self):
        return [str(self.coreMove), self.moveNum]
    

    def makeChanges(self, board, rules, topMove):
            
        if self.change == True:
            if topMove != None:
                self.coreMove = topMove
            else:
                self.coreMove = self.getMove(board, rules)
                
        self.moveNum = 0
        self.change = False
        
        self.move = None
        return self.moveNum

