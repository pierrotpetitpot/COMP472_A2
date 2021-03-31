class Node:
    # Node used for the depth first algorithm and aStar algorithm

    def __init__(self, parent, state):
        self.parent = parent
        self.state = state

    def print_node(self):
        print("parent: ", self.parent)
        print("state: ", self.state)
        print("\n")
