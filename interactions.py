import copy
import mockAgent as MA
import boardRules

class TTTInteract:
    def interact(self, board, current, mock, depth, agentNum, mockNum, rules):
        #if something bad happens, return "change"
        #else return "okay"
        
        if current.coreMove != None:
            current.move = current.coreMove
        else:
            current.coreMove = current.getMove(board, rules)
            current.move = current.coreMove

        for x in range(0,depth):
            board.fill(current.move, agentNum)

            if rules.win(board, agentNum):
                current.didLose = False
                current.didWin = True
                return False
            
            elif rules.tie(board):
                current.didLose = False
                current.didWin = False
                current.change = True
                return False
        

            mock.move = mock.getMove(board, mockNum, agentNum, rules)

            
            board.fill(mock.move, mockNum)


            if rules.win(board, mockNum):
                current.didLose = True
                current.didWin = False
                current.change = True
                return False
            
            elif rules.tie(board):
                current.didLose = False
                current.didWin = False
                current.change = True
                return False
            

            current.move = current.getMove(board, rules)

        current.neutral = True
        current.change = True
        return True
    

class nimInteract:
    
    def interact(self, board, current, mock, depth, agentNum, mockNum, rules):
    #if something bad happens, return "change"
    #else return "okay"

        if current.coreMove != None:
            current.move = current.coreMove
            
        else:
            current.coreMove = current.getMove(board, rules)
            current.move = current.coreMove

        for x in range(0,depth):
            board.fill(current.move)

            if rules.win(board):
                current.didLose = False
                current.didWin = True
                current.change = False
                return False
            
            mock.move = mock.getMove(board, mockNum, agentNum, rules)
            
            board.fill(mock.move)

            if rules.win(board):
                current.didLose = True
                current.didWin = False
                current.change = True
                return False
            
            current.move = current.getMove(board, rules)

        current.neutral = True
        current.change = True
        return True
