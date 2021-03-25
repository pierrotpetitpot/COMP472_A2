from main import *
from node import *
import copy


def aStar(root, goal):
    listOfCosts = []
    targetNode = copy.deepcopy(root)

    while goal != targetNode.state:
        listOfChildren = getAllChildren(targetNode)

        for child in listOfChildren:
            listOfCosts.append(getCost(child, goal))

        indexLowestCost = listOfCosts.index(min(listOfCosts))
        bestChild = listOfChildren(indexLowestCost)
        print(bestChild.state + "\n")
        targetNode = copy.deepcopy(bestChild)


# get the cost
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


goal = [2, 1, 3, 4, 5, 6, 7, 8, 9]

aNode = Node(None, [1, 2, 3, 4, 5, 6, 7, 8, 9])

aStar(aNode, goal)
