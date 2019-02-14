import random

class Mocker:
    def __init__(self):
        self.move = None #valid move based on board
        

    def getMove(self, board, rules, mockNum = None, playerNum = None):

        #Mocknum is opposite of playernum

        validMoves = rules.validMoves(board, mockNum)

        if len(validMoves) > 0:
            if playerNum == None and mockNum == None:
                smartMove = (self.makeSmartMove(validMoves, board, rules))
            else:
                smartMove = (self.makeSmartMove(validMoves, board, rules, mockNum, playerNum))
                
            return smartMove
        
        else:
            print("INVALID MOVE ERROR in getMove MockAgent")

    def makeSmartMove(self, validMoves, board, rules, mockNum = None, playerNum = None):
        wonMoves = []
        neutralMoves = []
        goodMoves = []
        if playerNum == None and mockNum == None:
            for move in validMoves:
                result = rules.goodMove(board, move)
                if result == True:
                    wonMoves.append(move)
                elif result == False:
                    neutralMoves.append(move)

        else:
            for move in validMoves:
                if rules.goodMove(board, move, mockNum, playerNum):
                    goodMoves.append(move)

        #print(goodMoves)
        if len(wonMoves) > 0:
            return wonMoves[random.randint(0,len(wonMoves)-1)]
        elif len(neutralMoves) > 0:
            return neutralMoves[random.randint(0,len(neutralMoves)-1)]
        elif len(goodMoves) > 0:
            return goodMoves[random.randint(0,len(goodMoves)-1)]
        else:
            return validMoves[random.randint(0,len(validMoves)-1)]
