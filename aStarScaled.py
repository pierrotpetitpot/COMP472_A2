import random
from node import *
import copy
from datetime import datetime
import math
from aStar import getBestChild
from aStar import aStar2
from statistics import *
from pprint import pprint
import csv


# creates a file with costumed dimension puzzles
def genericRandomGen(numberOfPuzzles, dimensions):
    f = open("scale.txt", "w")
    size = dimensions * dimensions

    for x in range(numberOfPuzzles):
        list = random.sample(range(1, size + 1), size)
        f.write(str(list))
        f.write("\n")
    f.close


# returns a list of nodes where each node is a puzzle from 20.txt
def getInput(filename):
    inputs = []
    with open(filename, 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            row = str(row)
            formattedRow = row.replace("[", "").replace("]", "").replace("'", "")
            puzzle = [int(x) for x in formattedRow.split(',')]
            inputs.append(puzzle)

    return inputs


# returns a list of children derived from a state
def getTotalChildrenScaled(state):
    dimensions = int(math.sqrt(len(state)))

    firstHalf = getHalfChildren(state, dimensions)
    verticalState = verticalize(state, dimensions)
    secondHalf = getHalfChildren(verticalState, dimensions)

    totalChildren = firstHalf + secondHalf
    return totalChildren


# returns only half of the children
def getHalfChildren(state, dimensions):
    listOfChildren = []
    for i in range(len(state)):
        if i % dimensions == (dimensions - 1):
            continue
        originalState = copy.deepcopy(state)
        listOfChildren.append(swapPositions(originalState, i, i + 1))
    return listOfChildren


# divides a list into smaller chunks
def chunks(list, dimensions):
    for i in range(0, len(list), dimensions):
        yield list[i:i + dimensions]


# returns a state where the rows are columns
def verticalize(state, dimensions):
    listOfChunks = list(chunks(state, dimensions))
    verticalState = []
    for i in range(dimensions):
        for chunk in listOfChunks:
            verticalState.append(chunk[i])

    return verticalState


# returns a list where elements are swapped
def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list


# returns euclidian distance
def getCostScaled(child, goal):
    dimensions = int(math.sqrt(len(child)))
    totalCost = 0
    for i in range(1, (dimensions * dimensions), 1):
        targetIndex = child.index(i)
        goalIndex = goal.index(i)
        totalCost += (getVerticalCostScaled(targetIndex, goalIndex, dimensions) * getVerticalCostScaled(targetIndex,
                                                                                                        goalIndex,
                                                                                                        dimensions) +
                      getHorizontalCostScaled(targetIndex, goalIndex, dimensions) * getHorizontalCostScaled(targetIndex,
                                                                                                            goalIndex,
                                                                                                            dimensions))
    return totalCost


# vertical cost is calculated by getting the floor value of an index division by "dimension"
def getVerticalCostScaled(targetVertical, goalVertical, dimensions):
    targetPosition = targetVertical // dimensions
    goalPosition = goalVertical // dimensions
    verticalCost = abs(targetPosition - goalPosition)
    return verticalCost


# horizontal cost is calculated by getting the modulus "dimension" of in the index
def getHorizontalCostScaled(targetHorizontal, goalHorizontal, dimensions):
    targetPosition = targetHorizontal % dimensions
    goalPosition = goalHorizontal % dimensions
    horizontalCost = abs(targetPosition - goalPosition)
    return horizontalCost


def aStarScaled(root, goal):
    targetNode = copy.deepcopy(root)
    listOfCosts = []
    startTime = datetime.now()

    # statistics
    solutionLength = 0
    noSolution = False
    cost = 0
    executionTime = 0
    listOfPaths = []

    while goal != targetNode:
        currentTime = datetime.now()
        delta = currentTime - startTime
        if delta.total_seconds() >= 2:
            noSolution = True
            break

        listOfChildren = getTotalChildrenScaled(targetNode)

        for child in listOfChildren:
            listOfCosts.append(getCostScaled(child, goal))

        bestChild = getBestChild(listOfChildren, listOfCosts)

        # print(bestChild)

        solutionLength = solutionLength + 1
        cost += min(listOfCosts)
        listOfPaths.append(bestChild)

        targetNode = copy.deepcopy(bestChild)
        listOfCosts = []

    endTime = datetime.now()
    executionTime = endTime - startTime

    statistics = Statistics(solutionLength, noSolution, cost, executionTime, listOfPaths)

    return statistics


def getResults(puzzles):
    listOfStatistics = []
    for puzzle in puzzles:
        goal = list(range(len(puzzle)))
        result = aStarScaled(puzzle, goal)
        listOfStatistics.append(result)

    return listOfStatistics


def getStatistics(results):
    totalLength = 0
    noSolutionCount = 0
    totalCost = 0
    listOfTimes = []

    for result in results:

        totalLength += result.length

        if result.noSolution:
            noSolutionCount = noSolutionCount + 1

        totalCost += result.cost

        listOfTimes.append(result.executionTime)

    totalTime = sum([d.seconds for d in listOfTimes])

    statisticsDictionary = {
        "totalLength": totalLength,
        "averageLength": totalLength/len(results),
        "totalNoSolution": noSolutionCount,
        "averageNoSolution": noSolutionCount/len(results),
        "totalCost": totalCost,
        "averageCost": totalCost/len(results),
        "totalTime": totalTime,
        "averageTime": totalTime/len(results)
    }

    return statisticsDictionary


def aStarScaledAnalysis(puzzles):
    results = getResults(puzzles)

    dictionary = getStatistics(results)

    f = open("statistics.txt", "w")
    f.write("Total length: "+str(dictionary["totalLength"]))
    f.write("\n")

    f.write("Average length: "+str(dictionary["averageLength"]))
    f.write("\n")

    f.write("Total noSolution: "+str(dictionary["totalNoSolution"]))
    f.write("\n")

    f.write("Average noSolution: "+str(dictionary["averageNoSolution"]))
    f.write("\n")

    f.write("Total cost: "+str(dictionary["totalCost"]))
    f.write("\n")

    f.write("Average cost: "+str(dictionary["averageCost"]))
    f.write("\n")

    f.write("Total time: "+str(dictionary["totalTime"]))
    f.write("\n")

    f.write("Average time: "+str(dictionary["averageTime"]))
    f.write("\n")
    f.close







# goal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# state = [2, 3, 1, 5, 6, 4, 7, 9, 8]

goal = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
state = [2, 1, 3, 4, 5, 7, 6, 8, 9, 11, 10, 12, 13, 14, 16, 15]

# result = aStarScaled(state, goal)
# pprint(result.listOfPaths)

genericRandomGen(5, 3)
aStarScaledAnalysis(getInput("scale.txt"))
