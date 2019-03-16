import operator
import ast

class StatMachine:
    
    def getStats(self, agentList):
        moveDict = {}

        for agent in agentList:
            agentMove = str(agent.coreMove)

            if agentMove not in moveDict:
                moveDict[agentMove] = 1
            else:
                moveDict[agentMove] += 1

        return moveDict
    

    def sumStats(self, moves, overallMoves):                   
        for key in moves.keys():
            if key not in overallMoves.keys():
                overallMoves[key] = moves[key]
            else:
                overallMoves[key] += moves[key]

        return overallMoves
    

    def arrayify(self, myString):
        return ast.literal_eval(myString)


    def normalize(self, wins, losses):
        pass

    def foundWin(self, moveNums):
        for move in moveNums.keys():
            try:
                success = moveNums[move]["won"]
                return True
            except:
                pass
            
        return False

    def createCertainList(self, overallMoveNums, foundItem):
        certainList = []
        foundWins, foundTies = False, False
        
        if foundItem == True:
            for move in overallMoveNums.keys():
                moveLiteral = self.arrayify(move)
                added = False
                try:
                    wins = overallMoveNums[move]["won"]
                    try:
                        loss = overallMoveNums[move]["lost"]
                        
                    except:
                        added = True
                        foundWins = True
                        certainList.append([moveLiteral, "won"])
                except:
                    pass
                
                if added == False:
                    try:
                        neutrals = overallMoveNums[move]["neutral"]
                        
                        try:
                            loss = overallMoveNums[move]["lost"]
                            
                        except:
                            certainList.append([moveLiteral, "neutral"])
                            foundTies = True
                    except:
                        certainList.append([moveLiteral, "lost"])
                        
                added = False
                
        if foundItem == False:
            onlyWins = False


        return certainList, foundWins, foundTies


    def createWLRatios(self, overallMoveNums, ratioDict):
        maxMoveNum = -1
        for move in overallMoveNums.keys():
            for status in overallMoveNums[move].keys():
                if status == "won":
                    for move_num in overallMoveNums[move][status].keys():

                        if move_num > maxMoveNum:
                            maxMoveNum = move_num

                        try:
                            lostNum = overallMoveNums[move]["lost"][move_num]
                            #do = True
                            
                        except:
                            lostNum = 0
                            #do = False

                        wonNum = overallMoveNums[move][status][move_num]
                        
                        percentage = (wonNum/(wonNum+lostNum))

                        scaledNum = wonNum/(wonNum+lostNum)
                        #scaledNum = wonNum*percentage

                        if move not in ratioDict:
                            ratioDict[move] = {}
                            ratioDict[move][move_num] = scaledNum #percentage
                            
                        else:
                            ratioDict[move][move_num] = scaledNum #percentage
        return maxMoveNum

    def createMoveNumList(self, listOfMoves, maxMoveNum, ratioDict):
        for move_num in range(1, maxMoveNum+1):
            index = move_num - 1
            listOfMoves.append([])
            for move_string in ratioDict.keys():
                try:
                    listOfMoves[index].append([ratioDict[move_string][move_num], move_string])
                except:
                    pass

        for x in range(0,len(listOfMoves)):
            listOfMoves[x] = sorted(listOfMoves[x], key=operator.itemgetter(0), reverse = True)
            

    def makeMoveRatioSums(self, itemRanks, listOfMoves, gameType):
        for x in range(0, len(listOfMoves)):
            if listOfMoves[x] != []:
                sortedMoveList = listOfMoves[x]

                for moveItem in sortedMoveList:
                    myMove = moveItem[1] # actual move (e.g. [2,0])
                    moveRatio = moveItem[0] # (wins * win_percentage) from self.createWLRatios

                    if myMove not in itemRanks:
                        if gameType == "norm":
                            itemRanks[myMove] = [moveRatio, 1]
                        else:
                            itemRanks[myMove] = [moveRatio, moveRatio]
                        
                    else:
                        if gameType == "norm":
                            itemRanks[myMove][1] += 1
                            itemRanks[myMove][0] += moveRatio

                        else:
                            if moveRatio > itemRanks[myMove][1]:
                                itemRanks[myMove][1] = moveRatio
        
    def pickBestMove(self, itemRanks, moveDict, gameType):
        bestMove = None
        considerOnes = False
        bestDictList = {}

        for item in itemRanks:                
            ratio1 = itemRanks[item][0]
            ratio2 = itemRanks[item][1]

            if ratio2 == 1:
                if considerOnes == False:
                    considerOnes = True
                    bestMove = None
                
            if considerOnes and ratio2 == 1:
                if item not in bestDictList:
                    if gameType == "indiff":
                        bestDictList[item] = ratio2/ratio1
                    else:
                        bestDictList[item] = ratio1/ratio2
                    
                if bestMove == None:
                    if gameType == "indiff":
                        bestMove = [item, (ratio2/ratio1)]
                    else:
                        bestMove = [item, ratio1/ratio2]
                        
                else:
                    if gameType == "indiff":
                        if (ratio2/ratio1) > bestMove[1]:
                            bestMove = [item, (ratio2/ratio1)]
                    else:
                        if ratio1/ratio2 > bestMove[1]:
                            bestMove = [item, ratio1/ratio2]
                            
            elif considerOnes == False:
                if item not in bestDictList:
                    if gameType == "indiff":
                        bestDictList[item] = ratio2/ratio1
                    else:
                        bestDictList[item] = ratio1/ratio2
                    
                if bestMove == None:
                    if gameType == "indiff":
                        bestMove = [item, (ratio2/ratio1)]
                    else:
                        bestMove = [item, ratio1/ratio2]
                        
                else:
                    if gameType == "indiff":
                        if (ratio2/ratio1) > bestMove[1]:
                            bestMove = [item, (ratio2/ratio1)]
                    else:
                        if ratio1/ratio2 > bestMove[1]:
                            bestMove = [item, ratio1/ratio2]
                
        
        if bestMove == None:
            for key in moveDict.keys():
                bestMove = str(key)
                break


        return str(bestMove[0])
    

    def highestStats(self, moveDict, overallMoveNums, bestMoveDict, gameType, printStuff = False):
        certainList = []
        
        unsortedList = []
        unsortedDict = {}

        finalList = []

        ## checks if we found a "win" scenario
        foundItem = self.foundWin(overallMoveNums)

        ## If we've found a definite win path, use certainList
        certainList, foundWins, foundTies = self.createCertainList(overallMoveNums, foundItem)

        ## Creates win/loss ratio overages for 4 moves, 3 moves, etc...
        ratioDict = {}
        maxMoveNum = self.createWLRatios(overallMoveNums, ratioDict)

        #Creates a list of move depth and wins in order ([[list of 1-move wins], [list of 2-move wins], etc..])
        listOfMoves = []
        self.createMoveNumList(listOfMoves, maxMoveNum, ratioDict)

        
        # Creates a list of the sum of moveRatios for a given move X, and either the highest moveRatio as
        # a complementary pair, or the number of moves.
        # Norm: [sum_of_moveRatios, num_of_moves]
        # Indiff: [sum_of_moveRatios, highest_move_ratio (usually the last move)]
        itemRanks = {}
        self.makeMoveRatioSums(itemRanks, listOfMoves, gameType)
        #print(listOfMoves)
        #print(itemRanks)
        #exit(5)

        # Get best move overall (see function for decision function)
        bestMoveString = self.pickBestMove(itemRanks, moveDict, gameType)
        

        if printStuff:
            print('-------------------')
            print("BEST MOVE DICT IS:", bestMoveDict)
            print()
            print("BEST MOVE IS:", bestMoveString)
            print()
            print("Item Ranks are: ", itemRanks)
            print()
            

        unsortedList = []
        for move in moveDict.keys():
            if str(move) == bestMoveString:
                unsortedList.append([self.arrayify(move),1])
            else:
                unsortedList.append([self.arrayify(move),0])

            
        if foundItem == True:
            sortedList = sorted(unsortedList, key=operator.itemgetter(1), reverse = True)
        else:
            sortedList = sorted(unsortedList, key=operator.itemgetter(1), reverse = False)



        if len(certainList) > 0 and (foundWins or foundTies):
            wList = []
            nList = []
            lList = []
            
            for item in certainList:
                if item[1] == "won":
                    wList.append(item)
                elif item[1] == "neutral":
                    nList.append(item)
                else:
                    lList.append(item)
                    
            totalList = wList + nList + lList
            isCert = totalList[0][1]
            return totalList, isCert
        
        if printStuff:
            print(overallMoveNums)
            print('-----')

        return sortedList, False #not certain that I won
