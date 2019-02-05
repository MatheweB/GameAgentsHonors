import operator
import ast
import copy
import random

doTheRatio = True

class StatMachine:
    
    def getStats(self, agentList):
        myDict = {}
        moveDict = {}

        for agent in agentList:
            agentMove = str(agent.coreMove)
            
            if agent.didLose:
                addWord = "lost"
                addNum = 1
            elif agent.didWin:
                addWord = "won"
                addNum = 1
            elif agent.neutral:
                addNum = 1
                addWord = "neutral"
            elif not agent.didWin and not agent.didLose and not agent.neutral:
                addNum = 1
                addWord = "tied"
                
            if addWord not in myDict.keys():
                myDict[addWord] = {}
                
            if agentMove not in myDict[addWord]:
                myDict[addWord][agentMove] = addNum
            else:
                myDict[addWord][agentMove] += addNum
                

            #if agent.didWin:
            if agentMove not in moveDict:
                moveDict[agentMove] = 1
            else:
                moveDict[agentMove] += 1


        return myDict, moveDict
    

    def sumStats(self, stats, moves, overallStats, overallMoves):

        for key in stats.keys():
            
            if key not in overallStats:
                overallStats[key] = {}

            for move in stats[key]:
                if move not in overallStats[key]:
                    overallStats[key][move] = stats[key][move]
                    
                else:
                    overallStats[key][move] += stats[key][move]

                    
        for key in moves.keys():
            if key not in overallMoves.keys():
                overallMoves[key] = moves[key]
            else:
                overallMoves[key] += moves[key]

        return overallStats, overallMoves

    def arrayify(self, myString):
        return ast.literal_eval(myString)


    def normalize(self, wins, losses):
        pass

    def makeLists(self, overall, won, lost, lostAltered, tied, neutral, other, certain):
        for item in overall.items():
            status = item[0]
            moveList = item[1]
            for move in moveList:
                listApp = [moveList[move], self.arrayify(move), status]
                moveArray = self.arrayify(move)
                if status == "lost":
                    lost.append(listApp)
                    lostAltered.append(moveArray)
                if status == "won":
                    won.append(listApp)
                    other.append(moveArray)
                if status == "tied":
                    tied.append(listApp)
                    other.append(moveArray)
                if status == "neutral":
                    neutral.append(listApp)
                    other.append(moveArray)

        for item in other:
            if item not in lostAltered:
                if item not in certain:
                    certain.append(item)

    def scaleWins(self, overall, lostList, confidence, gameType):
##        foundItem = False
        for item in overall:
            if item != "lost":
                return True
##                foundItem = True

                
##                if gameType == "indiff":
##                    return foundItem
##                else:
##                    for move in lostList: #Scale down scenarios to prevent losses
##                        moveString = str(move[1])
##                        if moveString in overall[item].keys():
##                            if int(overall[item][moveString]) > 0:
##                                ratio = move[0]/overall[item][moveString]
##                                if gameType == "norm":
##                                    if (ratio) > confidence:
##                                        overall[item][moveString] = round(overall[item][moveString]/ratio,4)
##        return foundItem
        return False

    def createCertainList(self, overall, certainList, unsortedList, foundItem, printStuff):
        for item in overall.items():
            status = item[0]
            moveList = item[1]
            for move in moveList:
                if len(certainList) > 0:
                    if status != "lost" or foundItem == False:
                        if self.arrayify(move) in certainList:
                            unsortedList.append([moveList[move], self.arrayify(move), status])
                            if printStuff:
                                print("OH BOY IM CERTAIN")

                else:
                    if status != "lost" or foundItem == False:
                        unsortedList.append([moveList[move], self.arrayify(move), status])

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
                        
                        scaledNum = wonNum*percentage

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
        bestDictList = {}

        for item in itemRanks:                
            ratio1 = itemRanks[item][0]
            ratio2 = itemRanks[item][1]
        
            if item not in bestDictList:
                if gameType == "indiff":
                    bestDictList[item] = (ratio2 - ratio1)
                else:
                    bestDictList[item] = ratio1/ratio2
                
            if bestMove == None:
                if gameType == "indiff":
                    bestMove = [item, (ratio2 - ratio1)]
                else:
                    bestMove = [item, ratio1/ratio2]
                    
            else:
                if gameType == "indiff":
                    if (ratio2 - ratio1) > bestMove[1]:
                        bestMove = [item, (ratio2 - ratio1)]
                else:
                    if ratio1/ratio2 > bestMove[1]:
                        bestMove = [item, ratio1/ratio2]
        
        if bestMove == None:
            for key in moveDict.keys():
                bestMove = str(key)
                break

        print(bestDictList)

        return str(bestMove[0])
    

    def highestStats(self, overall, moveDict, overallMoveNums, bestMoveDict, gameType, printStuff = False):
        
        high = []
        
        lostList = []
        lostAltered = []
        
        otherList = []
        wonList = []
        tiedList = []
        neutralList = []
        
        certainList = []
        
        unsortedList = []
        unsortedDict = {}

        finalList = []


        ## Creates Sanitized Lists
        self.makeLists(overall, wonList, lostList, lostAltered, tiedList, neutralList, otherList, certainList)


        ## Scales wins/losses and lets us know if we lose every scenario
        foundItem = False
        confidence = 1
        newOverall = copy.deepcopy(overall)
        if self.scaleWins(newOverall, lostList, confidence, gameType) == True:
            foundItem = True


        ## If we've found a definite win path, or an invevitable "lose" path, use certainList
        self.createCertainList(newOverall, certainList, unsortedList, foundItem, printStuff)


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


        # Get best move overall (see function for decision function)
        bestMoveString = self.pickBestMove(itemRanks, moveDict, gameType)
        

        if printStuff:
            print('-------------------')
            print('MOVEPERCDIF:', bestDictList)
            print()
            print(highList)
            print()
            print("BEST MOVES ARE:", bestMoves)
            print("BEST MOVE DICT IS:", bestMoveDict)
            print()
            print("BEST MOVE IS:", bestMoveString)
            print()
            print("OVERALL RANK:", overallRank)
            print()

            
        for item in unsortedList:
            if str(item[1]) == bestMoveString:
                item[0] = 1
            else:
                item[0] = 0
            
        for item in unsortedList: #Get the most numerous tie/win scenarios
            if str(item[1]) not in unsortedDict:
                unsortedDict[str(item[1])] = item
            else:
                if item[0] > unsortedDict[str(item[1])][0]:
                    unsortedDict[str(item[1])] = item


        for item in unsortedDict.items():
            finalList.append(item[1])

            
        if foundItem == False:
            sortedList = sorted(finalList, key=operator.itemgetter(0), reverse = False)
        else:
            sortedList = sorted(finalList, key=operator.itemgetter(0), reverse = True)

        wList = []
        tList = []
        nList = []
        lList = []

        
        if len(certainList) > 0:
            isCert = None
            
            for item in sortedList:
                if item[2] == "won":
                    isCert = "won"
                    wList.append(item)
                elif item[2] == "tied":
                    isCert = "tied"
                    tList.append(item)
                elif item[2] == "neutral":
                    isCert = "neutral"
                    nList.append(item)
                else:
                    isCert = "lost"
                    lList.append(item)
            totalList = wList + tList + nList + lList
            return totalList, isCert
        
        if printStuff:
            print(overallMoveNums)
            print('-----')
            
        return sortedList, False #not certain that I won
