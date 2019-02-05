import copy
import mockAgent as MA
import boardRules

class TTTInteract:
    def interact(self, board, current, mock, depth, rules, agentNum, mockNum, isRec = False):
        #if something bad happens, return "change"
        #else return "okay"
        
        if current.coreMove != None:
            current.move = current.coreMove
        else:
            current.coreMove = current.getMove(board, rules)
            current.move = current.coreMove
            
        moves = 0
        mockMove = None

        for x in range(0,depth):
            board.fill(current.move, agentNum)
            moves += 1

            if rules.win(board, agentNum):
                current.didLose = False
                current.didWin = True
                current.change = False
                current.moveNum = moves
                return False
            
            elif rules.tie(board):
                current.didLose = False
                current.didWin = False
                current.change = True
                current.moveNum = moves
                return False
            mockMove = mock.getMove(board, rules, mockNum, agentNum, isRec = isRec)
            board.fill(mockMove, mockNum)


            if rules.win(board, mockNum):
                current.didLose = True
                current.didWin = False
                current.change = True
                current.moveNum = moves
                return False
            
            elif rules.tie(board):
                current.didLose = False
                current.didWin = False
                current.change = True
                current.moveNum = moves
                return False
            
            current.move = current.getMove(board, rules)

        current.neutral = True
        current.change = True
        current.didLose = False
        current.didWin = False
        current.moveNum = moves
        return True
    

class nimInteract:
    
    def interact(self, board, current, mock, depth, rules, isRec = False):
    #if something bad happens, return "change"
    #else return "okay"

        if current.coreMove != None:
            current.move = current.coreMove
            
        else:
            current.coreMove = current.getMove(board, rules)
            current.move = current.coreMove
            
        moves = 0
        for x in range(0,depth):
            board.fill(current.move)
            moves += 1

            if rules.win(board):
                current.didLose = False
                current.didWin = True
                current.change = True
                current.moveNum = moves
                return False
            
            mock.move = mock.getMove(board, rules, isRec = isRec)
            board.fill(mock.move)

            if rules.win(board):
                current.didLose = True
                current.didWin = False
                current.change = False
                current.moveNum = moves
                return False
            
            current.move = current.getMove(board, rules)

        current.neutral = True
        current.change = False
        current.moveNum = moves
        return True
