from main import *
from node import *
import copy


def aStar(root, goal):
    listOfCosts = []
    targetNode = copy.deepcopy(root)
    visitedChildren = []

    while goal != targetNode.state:
        listOfChildren = getAllChildren(targetNode)

        for child in listOfChildren:
            if hasBeenVisited(child, visitedChildren):
                continue
            listOfCosts.append(getCost(child, goal))

        indexLowestCost = listOfCosts.index(min(listOfCosts))
        bestChild = listOfChildren(indexLowestCost)
        visitedChildren.append(bestChild.state)
        print(bestChild.state + "\n")
        targetNode = copy.deepcopy(bestChild)


# Cost is based on the amount of effort it would take for a state to get to the goal state.
# For example, if we were 1 swap away from the goal state, the cost would be 2 because two numbers are not
# where they should be.
def getCost(child, goal):
    totalCost = 0
    for i in range(9):
        targetIndex = child.state.index(i)
        goalIndex = goal.state.index(i)
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
        if child == visitedChild:
            visited = True
    return visited


goal = [2, 1, 3, 4, 5, 6, 7, 8, 9]

aNode = Node(None, [1, 2, 3, 4, 5, 6, 7, 8, 9])

aStar(aNode, goal)
