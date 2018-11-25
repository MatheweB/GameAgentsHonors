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
    OGBoard = Board.NimBoard([1,5,5]) #Board.TTTBoard() #
    board = copy.deepcopy(OGBoard)

    playFirst = False
    playSecond = True
    userUpdate = False

    numAgents = 250
    simNum = 150
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
                    board.fill(topMoves[0][1])

##                elif isCert == "won":
##                    board = newBoard

##                else:
##                    topBoi = []
##                    cert = []
##                    for x in range(0,len(topMoves)):
##                        newBoard = copy.deepcopy(board)
##                        newBoard.fill(topMoves[x][1])
##                        predBoard, nextTop, nextDone, isCert = simRunner.run_indiff(numAgents, simNum, gameRules, copy.deepcopy(newBoard), depth, userUpdate)
##                        if isCert == "lost":
##                            cert.append(topMoves[x][1])
##                        else:
##                            topBoi.append([nextTop[0][0], topMoves[x][1]])
##
##                    if len(cert) > 0:
##                        board.fill(cert[0])
##                    else:
##                        maxVal = topBoi[0][0]
##                        maxMove = topBoi[0][1]
##                        for move in topBoi:
##                            if move[0] < maxVal:
##                                maxVal = move[0]
##                                maxMove = move[1]
##                            
##                        board.fill(maxMove) #THIS MIGHT NOT WORK BECAUSE IT MAKES DUMB MOVES WITH 0% WIN RATE TO SOME HIGH(ER) WINRATE. TRY TOTAL POSI CHANGE

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
                    
                elif isCert == "won":
                    board = newBoard

                else:
                    topBoi = []
                    cert = []

                    
                    for x in range(0,len(topMoves)):
                        newBoard = copy.deepcopy(board)
                        newBoard.fill(topMoves[x][1], mockNum)
                        predBoard, nextTop, nextDone, _, _, isCert = simRunner.run_norm(numAgents, simNum, gameRules, copy.deepcopy(newBoard), depth, enemyAgent, enemyMock, userUpdate)
                        if isCert == "lost":
                            cert.append(topMoves[x][1])
                        else:
                            topBoi.append([nextTop[0][0], topMoves[x][1]])

                    if len(cert) > 0:
                        board.fill(cert[0], agentNum)
                        
                    else:
                        maxVal = topBoi[0][0]
                        maxMove = topBoi[0][1]
                        for move in topBoi:
                            if move[0] < maxVal:
                                maxVal = move[0]
                                maxMove = move[1]
                        print(topBoi)
                            
                        board.fill(maxMove, agentNum) #THIS MIGHT NOT WORK BECAUSE IT MAKES DUMB MOVES WITH 0% WIN RATE TO SOME HIGH(ER) WINRATE. TRY TOTAL POSI CHANGE

                
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



