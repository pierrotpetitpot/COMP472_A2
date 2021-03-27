from node import *
import copy
from datetime import datetime


def aStar(root, goal):
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
            f = open("iterativeDeepeningSol.txt", "w")
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
        print(bestChild.state)
        targetNode = copy.deepcopy(bestChild)
        listOfCosts = []


def aStar2(root, goal):
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
            f = open("iterativeDeepeningSol.txt", "w")
            f.write("Time of execution greater than 60 seconds")
            f.close
            break
        listOfChildren = getAllChildren(targetNode)

        for child in listOfChildren:
            listOfCosts.append(getCost2(child, goal))
        bestChild = getBestChild(listOfChildren, listOfCosts)
        visitedChildrenState.append(bestChild.state)
        print(bestChild.state)
        targetNode = copy.deepcopy(bestChild)
        listOfCosts = []

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

goal = [1,2,3,4,5,6,7,8,9]
aNode = Node(None, [9,8,7,6,5,4,3,2,1])


aStar(aNode, goal)
print("\n")
aStar2(aNode, goal)
