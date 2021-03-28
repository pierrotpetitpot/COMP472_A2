from node import *
import csv
import copy
from datetime import datetime
import random
import multiprocessing
import time
from aStar import getCost
from aStar import getCost2
from aStar import getBestChild
from datetime import datetime







def randomGen():
    f = open("20.txt", "w")
    for x in range(5):
        list = random.sample(range(1, 10), 9)
        f.write(str(list))
        f.write("\n")
    f.close


# outputs average and total
def aStarPrime(root, goal):

    listOfOutput = []
    listOfCosts = []
    targetNode = copy.deepcopy(root)
    visitedChildrenState = []
    startTime = datetime.now()
    currentTime = datetime.now()
    totalLength = 0

    while goal != targetNode.state:
        currentTime = datetime.now()
        delta = currentTime - startTime

        if delta.total_seconds() >= 2:
            # change the name of the file
            f = open("analysisAStar(1).txt", "a")
            f.write("Time of execution greater than 60 seconds" "\n")
            f.close
            break
        listOfChildren = getAllChildren(targetNode)

        for child in listOfChildren:
            listOfCosts.append(getCost(child, goal))
        bestChild = getBestChild(listOfChildren, listOfCosts)
        if bestChild is None:
            return
        visitedChildrenState.append(bestChild.state)
        listOfOutput.append(bestChild.state)
        targetNode = copy.deepcopy(bestChild)



        outputToFile(listOfOutput, "analysisAStar(1).txt")


        listOfCosts = []
        totalLength = totalLength + 1

        # outputToFileLength("analysisAStar(2).txt", totalLength)


def outputToFileLength(filename, totalLength):
    f = open(filename, "a")
    f.write(totalLength)
    f.close

def outputToFile(path, fileName):
    file = open(fileName, "a")

    for state in path:
        currentState = state
        file.write("\n\nState: ")
        scounter = 0
        for s in currentState:
            if scounter % 3 == 0:
                file.write("\n")
            file.write(str(s) + " ")
            scounter += 1
    file.close()


# returns a list of nodes where each node is a puzzle from 20.txt
def getInput(filename):
    inputs = []
    with open(filename, 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            row = str(row)
            formattedRow = row.replace("[", "").replace("]", "").replace("'", "")
            mylist = [int(x) for x in formattedRow.split(',')]
            aNode = Node(None, mylist)
            inputs.append(aNode)

    return inputs




def aStarAnalysis1(inputs, goalState):
    for input in inputs:
        f = open("analysisAStar(1).txt", "a")
        f.write("\n===========NEW PUZZLE===========\n")
        f.close
        aStarPrime(input, goalState)


# def aStarAnalysis2(inputs, goalState):
#     for input in inputs:
#         f = open("analysisAStar(2).txt", "a")
#         f.write("\n===========NEW PUZZLE===========\n")
#         f.close
#         aStarPrime(input, goalState)
# def aStarAnalysis3(inputs, goalState):
#     for input in inputs:
#         f = open("analysisAStar(3).txt", "a")
#         f.write("\n===========NEW PUZZLE===========\n")
#         f.close
#         aStarPrime(input, goalState)
#




def getAllChildren(node: Node):
    currentNodeState = node.state
    tempChildState = copy.deepcopy(currentNodeState)
    allChildren = []
    # child 0-1
    tempChildState[0], tempChildState[1] = tempChildState[1], tempChildState[0]
    newChild = Node(currentNodeState, tempChildState)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 1-2
    tempChildState[1], tempChildState[2] = tempChildState[2], tempChildState[1]
    newChild = Node(currentNodeState, tempChildState)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 0-3
    tempChildState[0], tempChildState[3] = tempChildState[3], tempChildState[0]
    newChild = Node(currentNodeState, tempChildState)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 1-4
    tempChildState[1], tempChildState[4] = tempChildState[4], tempChildState[1]
    newChild = Node(currentNodeState, tempChildState)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 2-5
    tempChildState[2], tempChildState[5] = tempChildState[5], tempChildState[2]
    newChild = Node(currentNodeState, tempChildState)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 3-4
    tempChildState[3], tempChildState[4] = tempChildState[4], tempChildState[3]
    newChild = Node(currentNodeState, tempChildState)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 4-5
    tempChildState[4], tempChildState[5] = tempChildState[5], tempChildState[4]
    newChild = Node(currentNodeState, tempChildState)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 3-6
    tempChildState[3], tempChildState[6] = tempChildState[6], tempChildState[3]
    newChild = Node(currentNodeState, tempChildState)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 4-7
    tempChildState[4], tempChildState[7] = tempChildState[7], tempChildState[4]
    newChild = Node(currentNodeState, tempChildState)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 5-8
    tempChildState[5], tempChildState[8] = tempChildState[8], tempChildState[5]
    newChild = Node(currentNodeState, tempChildState)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 6-7
    tempChildState[6], tempChildState[7] = tempChildState[7], tempChildState[6]
    newChild = Node(currentNodeState, tempChildState)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 7-8
    tempChildState[7], tempChildState[8] = tempChildState[8], tempChildState[7]
    newChild = Node(currentNodeState, tempChildState)
    allChildren.append(newChild)

    return allChildren


randomGen()

# test = [8, 4, 7, 1, 5, 6, 9, 3, 2]


goal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listOfInputs = getInput("20.txt")
aStarAnalysis1(listOfInputs, goal)
