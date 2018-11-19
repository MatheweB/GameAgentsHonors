import copy
import simulation as sim
import statistics as stat
import agent

class runSim:
    
    def initAgents(self, number):
        agentList = []
        for x in range(0,number):
            agentList.append(agent.Agent())
        return agentList

    
    def updateBoard(self, board, highestStats, playerNum = None): 
        move = highestStats[0][1]
        
        if playerNum != None:
            board.fill(move, playerNum)
            
        else:
            board.fill(move)
            
        return board


    def run_indiff(self, numAgents, simNum, gameRules, board, depth, userUpdate = False, isRec = False, printStuff = True):

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

            agentsList = self.initAgents(numAgents)

            overallStats = {}
            topMoves = None

            for x in range (0,simNum):
                newAgents, completed = simulator.matchAgents(agentsList, copy.deepcopy(board), depth, gameRules, isRec = isRec)
                agentsList = completed + newAgents
                
                stats = statMachine.getStats(agentsList)
                overallStats = statMachine.sumStats(stats, overallStats)
                
                #topMoves = statMachine.highestStats(overallStats, False)

                agents = simulator.changeAgents(agentsList, board, gameRules, None) #topMoves[0][1]) #topMove endpoint in agent.py
                
            topMoves, isCert = statMachine.highestStats(overallStats, printStuff)

            newBoard = copy.deepcopy(board)
            
            newBoard = self.updateBoard(newBoard, topMoves)
            
            if gameRules.win(newBoard):
                done = True
            else:
                done = False

            return newBoard, topMoves, done, isCert
        

    def run_norm(self, numAgents, simNum, gameRules, board, depth, playerNum, mockNum, userUpdate = False, isRec = False, printStuff = True):

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

            agentsList = self.initAgents(numAgents)

            overallStats = {}
            topMoves = None

            
            for x in range (0,simNum):
                newAgents, completed = simulator.matchAgents(agentsList, copy.deepcopy(board), depth, gameRules, playerNum, mockNum, isRec = isRec)
                agentsList = completed + newAgents
                
                stats = statMachine.getStats(agentsList)
                overallStats = statMachine.sumStats(stats, overallStats)
                
                #topMoves = statMachine.highestStats(overallStats, False)

                agentsList = simulator.changeAgents(agentsList, board, gameRules, None) #topMoves[0][1]) #topMove endpoint in agent.py
                
            topMoves, isCert = statMachine.highestStats(overallStats, printStuff)

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
