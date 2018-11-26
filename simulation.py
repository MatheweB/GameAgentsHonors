import copy
import mockAgent as MA
import boardRules

class Simulator:
    
    def clearAgents(self, agents):
        for agent in agents:
            agent.coreMove = None
            agent.didWin = False
            agent.didLose = False
            agent.neutral = False
        return agents

    def getMoveList(self, agents, moveDict):
        for agent in agents:
            if agent.moveNum != False:
                
                move = agent.getMoveItem() #0 = move, 1 = movenum
                if move[0] not in moveDict:
                    moveDict[move[0]] = [move[1], 1]
                else:
                    moveDict[move[0]][0] += move[1]
                    moveDict[move[0]][1] += 1
        return moveDict
    

    def changeAgents(self, agents, board, rules, topMove):
        for agent in agents:
            agent.makeChanges(board, rules, topMove)
        return agents

    def matchAgents(self, agents, initBoard, depth, rules, playerNum = None, mockNum = None, isRec = False): #divide list into those that go 1st and those that go 2nd

        newAgents = []
        completed = []
        
        mockAgent = MA.Mocker()
        #agents = self.clearAgents(agents)

        while len(agents) != 0:
            current = agents.pop()
            
            board = copy.deepcopy(initBoard)

            simMachine = rules.simMachine()

            if rules.is_indiff():
                should_continue = simMachine.interact(board, current, mockAgent, depth, rules, isRec = isRec)
            else:
                should_continue = simMachine.interact(board, current, mockAgent, depth, rules, playerNum, mockNum, isRec = isRec)               

            if should_continue:
                newAgents.append(current)
                
            else:
                completed.append(current)

        return newAgents, completed
