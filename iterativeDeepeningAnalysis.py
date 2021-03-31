from nodeDepth import NodeDepth
import copy
from datetime import datetime

import os
import time
import random
import csv

# calls the depth first algorithm with the 20 random puzzles
def iterativeDeepAnalysis1(inputs):
    for input in inputs:
        iterativeDeepeningAlgorithm(input)

# creates 20 random puzzles
def randomGen():
    f = open("20.txt", "w")
    for x in range(20):
        list = random.sample(range(1, 10), 9)
        f.write(str(list))
        f.write("\n")
    f.close

# writes the length of the path to a file
def outputToFileLength(path, filename):
    f = open(filename, "a")
    f.write(str(path))
    f.write(str("\n"))
    f.close

# get the randomized input to create a puzzle
def getInput(filename):
    inputs = []
    with open(filename, 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            row = str(row)
            formattedRow = row.replace("[", "").replace("]", "").replace("'", "")
            mylist = [int(x) for x in formattedRow.split(',')]
            inputs.append(mylist)

    return inputs

#method to get all the 12 possible children of a node
def getAllChildren(node: NodeDepth):
    currentNodeState = node.state
    tempChildState = copy.deepcopy(currentNodeState)
    depthCounter = node.depth
    allChildren = []
    # child 0-1
    tempChildState[0], tempChildState[1] = tempChildState[1], tempChildState[0]
    newChild = NodeDepth(currentNodeState, tempChildState, depthCounter+1)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 1-2
    tempChildState[1], tempChildState[2] = tempChildState[2], tempChildState[1]
    newChild = NodeDepth(currentNodeState, tempChildState, depthCounter+1)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 0-3
    tempChildState[0], tempChildState[3] = tempChildState[3], tempChildState[0]
    newChild = NodeDepth(currentNodeState, tempChildState,depthCounter+1)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 1-4
    tempChildState[1], tempChildState[4] = tempChildState[4], tempChildState[1]
    newChild = NodeDepth(currentNodeState, tempChildState, depthCounter+1)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 2-5
    tempChildState[2], tempChildState[5] = tempChildState[5], tempChildState[2]
    newChild = NodeDepth(currentNodeState, tempChildState, depthCounter+1)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 3-4
    tempChildState[3], tempChildState[4] = tempChildState[4], tempChildState[3]
    newChild = NodeDepth(currentNodeState, tempChildState, depthCounter+1)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 4-5
    tempChildState[4], tempChildState[5] = tempChildState[5], tempChildState[4]
    newChild = NodeDepth(currentNodeState, tempChildState, depthCounter+1)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 3-6
    tempChildState[3], tempChildState[6] = tempChildState[6], tempChildState[3]
    newChild = NodeDepth(currentNodeState, tempChildState, depthCounter+1)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 4-7
    tempChildState[4], tempChildState[7] = tempChildState[7], tempChildState[4]
    newChild = NodeDepth(currentNodeState, tempChildState, depthCounter+1)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 5-8
    tempChildState[5], tempChildState[8] = tempChildState[8], tempChildState[5]
    newChild = NodeDepth(currentNodeState, tempChildState, depthCounter+1)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 6-7
    tempChildState[6], tempChildState[7] = tempChildState[7], tempChildState[6]
    newChild = NodeDepth(currentNodeState, tempChildState,depthCounter+1)
    allChildren.append(newChild)
    tempChildState = copy.deepcopy(currentNodeState)
    # child 7-8
    tempChildState[7], tempChildState[8] = tempChildState[8], tempChildState[7]
    newChild = NodeDepth(currentNodeState, tempChildState, depthCounter+1)
    allChildren.append(newChild)

    return allChildren

# when the 12 children of a node is created by the method getAllChildren,
# we verify if the children state has already been visited
def getValidChildren(allChildren, closedList, openList):
    validChildren = []
    for child in allChildren:
        check = False
        for visitedC in closedList:
            if (child.state == visitedC.state):
                check = True
                break
        for visitedO in openList:
            if (child.state == visitedO.state):
                check = True
                break
        if (check == False):
            validChildren.append(child)
    return validChildren

# this method will compare the present with the goal and returns if it is the goal state
def compareGoal(currentNode: NodeDepth):
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if (currentNode.state == goal_state):
        return True
    else:
        return False

# this method is used when the goal has been found,
# it will trace back the parent of the goal node up to the root of the tree
# and will display the path in a file
def traceParent(solutionNode: NodeDepth, closedList):
    solutionCount = 0
    tempNode = solutionNode

    f = open("iterativeDeepeningSol.txt", "w")
    currentParent = tempNode.parent
    currentState = tempNode.state
    f.write("\n==============")
    f.write("\n\nParent: ")
    pcounter = 0
    for p in currentParent:
        if (pcounter % 3 == 0):
            f.write("\n")
        f.write(str(p) + " ")
        pcounter += 1
    f.write("\n\nState: ")
    scounter = 0
    for s in currentState:
        if (scounter % 3 == 0):
            f.write("\n")
        f.write(str(s) + " ")
        scounter += 1
    f.close()

    while (tempNode.parent != [0, 0, 0, 0, 0, 0, 0, 0, 0]):
        solutionCount += 1
        for closedNodes in closedList:
            if (closedNodes.state == tempNode.parent):
                tempNode = closedNodes
                f = open("iterativeDeepeningSol.txt", "a")
                currentParent = tempNode.parent
                currentState = tempNode.state
                f.write("\n==============")
                f.write("\n\nParent: ")
                pcounter = 0
                for p in currentParent:
                    if (pcounter % 3 == 0):
                        f.write("\n")
                    f.write(str(p) + " ")
                    pcounter += 1
                f.write("\n\nState: ")
                scounter = 0
                for s in currentState:
                    if (scounter % 3 == 0):
                        f.write("\n")
                    f.write(str(s) + " ")
                    scounter += 1
                f.close()
                break
    solutionCount += 1
    outputToFileLength(solutionCount, "iterativeLengthHolder.txt")

# The iterative deepening algorithm is implemented in this method
# Creation of the open and closed list
# Monitors the time to not exceed 60 seconds
def iterativeDeepeningAlgorithm (initial_state:list):
    startTime = datetime.now()
    currentTime = datetime.now()

    openList = []
    closedList = []
    depthList = []
    openList.append(NodeDepth([0,0,0,0,0,0,0,0,0],initial_state,1))

    while (openList.count != 0):
        currentTime = datetime.now()
        delta = currentTime - startTime
        if delta.total_seconds()>= 2:
            f = open("iterativeDeepeningSol.txt", "w")
            f.write("Time of execution greater than 60 seconds")
            f.close
            fd = open("iterativeNoSol.txt", "r")
            currentNosol = sum(map(int, fd.readlines()))
            currentNosol += 1
            fd.close
            fd = open("iterativeNoSol.txt", "w")
            fd.write(str(currentNosol))
            fd.close()
            break
        maxDepth = 2
        x = openList.pop()
        if compareGoal(x):
            solutionNode = x
            traceParent(solutionNode,closedList)
            closedList.append(x)
            break
        else:
            allXChildren = getAllChildren(x)
            closedList.append(x)
            allValidXChildren = getValidChildren(allXChildren, closedList, openList)
            if x.depth%(maxDepth-1)!=0:
                for validChild in reversed(allValidXChildren):
                    openList.append(validChild)
            else:
                for validChild in reversed(allValidXChildren):
                    depthList.append(validChild)
                if len(openList)==0:
                    openList = depthList

    f = open("iterativeDeepeningVisited.txt", "w")
    for currentnode in closedList:
        currentParent = currentnode.parent
        currentState = currentnode.state
        f.write("\n==============")
        f.write("\n\nParent: ")
        pcounter = 0
        for p in currentParent:
            if(pcounter%3 == 0):
                f.write("\n")
            f.write(str(p)+" ")
            pcounter+=1
        f.write("\n\nState: ")
        scounter = 0
        for s in currentState:
            if(scounter%3 == 0):
                f.write("\n")
            f.write(str(s)+" ")
            scounter+=1
    f.close()

# call randomGen and creates and initialize the file for the analysis
randomGen()
listOfInputs = getInput("20.txt")
fd = open("iterativeNoSol.txt", "w")
fd.write("0")
fd.close()

fd = open("iterativeLengthHolder.txt", "w")
fd.write("0")
fd.close()

print("\n")
# start the time and call the analysis with the list of 20 puzzles
# works with the results of the analysis in files and the results are  displayed in the console
start_timeh2 = time.time()
iterativeDeepAnalysis1(listOfInputs)
print("Total Time iterative deepening:", time.time() - start_timeh2, "seconds")
print("Average Time iterative deepening:", (time.time() - start_timeh2) / 20, "seconds")

fd = open("iterativeNoSol.txt", "r")
currentNosolutions = int(fd.readline())
fd.close

print("Total No solutions for iterative deepening :", currentNosolutions)
print("Average No solutions for iterative deepening :", (currentNosolutions / 20)*100, " %")


fd = open("iterativeLengthHolder.txt","r")
lengthTotal = sum(map(int, fd.readlines()))
averageTotal = lengthTotal / 20
fd.close()


print("Total length for iterative deepening :", lengthTotal)
print("Average length for iterative deepening :", averageTotal)

print("Total cost for iterative deepening :", lengthTotal, " Solution Depth")
print("Average cost for iterative deepening :", averageTotal, " Solution Depth")

fd.close()
os.remove("iterativeNoSol.txt")
os.remove("iterativeLengthHolder.txt")
