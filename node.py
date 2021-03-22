class Node:

    def __init__(self, parent, shift, depth, state):
        self.parent = parent
        self.state = state

    def print_node(self):
        print("parent: ", self.parent)
        print("state: ", self.state)
        print("\n")
