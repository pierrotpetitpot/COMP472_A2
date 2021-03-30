from node import Node
import copy
from datetime import datetime

import os
import time
import random
import csv


def depthFirstAnalysis1(inputs):
    for input in inputs:
        depthFirstAlgorithm(input)


def randomGen():
    f = open("20.txt", "w")
    for x in range(20):
        list = random.sample(range(1, 10), 9)
        f.write(str(list))
        f.write("\n")
    f.close


def outputToFileLength(path, filename):
    f = open(filename, "a")
    f.write(str(path))
    f.write(str("\n"))
    f.close


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


def compareGoal(currentNode: Node):
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if (currentNode.state == goal_state):
        return True
    else:
        return False


def traceParent(solutionNode: Node, closedList):
    solutionCount = 0
    tempNode = solutionNode

    f = open("depthFirstSolution.txt", "w")
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
                f = open("depthFirstSolution.txt", "a")
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
    outputToFileLength(solutionCount, "depthFirstLengthHolder.txt")


def depthFirstAlgorithm(initial_state: list):
    openList = []
    closedList = []
    openList.append(Node([0, 0, 0, 0, 0, 0, 0, 0, 0], initial_state))
    startTime = datetime.now()

    while (openList.count != 0):
        currentTime = datetime.now()
        delta = currentTime - startTime
        if delta.total_seconds() >= 60:
            f = open("depthFirstSolution.txt", "w")
            f.write("Time of execution greater than 60 seconds")
            f.close
            fd = open("depthFirstNosolution.txt", "r")
            currentNosol = sum(map(int, fd.readlines()))
            currentNosol += 1
            fd.close
            fd = open("depthFirstNosolution.txt", "w")
            fd.write(str(currentNosol))
            fd.close()
            break
        x = openList.pop()
        if (compareGoal(x)):
            solutionNode = x
            traceParent(solutionNode, closedList)
            closedList.append(x)
            break
        else:
            allXChildren = getAllChildren(x)
            closedList.append(x)
            allValidXChildren = getValidChildren(allXChildren, closedList, openList)
            for validChild in reversed(allValidXChildren):
                openList.append(validChild)

    f = open("depthFirstVisited.txt", "w")
    for currentnode in closedList:
        currentParent = currentnode.parent
        currentState = currentnode.state
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


randomGen()
listOfInputs = getInput("20.txt")
fd = open("depthFirstNosolution.txt", "w")
fd.write("0")
fd.close()

fd = open("depthFirstLengthHolder.txt", "w")
fd.write("0")
fd.close()

print("\n")

start_timeh2 = time.time()
depthFirstAnalysis1(listOfInputs)
print("Total Time depthFirst:", time.time() - start_timeh2, "seconds")
print("Average Time depthFirst:", (time.time() - start_timeh2) / 20, "seconds")

fd = open("depthFirstNosolution.txt", "r")
currentNosolutions = int(fd.readline())
fd.close

print("Total No solutions for DepthFirst :", currentNosolutions)
print("Average No solutions for DepthFirst :", currentNosolutions / 20)


fd = open("depthFirstLengthHolder.txt","r")
lengthTotal = sum(map(int, fd.readlines()))
averageTotal = lengthTotal / 20
fd.close()


print("Total length for DepthFirst :", lengthTotal)
print("Average length for DepthFirst :", averageTotal)

print("Total cost for DepthFirst :", lengthTotal, " Solution Depth")
print("Average cost for DepthFirst :", averageTotal, " Solution Depth")

fd.close()
os.remove("depthFirstNosolution.txt")
os.remove("depthFirstLengthHolder.txt")
