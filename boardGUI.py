import random
import copy
import operator
import time

import boardClasses as Board
import boardRules as Rules
import runSim as Sim


def main():
    simRunner = Sim.runSim()
    
    gameRules = Rules.Nim()  #rules.TTT() #
    board =  Board.NimBoard([1,2,3,4,5]) #Board.TTTBoard() #

    playFirst = False
    playSecond = True
    userUpdate = False

    numAgents = 80
    simNum = 50
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
                       
                newBoard, topMoves, done = simRunner.run_indiff(numAgents, simNum, gameRules, board, depth, userUpdate)

                if topMoves != None:
                    print(topMoves)
                    
                newBoard.printBoard()
                board = newBoard
                moveCount += 1

        else: # A normal game
            
            agentNum = "1"
            mockNum = "2"
            done = "neutral"

            moveCount = 0
            while done not in ["win", "tie"]:
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
                    
                newBoard, topMoves, done, agentNum, mockNum = simRunner.run_norm(self, numAgents, simNum, gameRules, board, depth, agentNum, mockNum, userUpdate)
                print(topMoves)
                print(agentNum)
                newBoard.printBoard()
                board = newBoard
                moveCount += 1

if __name__ == "__main__":
    main()



