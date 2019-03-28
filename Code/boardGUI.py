import copy
import boardClasses as Board
import boardRules as Rules
import runSim as Sim

def main():
    simRunner = Sim.runSim()
    
    #gameRules = Rules.TTT()
    #OGBoard = Board.TTTBoard()

    #gameRules = Rules.Nim()
    #OGBoard = Board.NimBoard([1,2,3,4,5])

    gameRules = Rules.Minichess()
    OGBoard = Board.ChessBoard()
    
    board = copy.deepcopy(OGBoard)

    playFirst = False
    playSecond = True
    userUpdate = False

    numAgents = 50 #220
    simNum = 100 #220
    depth = 20
    
    gameNum = 200

    for game in range(0,gameNum):



        if gameRules.is_indiff(): # An indifferent game
            if playFirst:
                board.printBoard()

            moveCount = 0
            done = False
            
            while done == False:
                if playFirst:
                    if moveCount%2 == 0:
                        userUpdate = True
                    else:
                        userUpdate = False

                elif playSecond:
                    if moveCount%2 == 1:
                        userUpdate = True
                    else:
                        userUpdate = False
                
                newBoard, topMoves, done, isCert = simRunner.run_indiff(numAgents, simNum, gameRules, board, depth, userUpdate)
                
                if userUpdate == True:
                    board = newBoard

                else:
                    #print(isCert)
                    topMove = topMoves[0][0]
                    board.fill(topMove)
                    
                #if topMoves != None:
                    #print(topMoves)

                board.printBoard()
                
                moveCount += 1
                
            board = copy.deepcopy(OGBoard)
            

        else: # A normal game

            if playFirst:
                board.printBoard()
            
            agentNum = "1"
            mockNum = "2"
            done = "neutral"

            moveCount = 0
            while done != "win" and done != "tie":
                if playFirst:
                    if moveCount%2 == 0:
                        userUpdate = True
                    else:
                        userUpdate = False

                elif playSecond:
                    if moveCount%2 == 1:
                        userUpdate = True
                    else:
                        userUpdate = False

                
                newBoard, topMoves, done, enemyAgent, enemyMock, isCert = simRunner.run_norm(numAgents, simNum, gameRules, board, depth, agentNum, mockNum, userUpdate)

                if userUpdate == True:
                    board = newBoard
                    
                else:
                    #print(isCert)
                    topMove = topMoves[0][0]
                    board.fill(topMove, agentNum)
               
                #print(topMoves)
                print("Player: " + str(agentNum))
                print()
                #print(done)
                agentNum = enemyAgent
                mockNum = enemyMock
                board.printBoard()
                moveCount += 1
                
            board = copy.deepcopy(OGBoard)

if __name__ == "__main__":
    main()



