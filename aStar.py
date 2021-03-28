from node import *
import copy
from datetime import datetime
import random


def randomGen():
    f = open("20.txt", "w")
    for x in range(20):
        list = random.sample(range(1, 10), 9)
        f.write(str(list))
        f.write("\n")
    f.close


def aStar(root, goal):
    listOfOutput = []
    listOfCosts = []
    targetNode = copy.deepcopy(root)
    visitedChildrenState = []
    startTime = datetime.now()
    currentTime = datetime.now()

    while goal != targetNode.state:
        currentTime = datetime.now()
        delta = currentTime - startTime
        if delta.total_seconds() >= 2:
            # change the name of the file
            f = open("defaultHeuristicSolution.txt", "w")
            f.write("Time of execution greater than 60 seconds")
            f.close
            f = open("defaultHeuristicPath.txt", "w")
            f.write("Time of execution greater than 60 seconds")
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
        listOfCosts = []
    aStarOutputSolution(listOfOutput)
    aStarOutputPath(listOfOutput)


def aStar2(root, goal):
    listOfOutput = []
    listOfCosts = []
    targetNode = copy.deepcopy(root)
    visitedChildrenState = []
    startTime = datetime.now()
    currentTime = datetime.now()
    while goal != targetNode.state:
        currentTime = datetime.now()
        delta = currentTime - startTime
        if delta.total_seconds() >= 60:
            # change the name of the file
            f = open("EuclideanHeuristicSolution.txt", "w")
            f.write("Time of execution greater than 60 seconds")
            f.close
            f = open("EuclideanHeuristicPath.txt", "w")
            f.write("Time of execution greater than 60 seconds")
            f.close
            break
        listOfChildren = getAllChildren(targetNode)

        for child in listOfChildren:
            listOfCosts.append(getCost2(child, goal))
        bestChild = getBestChild(listOfChildren, listOfCosts)
        visitedChildrenState.append(bestChild.state)
        listOfOutput.append(bestChild.state)
        targetNode = copy.deepcopy(bestChild)
        listOfCosts = []
    aStar2OutputSolution(listOfOutput)
    aStar2OutputPath(listOfOutput)


def aStarOutputSolution(path):
    file = open("defaultHeuristicSolution.txt", "w")
    for state in path:
        currentState = state
        file.write("\n==============")
        file.write("\n\nState: ")
        scounter = 0
        for s in currentState:
            if scounter % 3 == 0:
                file.write("\n")
            file.write(str(s) + " ")
            scounter += 1
    file.close()


def aStarOutputPath(path):
    file = open("defaultHeuristicPath.txt", "w")
    for state in path:
        currentState = state
        file.write("\n==============")
        file.write("\n\nState: ")
        scounter = 0
        for s in currentState:
            if scounter % 3 == 0:
                file.write("\n")
            file.write(str(s) + " ")
            scounter += 1
    file.close()


def aStar2OutputSolution(path):
    file = open("EuclideanHeuristicSolution.txt", "w")
    for state in path:
        currentState = state
        file.write("\n==============")
        file.write("\n\nState: ")
        scounter = 0
        for s in currentState:
            if scounter % 3 == 0:
                file.write("\n")
            file.write(str(s) + " ")
            scounter += 1
    file.close()


def aStar2OutputPath(path):
    file = open("EuclideanHeuristicPath.txt", "w")
    for state in path:
        currentState = state
        file.write("\n==============")
        file.write("\n\nState: ")
        scounter = 0
        for s in currentState:
            if scounter % 3 == 0:
                file.write("\n")
            file.write(str(s) + " ")
            scounter += 1
    file.close()


# Cost is based on the amount of effort it would take for a state to get to the goal state.
# For example, if we were 1 swap away from the goal state, the cost would be 2 because two numbers are not
# where they should be.
def getCost(child, goal):
    totalCost = 0
    for i in range(1, 9, 1):
        targetIndex = child.state.index(i)
        goalIndex = goal.index(i)
        totalCost += (getHorizontalCost(targetIndex, goalIndex) + getVerticalCost(targetIndex, goalIndex))
    return totalCost


def getCost2(child, goal):
    totalCost = 0
    for i in range(1, 9, 1):
        targetIndex = child.state.index(i)
        goalIndex = goal.index(i)
        totalCost += (getHorizontalCost(targetIndex, goalIndex) * getHorizontalCost(targetIndex, goalIndex) +
                      getVerticalCost(targetIndex, goalIndex) * getVerticalCost(targetIndex, goalIndex))
    return totalCost


# vertical cost is calculated by getting the floor value of an index division by 3
def getVerticalCost(targetVertical, goalVertical):
    targetPosition = targetVertical // 3
    goalPosition = goalVertical // 3
    verticalCost = abs(targetPosition - goalPosition)
    return verticalCost


# horizontal cost is calculated by getting the modulus 3 of in the index
def getHorizontalCost(targetHorizontal, goalHorizontal):
    targetPosition = targetHorizontal % 3
    goalPosition = goalHorizontal % 3
    horizontalCost = abs(targetPosition - goalPosition)
    return horizontalCost


# return if the child has already been visited
def hasBeenVisited(child, visitedChildren):
    visited = False
    for visitedChild in visitedChildren:
        if child.state == visitedChild:
            visited = True
    return visited


def getBestChild(children, listOfCosts):
    if len(listOfCosts) > 0:
        indexLowestCost = listOfCosts.index(min(listOfCosts))
        bestChild = children[indexLowestCost]
        return bestChild
    else:
        return


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


goal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
aNode = Node(None, [3, 1, 5, 6, 8, 7, 9, 4, 2])

randomGen()

# my_file = open("20.txt", "r")
# content_list = my_file.readlines()
# aNode = Node(None, content_list)
# aStar(aNode, goal)

aStar(aNode, goal)
# aStar2(aNode, goal)
