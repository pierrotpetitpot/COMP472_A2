from node import Node
import copy
from datetime import datetime

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

# when the 12 children of a node is created by the method getAllChildren,
# we verify if the children state has already been visited
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

# this method will compare the present with the goal and returns if it is the goal state
def compareGoal(currentNode: Node):
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    if (currentNode.state == goal_state):
        return True
    else:
        return False

# this method is used when the goal has been found,
# it will trace back the parent of the goal node up to the root of the tree
# and will display the path in a file
def traceParent(solutionNode:Node,closedList):
    tempNode = solutionNode

    f = open("depthFirstSolution.txt", "w")
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

    while(tempNode.parent != [0,0,0,0,0,0,0,0,0]):
        for closedNodes in closedList:
            if(closedNodes.state == tempNode.parent):
                tempNode = closedNodes
                f = open("depthFirstSolution.txt", "a")
                currentParent = tempNode.parent
                currentState = tempNode.state
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
                break

# The depth first algorithm is implemented in this method
# Creation of the open and closed list
# Monitors the time to not exceed 60 seconds
def depthFirstAlgorithm (initial_state:list):
    openList = []
    closedList = []
    openList.append(Node([0,0,0,0,0,0,0,0,0],initial_state))
    startTime = datetime.now()
    currentTime = datetime.now()

    # when there is still content in the openlist
    # Pop the node and compare with the goal
    # If it is the goal, call the method traceParent
    # If not, the children of the node will be created
    while (openList.count != 0):
        currentTime = datetime.now()
        delta = currentTime - startTime
        if delta.total_seconds() >= 60:
            f = open("depthFirstSolution.txt", "w")
            f.write("Time of execution greater than 60 seconds")
            f.close
            break
        x = openList.pop()
        if(compareGoal(x)):
            solutionNode = x
            traceParent(solutionNode,closedList)
            closedList.append(x)
            break
        else:
            allXChildren = getAllChildren(x)
            closedList.append(x)
            allValidXChildren = getValidChildren(allXChildren,closedList,openList)
            for validChild in reversed(allValidXChildren):
                openList.append(validChild)

    # Writes all the visited node in a file
    f = open("depthFirstVisited.txt", "w")
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