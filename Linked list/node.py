class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def insert(self,NewNode):
        if self.head  == None:
            self.head = NewNode
    def push(self,Newnode):
        node = Newnode
        node.next = self.head
        self.head = node

    def insert_after(self,pre_node,newNode):
        if pre_node == None:
            print("the node should be in linked list")
            return
        node = newNode
        node.next = pre_node.next
        pre_node.next = node

    def append(self,newnode):
        node = newnode
        temp = self.head
        while (temp.next):
            temp = temp.next     
        temp.next = node
        node.next = None

# deletion

    def del_front(self,delNode):
        temp = self.head
        self.head = temp.next

    def betweeen(self,delNode):
        # if delNode.next == None:
        pass
            
        
     def end(self,delnode):
         pass
        

#printing of the node
    def print_node(self):
       temp = self.head
       while (temp):
           print(temp.data)
           temp = temp.next

node1 = Node(4)
node2 = Node(5)
node3 = Node(7)
node4 = Node(10)
node8 = Node(8)
node5 = Node(11)
node6 = Node(12)
link = Linkedlist()
link.insert(node1)
link.push(node2)
link.push(node3)
link.insert_after(node2,node4)
link.insert_after(node2,node8)
link.append(node5)
link.append(node6)
link.del_front(node1)
link.print_node()
