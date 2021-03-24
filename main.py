from node import Node
initial_state = [9,8,7,6,5,4,3,2,1]
node = Node([None],initial_state)
allChildren = []


def getAllChildren(node:Node):
    currentNodeState = node.state
    tempChildState = currentNodeState
    allChildren = []
    # child 0-1
    tempChildState[0], tempChildState[1] = tempChildState[1], tempChildState[0]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.insert(newChild)
    tempChildState = currentNodeState
    # child 1-2
    tempChildState[1], tempChildState[2] = tempChildState[2], tempChildState[1]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.insert(newChild)
    tempChildState = currentNodeState
    # child 0-3
    tempChildState[0], tempChildState[3] = tempChildState[3], tempChildState[0]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.insert(newChild)
    tempChildState = currentNodeState
    # child 1-4
    tempChildState[1], tempChildState[4] = tempChildState[4], tempChildState[1]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.insert(newChild)
    tempChildState = currentNodeState
    # child 2-5
    tempChildState[2], tempChildState[5] = tempChildState[5], tempChildState[2]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.insert(newChild)
    tempChildState = currentNodeState
    # child 3-4
    tempChildState[3], tempChildState[4] = tempChildState[4], tempChildState[3]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.insert(newChild)
    tempChildState = currentNodeState
    # child 4-5
    tempChildState[4], tempChildState[5] = tempChildState[5], tempChildState[4]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.insert(newChild)
    tempChildState = currentNodeState 
    # child 3-6
    tempChildState[3], tempChildState[6] = tempChildState[6], tempChildState[3]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.insert(newChild)
    tempChildState = currentNodeState 
    # child 4-7
    tempChildState[4], tempChildState[7] = tempChildState[7], tempChildState[4]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.insert(newChild)
    tempChildState = currentNodeState
    # child 5-8
    tempChildState[5], tempChildState[8] = tempChildState[8], tempChildState[5]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.insert(newChild)
    tempChildState = currentNodeState
    # child 6-7
    tempChildState[6], tempChildState[7] = tempChildState[7], tempChildState[6]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.insert(newChild)
    tempChildState = currentNodeState
    # child 7-8
    tempChildState[7], tempChildState[8] = tempChildState[8], tempChildState[7]
    newChild = Node(currentNodeState,tempChildState)
    allChildren.insert(newChild)
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
            validChildren.insert(child)
    return validChildren

def compareGoal(currentNode:Node):
    goal_state = [1,2,3,4,5,6,7,8,9]
    if(currentNode.state == goal_state):
        return True
    else: return False

def depthFirstAlgorithm (initial_state:list):
    initialNode = Node([None],initial_state)
    openList = [initialNode]
    closedList = []
    solutionNode = Node([],[])
    while (openList.count != 0):
        x = openList.pop()
        if(compareGoal(x)):
            solutionNode.parent = x.parent
            solutionNode.state = x.state
        else:
            allXChildren = getAllChildren(x)
            closedList.append(x)
            allValidXChildren = getValidChildren(allXChildren,closedList,openList)
            for validChild in allValidXChildren:
                openList.append(validChild)
    
    return Node([None],[None])



