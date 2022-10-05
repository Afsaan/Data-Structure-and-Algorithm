class Node:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None

    def print_tree(self):
        print(self.data)

root = Node(10)
root.PrintTree()