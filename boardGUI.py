import random
import copy
import operator
import time

import boardClasses as Board
import agent
import statistics as stat
import boardRules as rules
import simulation as sim

depth = 200
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

def updateBoardPlayer(board, x, y): #TODO IMPLEMENT RULES

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
    global agentNum
    global mockNum

    gameRules = rules.Nim()  #rules.TTT()
    boardType = Board.NimBoard([1,2,3,4,5]) #Board.TTTBoard()

    
    simulator = sim.Simulator()
    statMachine = stat.StatMachine()
    
    numAgents = 500
    simNum = 100
    gameNum = 20
    
    
    
    for x in range(0,gameNum):

        board = copy.deepcopy(boardType)

        done = False

        agents = initAgents(numAgents)

        agentNum = "1"
        
        mockNum = "2"

        while not done:

            overallStats = {}
            topMoves = None

            if agentNum == "1":# or agentNum == "X":
            
                for x in range (0,simNum):
                    newAgents, completed = simulator.matchAgents(agents, copy.deepcopy(board), depth, agentNum, mockNum, gameRules)
                    agents = completed + newAgents
                    
                    stats = statMachine.getStats(agents)
                    overallStats = statMachine.sumStats(stats, overallStats)
                    
                    #topMoves = statMachine.highestStats(overallStats, False)

                    agents = simulator.changeAgents(agents, board, gameRules, None) #topMoves[0][1]) #topMove endpoint in agent.py
                    #board.printBoard()
                    
                topMoves = statMachine.highestStats(overallStats, printStuff = True)
                

                print(topMoves)
                print(agentNum)
                
                board = updateBoard(board, topMoves)
                agents = simulator.clearAgents(agents) #clears top moves
                board.printBoard()
                

            elif agentNum == "2":
                if board.m == 1: #TODO IMPLEMENT RULES
                    y = input("col: ")
                    value = input("number: ")
                    board = updateBoardPlayer(board, int(y), int(value))
                

                else:
                    y = input("row: ")
                    x = input("column: ")
                    board = updateBoardPlayer(board, int(x), int(y))

                
            if agentNum == "2":
                agentNum = "1"
                mockNum = "2"
                
            else:
                agentNum = "2"
                mockNum = "1"

            overallStats = {}


if __name__ == "__main__":
    main()



