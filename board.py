class Board:
    def __init__(self, n, m):
        self.tiles = []
        self.n = n
        self.m = m
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
        for y in range(0,self.n):
            for x in range(0,self.m):
                print(str(self.tiles[y][x]) + " ", end = "")
            print()
        print("________")



