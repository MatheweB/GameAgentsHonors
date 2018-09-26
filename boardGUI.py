import random
import copy
import operator
import time

import boardClasses as Board
import agent
import statistics as stat
import boardRules as rules
import simulation as sim

depth = 5
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


def updateBoard(board, highestStats):
    move = highestStats[0][1]
    board.fill(move, agentNum)
    return board

def updateBoardPlayer(board, x, y):
    move = []
    move.append(y)
    move.append(x)
    board.fill(move, agentNum)
    return board


def main():
    global goodCount
    global agentNum
    global mockNum
    
    simulator = sim.Simulator()
    statMachine = stat.StatMachine()
    TTTRules = rules.TTT()
    numAgents = 1000
    simNum = 1

    gameNum = 20
    
    
    
    for x in range(0,gameNum):

        board = Board.TTTBoard()

        done = False

        agents = initAgents(numAgents)

        while not done:

            turnNum = 1
            overallStats = {}
            topMoves = None

            if agentNum == "O": #or agentNum == "X":
            
                for x in range (0,simNum):
                    newAgents, completed = simulator.matchAgents(agents, copy.deepcopy(board), depth, agentNum, mockNum)
                    agents = completed + newAgents
                    
                    stats = statMachine.getStats(agents)
                    overallStats = statMachine.sumStats(stats, overallStats)
                    
                    #topMoves = statMachine.highestStats(overallStats)

                    agents = simulator.changeAgents(agents, board, None) #topMoves[0][1]) #topMove endpoint in agent.py
                    
                topMoves = statMachine.highestStats(overallStats, True) #true = print certList
                

                print(topMoves)
                board = updateBoard(board, topMoves)
                agents = simulator.clearAgents(agents) #clears top moves
                board.printBoard()
                

            elif agentNum == "X":
                y = input("row: ")
                x = input("column: ")
                board = updateBoardPlayer(board, int(x), int(y))
            

            if TTTRules.win(board, agentNum):
                done = True
                agentNum = "X"
                
            elif TTTRules.tie(board):
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



