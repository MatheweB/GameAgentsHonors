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

    def isFull(self):
        full = True
        for y in self.tiles:
            for x in y:
                if x == "*":
                    full = False

        return full
                    
