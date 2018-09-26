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

            if current.coreMove != None:
                current.move = current.coreMove
            else:
                current.coreMove = current.getMove(initBoard, rules)
                current.move = current.coreMove
            
            board = copy.deepcopy(initBoard)

            should_continue = self.interact(board, current, mockAgent, depth, agentNum, mockNum, rules)

            if should_continue:
                newAgents.append(current)
                
            else:
                completed.append(current)

        return newAgents, completed

    def interact(self, board, current, mock, depth, agentNum, mockNum, rules):
        #if something bad happens, return "change"
        #else return "okay"


        for x in range(0,depth):
            board.fill(current.move, agentNum)

            if rules.win(board, agentNum):
                current.didLose = False
                current.didWin = True
                current.change = True
                return False
            
            elif rules.tie(board):
                current.didLose = False
                current.didWin = False
                current.change = True
                return False
        

            mock.move = mock.getMove(board, mockNum, agentNum, rules)

            
            board.fill(mock.move, mockNum)


            if rules.win(board, mockNum):
                current.didLose = True
                current.didWin = False
                current.change = True
                return False
            
            elif rules.tie(board):
                current.didLose = False
                current.didWin = False
                current.change = True
                return False
            

            current.move = current.getMove(board, rules)

        current.neutral = True
        current.change = True
        return True
