import copy
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
            if agent.didWin == True:
                move = agent.getMoveItem() #0 = move, 1 = movenum
                if move[0] not in moveDict:
                    moveDict[move[0]] = {}
                    
                if "won" not in moveDict[move[0]]:
                    moveDict[move[0]]["won"] = {}

                if move[1] not in moveDict[move[0]]["won"]:
                    moveDict[move[0]]["won"][move[1]] = 1
                else:
                    moveDict[move[0]]["won"][move[1]] += 1
                    
            elif agent.didLose == True:
                move = agent.getMoveItem() #0 = move, 1 = movenum
                if move[0] not in moveDict:
                    moveDict[move[0]] = {}
                    
                if "lost" not in moveDict[move[0]]:
                    moveDict[move[0]]["lost"] = {}

                if move[1] not in moveDict[move[0]]["lost"]:
                    moveDict[move[0]]["lost"][move[1]] = 1
                else:
                    moveDict[move[0]]["lost"][move[1]] += 1

        return moveDict
    

    def changeAgents(self, agents, board, rules, topMove):
        for agent in agents:
            agent.makeChanges(board, rules, topMove)
        return agents

    def matchAgents(self, agents, mockAgent, initBoard, depth, rules, playerNum = None, mockNum = None, isRec = False): #divide list into those that go 1st and those that go 2nd

        newAgents = []
        completed = []

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
