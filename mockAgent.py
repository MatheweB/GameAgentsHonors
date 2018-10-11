import boardRules
import random
import operator

class Mocker:
    def __init__(self):
        self.move = None #valid move based on board

    def getMove(self, board, rules, playerNum = None, mockNum = None):
        
        validMoves = rules.validMoves(board)

        if len(validMoves) > 0:
            if playerNum == None and mockNum == None:
                smartMove = (self.makeSmartMove(validMoves, board, rules))
            else:
                smartMove = (self.makeSmartMove(validMoves, board, rules, playerNum, mockNum))
                
            return smartMove
                
        else:
            print("INVALID MOVE ERROR in getMove MockAgent")


    def makeSmartMoveNim(self, validMoves, board, rules): #TOO SMART
        smartArray= []
        for move in validMoves:
            nimVal = rules.getNimVal(board, move)
            smartArray.append([nimVal, move])
            
        smartArray.sort(key=operator.itemgetter(0))
        return smartArray[0][1]
        

    def makeSmartMove(self, validMoves, board, rules, playerNum = None, mockNum = None):
        goodMoves = []
        if playerNum == None and mockNum == None:
            for move in validMoves:
                if rules.goodMove(board, move):
                    goodMoves.append(move)
        else:
            for move in validMoves:
                if rules.goodMove(board, move, playerNum, mockNum):
                    goodMoves.append(move)

        #print(goodMoves)
        if len(goodMoves) > 0:
            return goodMoves[random.randint(0,len(goodMoves)-1)]
            
        else:
            return validMoves[random.randint(0,len(validMoves)-1)]
