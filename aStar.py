from main import *
from node import *
import copy


def aStar(root, goal):
    listOfCosts = []
    targetNode = copy.deepcopy(root)
    visitedChildrenState = []

    while goal != targetNode.state:
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


# Cost is based on the amount of effort it would take for a state to get to the goal state.
# For example, if we were 1 swap away from the goal state, the cost would be 2 because two numbers are not
# where they should be.
def getCost(child, goal):
    totalCost = 0
    for i in range(1,9,1):
        targetIndex = child.state.index(i)
        goalIndex = goal.index(i)
        totalCost += (getHorizontalCost(targetIndex, goalIndex) + getVerticalCost(targetIndex, goalIndex))
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
    if  len(listOfCosts) > 0:
        indexLowestCost = listOfCosts.index(min(listOfCosts))
        bestChild = children[indexLowestCost]
        return bestChild
    else:
        return



goal = [1,2,3,4,5,6,7,8,9]

aNode = Node(None, [6,1,2,7,8,3,5,4,9])

aStar(aNode, goal)
