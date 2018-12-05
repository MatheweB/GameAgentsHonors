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


    def highestStats(self, overall, moveDict, overallMoveNums, bestMoveDict, gameType, printStuff = False):

        #print(moveDict)
        
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

        confidence = 1

        for item in overall.items():
            status = item[0]
            moveList = item[1]
            for move in moveList:
                listApp = [moveList[move], self.arrayify(move), status]
                moveArray = self.arrayify(move)
                if status == "lost":
                    lostList.append(listApp)
                    lostAltered.append(moveArray)
                if status == "won":
                    wonList.append(listApp)
                    otherList.append(moveArray)
                if status == "tied":
                    tiedList.append(listApp)
                    otherList.append(moveArray)
                if status == "neutral":
                    neutralList.append(listApp)
                    otherList.append(moveArray)

        for item in otherList:
            if item not in lostAltered:
                if item not in certainList:
                    certainList.append(item)

        foundItem = False #If all "lost"

        newOverall = copy.deepcopy(overall)               
        for item in newOverall:
            if item != "lost":
                foundItem = True
                break
##                for move in lostList: #Scale down scenarios to prevent losses
##                    moveString = str(move[1])
##                    if moveString in newOverall[item].keys():
##                        if int(newOverall[item][moveString]) > 0:
##                            ratio = move[0]/newOverall[item][moveString]
##                            if doTheRatio == True:
##                                if (ratio) > confidence:
##                                    newOverall[item][moveString] = round(newOverall[item][moveString]/ratio,4)
       
        for item in newOverall.items():
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

        highList = {}
        highMoveNum = -1
        for move in overallMoveNums.keys():
            for status in overallMoveNums[move].keys():
                if status == "won":
                    for move_num in overallMoveNums[move][status].keys():

                        if move_num > highMoveNum:
                            highMoveNum = move_num

                        try:
                            lostNum = overallMoveNums[move]["lost"][move_num]
                            #do = True
                            
                        except:
                            lostNum = 0
                            #do = False

                        wonNum = overallMoveNums[move][status][move_num]

                        percentage = (wonNum/(wonNum+lostNum))

                        if move not in highList:
                            highList[move] = {}
                            highList[move][move_num] = percentage
                            
                        else:
                            highList[move][move_num] = percentage #FIXIXIXIXIXIXIXIXIXIXIXIXIX
        
        listOfMoves = []
        for move_num in range(1, highMoveNum+1):
            index = move_num - 1
            listOfMoves.append([])
            for move_string in highList.keys():
                try:
                    listOfMoves[index].append([highList[move_string][move_num], move_string])
                except:
                    pass

        for x in range(0,len(listOfMoves)):
            listOfMoves[x] = sorted(listOfMoves[x], key=operator.itemgetter(0), reverse = True)


        bestMoves = []
        overallRank = {}


        itemRanks = {}
        for x in range(0, len(listOfMoves)):
            if listOfMoves[x] != []:
                sortedMoveList = listOfMoves[x]

                for moveItem in sortedMoveList:
                    myMove = moveItem[1]
                    moveRatio = moveItem[0]

                    if myMove not in itemRanks:
                        itemRanks[myMove] = [moveRatio, moveRatio]
                        
                    else:
                        if moveRatio > itemRanks[myMove][1]:
                            itemRanks[myMove][1] = moveRatio

        bestMove = None
        bestDictList = {}
        for item in itemRanks:

            if itemRanks[item][0] == 1 and gameType == "norm":
                ratio1 = 1
                ratio2 = 0
            else:
                ratio1 = itemRanks[item][0]
                ratio2 = itemRanks[item][1]
            
            if item not in bestDictList:
                if gameType == "indiff":
                    bestDictList[item] = (ratio2 - ratio1)
                else:
                    bestDictList[item] = (ratio2 + ratio1)
                
            if bestMove == None:
                if gameType == "indiff":
                    bestMove = [item, (ratio2 - ratio1)]
                else:
                    bestMove = [item, (ratio2 + ratio1)]
                    
            else:
                if gameType == "indiff":
                    if (ratio2 - ratio1) > bestMove[1]:
                        bestMove = [item, (ratio2 - ratio1)]
                else:
                    if (ratio2 + ratio1) > bestMove[1]:
                        bestMove = [item, (ratio2 + ratio1)]
        
        if bestMove == None:
            for key in moveDict.keys():
                bestMove = str(key)
                break
            
        bestMoveString = str(bestMove[0])

        
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
