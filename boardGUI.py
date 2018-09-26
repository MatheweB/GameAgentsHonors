import random
import copy
import operator
import time

import boardClasses as Board
import agent
import statistics as stat
import boardRules as rules
import simulation as sim

depth = 15
goodCount = 0
agentNum = "O"
mockNum = "X"


def getAgentNum():
    return agentNum

def initAgents(number):
    agentList = []
    for x in range(0,number):
        agentList.append(agent.Agent())
    return(agentList)


def updateBoard(board, highestStats): #TODO IMPLEMENT RULES
    move = highestStats[0][1]
    board.fill(move, agentNum)
    return board

def updateBoardPlayer(board, x, y):

    if board.m == 1:
        move = []
        move.append(y)
        move.append(x)
        board.fill(move, agentNum)

    else:
        move = []
        move.append(y)
        move.append(x)
        board.fill(move, agentNum)
        
    return board


def main():
    global goodCount
    global agentNum
    global mockNum


    gameRules = rules.Nim()  #rules.TTT()
    boardType = Board.NimBoard() #Board.TTTBoard()

    
    simulator = sim.Simulator()
    statMachine = stat.StatMachine()
    
    numAgents = 1000
    simNum = 10
    gameNum = 20
    
    
    
    for x in range(0,gameNum):

        board = copy.deepcopy(boardType)

        done = False

        agents = initAgents(numAgents)

        while not done:

            turnNum = 1
            overallStats = {}
            topMoves = None

            if agentNum == "O": #or agentNum == "X":
            
                for x in range (0,simNum):
                    newAgents, completed = simulator.matchAgents(agents, copy.deepcopy(board), depth, agentNum, mockNum, gameRules)
                    agents = completed + newAgents
                    
                    stats = statMachine.getStats(agents)
                    overallStats = statMachine.sumStats(stats, overallStats)
                    
                    #topMoves = statMachine.highestStats(overallStats)

                    agents = simulator.changeAgents(agents, board, gameRules, None) #topMoves[0][1]) #topMove endpoint in agent.py
                    #board.printBoard()
                    
                topMoves = statMachine.highestStats(overallStats, True) #true = print certList
                

                print(topMoves)
                board = updateBoard(board, topMoves)
                agents = simulator.clearAgents(agents) #clears top moves
                board.printBoard()
                

            elif agentNum == "X":
                if board.m == 1: #TODO IMPLEMENT RULES
                    y = input("col: ")
                    value = input("number: ")
                    board = updateBoardPlayer(board, int(y), int(value))
                    

                else:
                    
                    y = input("row: ")
                    x = input("column: ")
                    board = updateBoardPlayer(board, int(x), int(y))
            

            if gameRules.win(board, agentNum):
                done = True
                agentNum = "X"
                
            elif gameRules.tie(board):
                goodCount += 1
                agentNum = "X"
                done = True

            if agentNum == "O":
                agentNum = "X"
                mockNum = "O"
                
            else:
                agentNum = "O"
                mockNum = "X"

            overallStats = {}
            turnNum += 1
        print(goodCount)
        print()
        print()
        print()

    print(goodCount)

if __name__ == "__main__":
    main()



