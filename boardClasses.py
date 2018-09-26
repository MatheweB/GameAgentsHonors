import board

class Piece:
    def __init__(self,name,constraints, string):
        self.name = None
        self.constraints = constraints
        self.string = string

    def __str__(self):
        return self.string


class TTTBoard(board.Board):
    def __init__(self):
        super().__init__(3, 3)
                    

class NimBoard(board.Board):
    def __init__(self, stackArray):
        super().__init__(1, 3)
        self.tiles = stackArray #user gives in BoardGUI
        self.n = len(stackArray)

        
##        for x in range(0,len(self.tiles)):
##            if self.tiles[x] == "*":
##                self.tiles[x] = 5
        

    def fill(self, move, placeholder): #Change function params to be custom per-game later
        self.tiles[move[1]] -= move[0]
            
        
    
