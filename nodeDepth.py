class NodeDepth:

    def __init__(self, parent, state, depth):
        self.parent = parent
        self.state = state
        self.depth = depth

    def print_node(self):
        print("parent: ", self.parent)
        print("state: ", self.state)
        print("depth: ", self.depth)
        print("\n")
