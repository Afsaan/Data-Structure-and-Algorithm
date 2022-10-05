class Trees:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None


Root = Trees(50)
node1 = Trees(20)
node2 = Trees(25)
node3 = Trees(26)
node4 = Trees(37)
node5 = Trees(26)
node6 = Trees(37)

#coonecting the nodes

Root.left_node = node1
Root.right_node = node2

node1.left_node = node3
node1.right_node = node4

node2.left_node = node5
node2.right_node = node6


