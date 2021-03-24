from node import Node
from queue import LifoQueue
initial_state = [2,1,3,4,5,6,7,8,9]

def getAllChildren(node:Node):
    currentNodeState = node.state
    tempChildState = currentNodeState
    allChildren = []
    # child 0-1
    tempChildState[0], tempChildState[1] = tempChildState[1], tempChildState[0]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.append(newChild)
    tempChildState = currentNodeState
    # child 1-2
    tempChildState[1], tempChildState[2] = tempChildState[2], tempChildState[1]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.append(newChild)
    tempChildState = currentNodeState
    # child 0-3
    tempChildState[0], tempChildState[3] = tempChildState[3], tempChildState[0]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.append(newChild)
    tempChildState = currentNodeState
    # child 1-4
    tempChildState[1], tempChildState[4] = tempChildState[4], tempChildState[1]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.append(newChild)
    tempChildState = currentNodeState
    # child 2-5
    tempChildState[2], tempChildState[5] = tempChildState[5], tempChildState[2]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.append(newChild)
    tempChildState = currentNodeState
    # child 3-4
    tempChildState[3], tempChildState[4] = tempChildState[4], tempChildState[3]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.append(newChild)
    tempChildState = currentNodeState
    # child 4-5
    tempChildState[4], tempChildState[5] = tempChildState[5], tempChildState[4]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.append(newChild)
    tempChildState = currentNodeState 
    # child 3-6
    tempChildState[3], tempChildState[6] = tempChildState[6], tempChildState[3]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.append(newChild)
    tempChildState = currentNodeState 
    # child 4-7
    tempChildState[4], tempChildState[7] = tempChildState[7], tempChildState[4]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.append(newChild)
    tempChildState = currentNodeState
    # child 5-8
    tempChildState[5], tempChildState[8] = tempChildState[8], tempChildState[5]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.append(newChild)
    tempChildState = currentNodeState
    # child 6-7
    tempChildState[6], tempChildState[7] = tempChildState[7], tempChildState[6]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.append(newChild)
    tempChildState = currentNodeState
    # child 7-8
    tempChildState[7], tempChildState[8] = tempChildState[8], tempChildState[7]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.append(newChild)
    tempChildState = currentNodeState

    return allChildren

def getValidChildren(allChildren,closedList,openList):
    validChildren = []
    for child in allChildren:
        check = False
        for visitedC in closedList:
            if(child.state == visitedC.state):
                check = True
                break
        for visitedO in openList:
            if(child.state == visitedO.state):
                check = True
                break
        if(check == False):
            validChildren.append(child)
    return validChildren

def compareGoal(currentNode:Node):
    goal_state = [1,2,3,4,5,6,7,8,9]
    if(currentNode.state == goal_state):
        return True
    else: return False

def traceParent(solutionNode:Node,closedList):
    tempNode = solutionNode
    
    f = open("depthFirstSolution.txt", "w")
    currentParent = tempNode.parent
    currentState = tempNode.state
    f.write("Parent: \n")
    pcounter = 1
    for p in currentParent:
        if(pcounter % 3):
            f.write("\n")
        f.write(p)
        fcounter+=1
    f.write("State: \n")
    scounter = 1
    for s in currentState:
        if(scounter % 3):
            f.write("\n")
        f.write(s)
        scounter+=1
    f.close()

    while(tempNode.parent != [0,0,0,0,0,0,0,0,0]):
        for closedNodes in closedList:
            if(closedNodes.state == tempNode.state):
                tempNode = closedNodes
                f = open("depthFirstSolution.txt", "a")
                currentParent = tempNode.parent
                currentState = tempNode.state
                f.write("Parent: \n")
                pcounter = 1
                for p in currentParent:
                    if(pcounter % 3):
                        f.write("\n")
                    f.write(p)
                    fcounter+=1
                f.write("State: \n")
                scounter = 1
                for s in currentState:
                    if(scounter % 3):
                        f.write("\n")
                    f.write(s)
                    scounter+=1
                f.close()
                break
    

def depthFirstAlgorithm (initial_state:list):
    openList = []
    closedList = []
    
    while (openList.count != 0):
        openList.append(Node([0,0,0,0,0,0,0,0,0],initial_state))
        x = openList.pop()
        if(compareGoal(x)):
            solutionNode = x
            traceParent(solutionNode,closedList)
        else:
            allXChildren = getAllChildren(x)
            closedList.append(x)
            allValidXChildren = getValidChildren(allXChildren,closedList,openList)
            for validChild in allValidXChildren:
                openList.insert(0,validChild)
    
    f = open("depthFirstVisited.txt", "w")
    for currentnode in closedList:
        currentParent = currentnode.parent
        currentState = currentnode.state
        f.write("Parent: \n")
        pcounter = 1
        for p in currentParent:
            if(pcounter % 3):
                f.write("\n")
            f.write(p)
            fcounter+=1
        f.write("State: \n")
        scounter = 1
        for s in currentState:
            if(scounter % 3):
                f.write("\n")
            f.write(s)
            scounter+=1
    f.close()

    
depthFirstAlgorithm(initial_state)


