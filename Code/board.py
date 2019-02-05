class Board:
    def __init__(self, m, n):
        self.tiles = []
        self.m = m
        self.n = n

        if self.m == 1:
            for y in range (0,self.n):
                self.tiles.append("*")
            
        else:
            for y in range (0,n):
                self.tiles.append([])
                for x in range(0,m):
                    self.tiles[y].append("*")

    def fill(self, position, piece): #implement fill rules 
        try:
            self.tiles[position[0]][position[1]] = piece
        except:
            print("SOMETHING WENT VERY WRONG in fill")
            exit(5)
            
    def printBoard(self):

        if self.m == 1:
            for y in range (0,self.n):
                print(str(self.tiles[y]) + " ", end = "")
            print()
            print("________")
        

        else:
            for y in range(0,self.n):
                for x in range(0,self.m):
                    print(str(self.tiles[y][x]) + " ", end = "")
                print()
            print("________")



