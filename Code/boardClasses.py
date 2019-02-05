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

    def userUpdate(self, playerNum):
        y = int(input("row: "))
        x = int(input("column: "))
        
        move = []
        move.append(y)
        move.append(x)
        self.fill(move, playerNum)
                   

class NimBoard(board.Board):
    def __init__(self, stackArray):
        super().__init__(1, 3)
        self.tiles = stackArray #user gives in BoardGUI
        self.n = len(stackArray)
        
    def fill(self, move, placeholder = None): #make modular!
        self.tiles[move[1]] -= move[0]

    def userUpdate(self):
        col = int(input("col: "))
        value = int(input("number: "))
        
        move = []
        move.append(value)
        move.append(col)
        self.fill(move)
            
        
    
