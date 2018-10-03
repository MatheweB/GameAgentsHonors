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

    def changeAgents(self, agents, board, rules, topMove):
        for agent in agents:
            agent.makeChanges(board, rules, topMove)
        return agents


    def matchAgents(self, agents, initBoard, depth, agentNum, mockNum, rules): #divide list into those that go 1st and those that go 2nd

        newAgents = []
        completed = []
        mockAgent = MA.Mocker()
        #agents = self.clearAgents(agents)

        while len(agents) != 0:
            current = agents.pop()
            
            board = copy.deepcopy(initBoard)

            simMachine = rules.simMachine()
            
            should_continue = simMachine.interact(board, current, mockAgent, depth, agentNum, mockNum, rules)

            if should_continue:
                newAgents.append(current)
                
            else:
                completed.append(current)

        return newAgents, completed
