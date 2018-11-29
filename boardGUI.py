import random
import copy
import operator
import time


import boardClasses as Board
import boardRules as Rules
import runSim as Sim

def main():
    simRunner = Sim.runSim()
    
    gameRules = Rules.Nim()  # Rules.TTT() #
    OGBoard = Board.NimBoard([5,3]) #Board.TTTBoard() #
    board = copy.deepcopy(OGBoard)

    playFirst = False
    playSecond = True
    userUpdate = False

    numAgents = 200
    simNum = 100
    depth = 200
    
    gameNum = 20

    for game in range(0,gameNum):

        if gameRules.is_indiff(): # An indifferent game

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
                    print(isCert)
                    board.fill(topMoves[0][1])
                    
                if topMoves != None:
                    print(topMoves)

                board.printBoard()
                
                moveCount += 1
                
            board = copy.deepcopy(OGBoard)
            

        else: # A normal game
            
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
                    print(isCert)
                    board.fill(topMoves[0][1], agentNum)
               
                print(topMoves)
                print(agentNum)
                print(done)
                agentNum = enemyAgent
                mockNum = enemyMock
                board.printBoard()
                moveCount += 1
                
            board = copy.deepcopy(OGBoard)

if __name__ == "__main__":
    main()



