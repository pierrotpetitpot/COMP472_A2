from node import Node
initial_state = [9,8,7,6,5,4,3,2,1]
node = Node([None],initial_state)
goal_state = [1,2,3,4,5,6,7,8,9]
allChildren = []

open = [initial_state]
closed = []

def getAllChildren(node:Node):
    currentNode = node.state
    tempChild = currentNode
    allChildren = []
    # child 0-1
    tempChild[0], tempChild[1] = tempChild[1], tempChild[0]
    allChildren.insert(tempChild)
    tempChild = currentNode 
    # child 1-2
    tempChild[1], tempChild[2] = tempChild[2], tempChild[1]
    allChildren.insert(tempChild)
    tempChild = currentNode 
    # child 0-3
    tempChild[0], tempChild[3] = tempChild[3], tempChild[0]
    allChildren.insert(tempChild)
    tempChild = currentNode 
    # child 1-4
    tempChild[1], tempChild[4] = tempChild[4], tempChild[1]
    allChildren.insert(tempChild)
    tempChild = currentNode 
    # child 2-5
    tempChild[2], tempChild[5] = tempChild[5], tempChild[2]
    allChildren.insert(tempChild)
    tempChild = currentNode 
    # child 3-4
    tempChild[3], tempChild[4] = tempChild[4], tempChild[3]
    allChildren.insert(tempChild)
    tempChild = currentNode 
    # child 4-5
    tempChild[4], tempChild[5] = tempChild[5], tempChild[4]
    allChildren.insert(tempChild)
    tempChild = currentNode 
    # child 3-6
    tempChild[3], tempChild[6] = tempChild[6], tempChild[3]
    allChildren.insert(tempChild)
    tempChild = currentNode 
    # child 4-7
    tempChild[4], tempChild[7] = tempChild[7], tempChild[4]
    allChildren.insert(tempChild)
    tempChild = currentNode 
    # child 5-8
    tempChild[5], tempChild[8] = tempChild[8], tempChild[5]
    allChildren.insert(tempChild)
    tempChild = currentNode 
    # child 6-7
    tempChild[6], tempChild[7] = tempChild[7], tempChild[6]
    allChildren.insert(tempChild)
    tempChild = currentNode 
    # child 7-8
    tempChild[7], tempChild[8] = tempChild[8], tempChild[7]
    allChildren.insert(tempChild)
    tempChild = currentNode

    return allChildren

def getValidChildren(allChildren,closed):
    validChildren = []
    for child in allChildren:
        check = False
        for visited in closed:
            if(child == visited):
                check = True
                break
        if(check == False):
            validChildren.insert(visited)
    return validChildren

def compareGoal(currentNode:Node,goal_state:list):
    if(currentNode.state == goal_state):
        return True
    else: return False