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

    def changeAgents(self, agents, board):
        for agent in agents:
            agent.makeChanges(board)
        return agents


    def matchAgents(self, agents, initBoard, depth, agentNum, mockNum): #divide list into those that go 1st and those that go 2nd

        newAgents = []
        completed = []
        mockAgent = MA.Mocker()
        #agents = self.clearAgents(agents)

        while len(agents) != 0:
            current = agents.pop()

            if current.coreMove != None:
                current.move = current.coreMove
            else:
                current.coreMove = current.getMove(initBoard)
                current.move = current.coreMove
            
            board = copy.deepcopy(initBoard)

            should_continue = self.interact(board, current, mockAgent, depth, agentNum, mockNum)

            if should_continue:
                newAgents.append(current)
                
            else:
                completed.append(current)

        return newAgents, completed

    def interact(self, board, current, mock, depth, agentNum, mockNum):
        #if something bad happens, return "change"
        #else return "okay"

        TTTRules = boardRules.TTT()


        for x in range(0,depth):
            board.fill(current.move, agentNum)

            if TTTRules.win(board, agentNum):
                current.didLose = False
                current.didWin = True
                return False
            
            elif board.isFull():
                current.didLose = False
                current.didWin = False
                current.change = True
                return False
        

            mock.move = mock.getMove(board, mockNum, agentNum, "DUMMY RULES")

            
            board.fill(mock.move, mockNum)


            if TTTRules.win(board, mockNum):
                current.didLose = True
                current.didWin = False
                current.change = True
                return False
            
            elif board.isFull():
                current.didLose = False
                current.didWin = False
                current.change = True
                return False
            

            current.move = current.getMove(board)

        current.neutral = True
        current.change = True
        return True
