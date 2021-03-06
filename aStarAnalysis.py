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
import re
import os
import time

#randomize the puzzle

def randomGen():
    f = open("20.txt", "w")
    for x in range(20):
        list = random.sample(range(1, 10), 9)
        f.write(str(list))
        f.write("\n")
    f.close


# outputs average and total for h1
def aStarPrime(root, goal):
    listOfOutput = []
    listOfCosts = []
    targetNode = copy.deepcopy(root)
    visitedChildrenState = []
    startTime = datetime.now()
    currentTime = datetime.now()
    totalLength = 0
    puzzleCost = 0

    while goal != targetNode.state:
        currentTime = datetime.now()
        delta = currentTime - startTime

        if delta.total_seconds() >= 60:
            # change the name of the file
            f = open("analysisAStar_h1_p0.txt", "a")
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
        outputToFile(listOfOutput, "analysisAStar_h1_p0.txt")
        # outputToFileLength(path, "analysisAStar_h1(2).txt")

        puzzleCost += min(listOfCosts)
        listOfCosts = []

    length = len(listOfOutput)
    outputToFileLengthHolder(length, "aStarlengthHolder_h1.txt")
    outputSinglePuzzleCost(puzzleCost, "aStarPuzzleCost_h1.txt")

    with open("aStarlengthHolder_h1.txt") as fh:
        lengthTotal = sum(map(int, fh.readlines()))
        averageTotal = lengthTotal / 20
    f = open("analysisAStar_h1_p1.txt", "w")
    f.write("The total length of solution and search paths: ")
    f.write(str(lengthTotal))
    f.write("\n")
    f.write("The average length of solution and search paths: ")
    f.write(str(averageTotal))
    f.write(str("\n"))


# outputs average and total for h2
def aStarPrime2(root, goal):
    listOfOutput = []
    listOfCosts = []
    targetNode = copy.deepcopy(root)
    visitedChildrenState = []
    startTime = datetime.now()
    currentTime = datetime.now()
    totalLength = 0
    puzzleCost = 0


    while goal != targetNode.state:
        currentTime = datetime.now()
        delta = currentTime - startTime

        if delta.total_seconds() >= 60:
            # change the name of the file
            f = open("analysisAStar_h2_p0.txt", "a")
            f.write("Time of execution greater than 60 seconds" "\n")
            f.close
            break
        listOfChildren = getAllChildren(targetNode)

        for child in listOfChildren:
            listOfCosts.append(getCost2(child, goal))
        bestChild = getBestChild(listOfChildren, listOfCosts)
        if bestChild is None:
            return
        visitedChildrenState.append(bestChild.state)
        listOfOutput.append(bestChild.state)
        targetNode = copy.deepcopy(bestChild)
        outputToFile(listOfOutput, "analysisAStar_h2_p0.txt")
        # outputToFileLength(path, "analysisAStar_h1(2).txt")
        puzzleCost += min(listOfCosts)
        listOfCosts = []

    length = len(listOfOutput)
    outputToFileLengthHolder(length, "aStarlengthHolder_h2.txt")
    outputSinglePuzzleCost(puzzleCost, "aStarPuzzleCost_h2.txt")


    with open("aStarlengthHolder_h2.txt") as fh:
        lengthTotal = sum(map(int, fh.readlines()))
        averageTotal = lengthTotal / 20
    f = open("analysisAStar_h2_p1.txt", "w")
    f.write("The total length of solution and search paths: ")
    f.write(str(lengthTotal))
    f.write("\n")
    f.write("The average length of solution and search paths: ")
    f.write(str(averageTotal))
    f.write(str("\n"))

# write to a file the length
def outputToFileLength(path, filename):
    f = open(filename, "w")
    f.write(str(path))
    f.write(str("\n"))
    f.close

# write to a file for the length holder
def outputToFileLengthHolder(path, filename):
    f = open(filename, "a")
    f.write(str(path))
    f.write(str("\n"))
    f.close

# write the states to the output file
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

# method that calls the aStarPrime with the puzzles
def aStarAnalysis1(inputs, goalState):
    for input in inputs:
        f = open("analysisAStar_h1_p0.txt", "a")
        f.write("\n===========NEW PUZZLE===========\n")
        f.close
        aStarPrime(input, goalState)
    outputAverageCost("aStarPuzzleCost_h1.txt", "averagePuzzleCost_h1.txt")

# method that calls the aStarPrime2 with the puzzles
def aStarAnalysis2(inputs, goalState):
    for input in inputs:
        f = open("analysisAStar_h2_p0.txt", "a")
        f.write("\n===========NEW PUZZLE===========\n")
        f.close
        aStarPrime2(input, goalState)

    outputAverageCost("aStarPuzzleCost_h2.txt", "averagePuzzleCost_h2.txt")

#method to get all the 12 possible children of a node
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

# write to a file that outputs the puzzle cost
def outputSinglePuzzleCost(puzzleCost, fileName):
    f = open(fileName, "a")
    f.write(str(puzzleCost))
    f.write(str("\n"))
    f.close

# write to a file that outputs the average cost
def outputAverageCost(fileNameRead,fileNameWrite):
    with open(fileNameRead) as fh:
        totalcost = sum(map(int, fh.readlines()))
        averageCost = totalcost / 20
    f = open(fileNameWrite, "w")
    f.write("The total cost for all puzzle is: ")
    f.write(str(totalcost))
    f.write("\n")
    f.write("The average cost for a puzzle is: ")
    f.write(str(averageCost))
    f.write(str("\n"))

randomGen()

# test = [8, 4, 7, 1, 5, 6, 9, 3, 2]


goal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listOfInputs = getInput("20.txt")

print("\n")

start_timeh2 = time.time()
aStarAnalysis1(listOfInputs, goal)
print("Total Time h1:", time.time() - start_timeh2, "seconds")
print("Average Time h1:", (time.time() - start_timeh2) / 20, "seconds")

print("\n")

start_timeh2 = time.time()
aStarAnalysis2(listOfInputs, goal)
print("Total Time h2:", time.time() - start_timeh2, "seconds")
print("Average Time h2:", (time.time() - start_timeh2) / 20, "seconds")

os.remove("aStarlengthHolder_h1.txt")
os.remove("aStarlengthHolder_h2.txt")
