from nodeDepth import NodeDepth
import copy
from datetime import datetime


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

def compareGoal(currentNode: NodeDepth):
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if (currentNode.state == goal_state):
        return True
    else:
        return False

def traceParent(solutionNode:NodeDepth,closedList):
    tempNode = solutionNode

    f = open("iterativeDeepeningSol.txt", "w")
    currentParent = tempNode.parent
    currentState = tempNode.state
    f.write("\n==============")
    f.write("\n\nParent: ")
    pcounter = 0
    for p in currentParent:
        if(pcounter % 3 == 0):
            f.write("\n")
        f.write(str(p)+" ")
        pcounter+=1
    f.write("\n\nState: ")
    scounter = 0
    for s in currentState:
        if(scounter %3 == 0):
            f.write("\n")
        f.write(str(s)+" ")
        scounter+=1
    f.close()

    while (tempNode.parent != [0, 0, 0, 0, 0, 0, 0, 0, 0]):
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
        if delta.total_seconds()>= 60:
            f = open("iterativeDeepeningSol.txt", "w")
            f.write("Time of execution greater than 60 seconds")
            f.close
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
