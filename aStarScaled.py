import random
import copy
from datetime import datetime
import math
from aStar import getBestChild
from statistics import *
import csv
import matplotlib.pyplot as plt
import os


# creates a file with costumed dimension puzzles
def genericRandomGen(numberOfPuzzles, dimensions):
    f1 = open("scaledPuzzlesToDelete.txt", "w")
    f2 = open("scaledPuzzles.txt", "a")

    size = dimensions * dimensions

    for x in range(numberOfPuzzles):
        list = random.sample(range(1, size + 1), size)
        f1.write(str(list))
        f1.write("\n")

        f2.write(str(list))
        f2.write("\n")

    f1.close
    f2.close


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
    results = getHalfChildren(verticalState, dimensions)
    secondHalf = []
    for result in results:
        secondHalf.append(verticalize(result, dimensions))

    totalChildren = firstHalf + secondHalf

    random.shuffle(totalChildren)

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


# generic aStar
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
        if delta.total_seconds() >= 60:
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


# aStar is applied for all puzzles of fixed n x n dimensions
def getResults(puzzles):
    listOfStatistics = []
    for puzzle in puzzles:
        goal = list(range(1, len(puzzle) + 1))
        result = aStarScaled(puzzle, goal)
        listOfStatistics.append(result)

    return listOfStatistics


# get stats for the puzzles solved in n x n dimensions
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

    totalTime = sum([d.microseconds for d in listOfTimes])

    statisticsDictionary = {
        "totalLength": totalLength,
        "averageLength": totalLength / len(results),
        "totalNoSolution": noSolutionCount,
        "averageNoSolution": noSolutionCount / len(results),
        "totalCost": totalCost,
        "averageCost": totalCost / len(results),
        "totalTime": totalTime,
        "averageTime": totalTime / len(results)
    }

    return statisticsDictionary


# output stats in a file
def outputStats(filename, dictionary):
    f = open(filename, "a")
    f.write("Total length: " + str(dictionary["totalLength"]))
    f.write("\n")

    f.write("Average length: " + str(dictionary["averageLength"]))
    f.write("\n")

    f.write("Total noSolution: " + str(dictionary["totalNoSolution"]))
    f.write("\n")

    f.write("Average noSolution: " + str(dictionary["averageNoSolution"]))
    f.write("\n")

    f.write("Total cost: " + str(dictionary["totalCost"]))
    f.write("\n")

    f.write("Average cost: " + str(dictionary["averageCost"]))
    f.write("\n")

    f.write("Total time(in microseconds): " + str(dictionary["totalTime"]))
    f.write("\n")

    f.write("Average time(in microseconds): " + str(dictionary["averageTime"]))
    f.write("\n")

    f.write("\n")
    f.write("\n")
    f.write("\n")

    f.close


# outputs solutions paths for each puzzles of n by n size
def outputSolutionPaths(results):
    f1 = open("solutionPathsForScaled.txt", "w")

    for result in results:
        for state in result.listOfPaths:
            f1.write(str(list(state)))
    f1.write("\n")

    f1.close


# apply aStar for puzzles of n by n, get stats and output them in a file
def aStarScaledAnalysis(puzzles):
    results = getResults(puzzles)
    dictionary = getStatistics(results)
    outputStats("aStarScaledStatistics.txt", dictionary)

    return dictionary


# plots a single graph for a specific stat
def singleGraph(xAxis, yAxis, xLabel, yLabel, title):
    plt.plot(xAxis, yAxis)
    plt.xticks(range(xAxis[0], len(xAxis) + (1 + xAxis[0])))
    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(title)
    plt.show()


def deleteFileSafely(filename):
    if os.path.exists(filename):
        os.remove(filename)


# graphs multiple plots where x axis is the puzzles dimensions, and y axis are the stats.
# this function generates X number of puzzles of various sizes between start and end dimensions, applies aStar for all the puzzles
# and generates the data to be plotted in the graph
def graphPlotting(numberOfPuzzles, startDimensions, endDimensions):
    listOfDictionaries = []
    for i in range(startDimensions, endDimensions + 1):
        genericRandomGen(numberOfPuzzles, i)
        statistics = aStarScaledAnalysis(getInput("scaledPuzzlesToDelete.txt"))
        listOfDictionaries.append(statistics)

    xAxis = list(range(startDimensions, endDimensions + 1, 1))

    # yAxis
    averageCosts = []
    averageLength = []
    averageTime = []
    averageNoSolution = []

    for dictionary in listOfDictionaries:
        averageCosts.append(dictionary["averageCost"])
        averageLength.append(dictionary["averageLength"])
        averageTime.append(dictionary["averageTime"])
        averageNoSolution.append(dictionary["averageNoSolution"])

    singleGraph(xAxis, averageTime, "dimensions", "Time in micro seconds", "stats")
    singleGraph(xAxis, averageLength, "dimensions", "Average length", "stats")
    singleGraph(xAxis, averageCosts, "dimensions", "Average cost", "stats")
    singleGraph(xAxis, averageNoSolution, "dimensions", "Average no solution", "stats")


graphPlotting(10, 2, 6)
deleteFileSafely("scaledPuzzlesToDelete.txt")
