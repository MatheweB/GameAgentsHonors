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

        self.playerNumber = None

    def getMove(self, board, rules):
        validMoves = rules.validMoves(board, self.playerNumber)
        
        if len(validMoves) > 0:
            
            return validMoves[random.randint(0,len(validMoves)-1)]
        
        else:
            print("INVALID MOVE ERROR in getMove")

    def getMoveItem(self):
        return [str(self.coreMove), self.moveNum]
    

    def makeChanges(self, board, rules, topMove, searchingBad):
        if searchingBad:
            if self.change == True: # I had a bad move
                self.coreMove = self.coreMove # keep it
            elif self.change == False: # I had a good move
                self.coreMove =  self.getMove(board, rules) #search!
        else:
            if self.change == True: # I had a bad move
                self.coreMove = topMove #trust the population
            elif self.change == False: # I had a good move
                self.coreMove =  self.getMove(board, rules) # keep it
                
 
        self.moveNum = 0
        self.change = False
        
        self.move = None
        return self.moveNum
