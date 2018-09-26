import operator
import ast

class StatMachine:
    def getStats(self, agentList):
        myDict = {}

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
                

        return myDict

    def sumStats(self, stats, overallStats):
        
        for key in stats.keys():
            
            if key not in overallStats:
                overallStats[key] = {}

            for move in stats[key]:
                if move not in overallStats[key]:
                    overallStats[key][move] = stats[key][move]
                else:
                    overallStats[key][move] += stats[key][move]

        return overallStats

    def arrayify(self, myString):
        return ast.literal_eval(myString)


    def normalize(self, wins, losses):
        pass


    def highestStats(self, overall, printStuff = False):
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

        for x in range(0,1): #LOSS CORRECTED 1st PASS - THEN CALCULATING WIN PERCENT VS TIE
            if x == 0:
                blackListed = "lost"
                myList = lostList
                
            for item in overall:
                if item != blackListed and item != "lost":
                    if blackListed == "lost":
                        foundItem = True
                    for move in myList: #Scale down scenarios to prevent losses
                        
                        moveString = str(move[1])
                        if moveString in overall[item].keys():
                            if int(overall[item][moveString]) > 0:
                                ratio = move[0]/overall[item][moveString]
                                if (ratio) > confidence:
                                    overall[item][moveString] = round(overall[item][moveString]/((move[0]/overall[item][moveString])),4)
                                
                                    
            
        
        for item in overall.items():
            status = item[0]
            moveList = item[1]
            for move in moveList:
                if len(certainList) > 0:
                    if status != "lost" or foundItem == False:
                        if self.arrayify(move) in certainList:
                            #print("OH BOY IM CERTAIN")
                            #print(move)
                            unsortedList.append([moveList[move], self.arrayify(move), status])

                else:
                    if status != "lost" or foundItem == False:
                        unsortedList.append([moveList[move], self.arrayify(move), status])


        
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
            for item in sortedList:
                if item[2] == "won":
                    wList.append(item)
                elif item[2] == "tied":
                    tList.append(item)
                elif item[2] == "neutral":
                    nList.append(item)
                else:
                    lList.append(item)
            totalList = wList + tList + nList + lList
            return totalList
            
            
        return sortedList
