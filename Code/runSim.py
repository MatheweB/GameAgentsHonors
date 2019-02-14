import copy
import simulation as sim
import statistics as stat
import agent
import mockAgent as mock


class runSim:
    
    def initAgents(self, number, agentNum):
        agentList = []
        for x in range(0,number):
            agentList.append(agent.Agent())
            if agentNum != None:
                agentList[x].playerNumber = agentNum
        return agentList

    
    def updateBoard(self, board, highestStats, playerNum = None):
        move = highestStats[0][0]
        
        if playerNum != None:
            print("filling " + str(move) + " "+ playerNum)
            board.fill(move, playerNum)
            
            
        else:
            board.fill(move)
            
        return board


    def run_indiff(self, numAgents, simNum, gameRules, board, depth, userUpdate = False, printStuff = True):
        printStuff = False

        if userUpdate == True:
            newBoard = copy.deepcopy(board)
            newBoard.userUpdate()

            if gameRules.win(newBoard):
                win = True
            else:
                win = False
                
            return newBoard, None, win, "userUpdate"

        else:
        
            simulator = sim.Simulator()
            statMachine = stat.StatMachine()

            done = False

            agentsList = self.initAgents(numAgents, None)

            overallMoves = {} # move: number_total_plays
            overallMoveNums = {} # move: (won: 3turns: 3; 4turns: 6),(lost:2turns:1)
            bestMoveDict = {}
            
            mockAgent = mock.Mocker()
            
            topMoves = None

            for x in range (0,simNum):
                newAgents, completed = simulator.matchAgents(agentsList, mockAgent, copy.deepcopy(board), depth, gameRules)
                agentsList = completed + newAgents
                
                moveDict = statMachine.getStats(agentsList)
                # stats = won: [move:x], lost: [move:y], neutral [move:z]
                # moveDict = move: number_total_plays_this_run
                
                overallMoves = statMachine.sumStats(moveDict, overallMoves)
                
                overallMoveNums = simulator.getMoveList(agentsList, overallMoveNums)
                

                topMoves, isCert = statMachine.highestStats(overallMoves, overallMoveNums, bestMoveDict, "indiff", False)
                if (x < simNum//2): #Explore "Bad" moves
                    agents = simulator.changeAgents(agentsList, board, gameRules, topMoves[0][0], True) #true for searchingbadmoves
                
                else: #Trust the data and do good moves
                    agents = simulator.changeAgents(agentsList, board, gameRules, topMoves[0][0], False) #topMove endpoint in agent.py (or None)
                
            topMoves, isCert = statMachine.highestStats(overallMoves, overallMoveNums, bestMoveDict, "indiff", True)

            newBoard = copy.deepcopy(board)
            
            newBoard = self.updateBoard(newBoard, topMoves)
            
            if gameRules.win(newBoard):
                done = True
            else:
                done = False

            return newBoard, topMoves, done, isCert
        

    def run_norm(self, numAgents, simNum, gameRules, board, depth, playerNum, mockNum, userUpdate = False, printStuff = True):
        printStuff = False
        if userUpdate == True:
            newBoard = copy.deepcopy(board)
            newBoard.userUpdate(playerNum)
            
            if gameRules.win(newBoard, playerNum):
                done = "win"
                
            elif gameRules.tie(newBoard):
                done = "tie"
            else:
                done = "neutral"
                
            if playerNum == "2":
                playerNum = "1"
                mockNum = "2"
            
            else:
                playerNum = "2"
                mockNum = "1"
            
            return newBoard, None, done, playerNum, mockNum, "userUpdate"

        else:
        
            simulator = sim.Simulator()
            statMachine = stat.StatMachine()

            done = False

            agentsList = self.initAgents(numAgents, playerNum)

            overallMoves = {}
            overallMoveNums = {}
            bestMoveDict = {}
            
            mockAgent = mock.Mocker()
            
            topMoves = None

            
            for x in range (0,simNum):
                newAgents, completed = simulator.matchAgents(agentsList, mockAgent, copy.deepcopy(board), depth, gameRules, playerNum, mockNum)
                agentsList = completed + newAgents
                
                moveDict = statMachine.getStats(agentsList)
                overallMoves = statMachine.sumStats(moveDict, overallMoves)

                overallMoveNums = simulator.getMoveList(agentsList, overallMoveNums)
                
                topMoves, isCert = statMachine.highestStats(overallMoves, overallMoveNums, bestMoveDict, "norm", False)
                if (x < simNum//2): #Explore "Bad" moves
                    agents = simulator.changeAgents(agentsList, board, gameRules, topMoves[0][0], True) #true for searchingbadmoves
                
                else: #Trust the data and do good moves
                    agents = simulator.changeAgents(agentsList, board, gameRules, topMoves[0][0], False) #topMove endpoint in agent.py (or None)
                
                              
            topMoves, isCert = statMachine.highestStats(overallMoves, overallMoveNums, bestMoveDict, "norm", True)

            newBoard = copy.deepcopy(board)
            
            newBoard = self.updateBoard(newBoard, topMoves, playerNum)
            
            if gameRules.win(newBoard, playerNum):
                done = "win"
                
            elif gameRules.tie(newBoard):
                done = "tie"
                
            else:
                done = "neutral"
                
            if playerNum == "2":
                playerNum = "1"
                mockNum = "2"
            
            else:
                playerNum = "2"
                mockNum = "1"

            return newBoard, topMoves, done, playerNum, mockNum, isCert
