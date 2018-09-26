import copy

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
        for y in range (0,board.n):
            for x in range(0,board.m):
                if board.tiles[y][x] == "*":
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
        
        
