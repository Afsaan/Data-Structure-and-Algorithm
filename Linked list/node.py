class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    # initialize the head to None
    def __init__(self):
        self.head = None

#insertion

    # to insert the first node
    def insert(self,NewNode):
        if self.head  == None:
            self.head = NewNode

    # to insert at the beg
    def push(self,Newnode):
        node = Newnode
        node.next = self.head
        self.head = node

    # insert anywhere in between the nodes
    def insert_after(self,pre_node,newNode):
        if pre_node == None:
            print("the node should be in linked list")
            return
        node = newNode
        node.next = pre_node.next
        pre_node.next = node
    # add at the end of the list
    def append(self,newnode):
        node = newnode
        temp = self.head
        while (temp.next):
            temp = temp.next     
        temp.next = node
        node.next = None

# deletion

    # del the given node with help of the values
    def keys(self,key):
        temp = self.head

        #if key is first node
        if temp != None:
            if (temp.data==key):
                self.head = temp.next
                temp = None
                return

        # if key is present at any other location
        while (temp is not None):
            if temp.data == key:
                break
            prev = temp  #saving the previous node
            temp = temp.next

        prev.next = temp.next

        temp =None

    # del the node bt position
    def position (self,position):
        temp = self.head
        if position == 0:
            self.head = temp.next
            temp.next = None

        for i in range (position -1):
            temp = temp.next
            if temp.next == None:
                return
        
        if temp == None:
            return

        if temp.next == None:
            return

        next = temp.next.next

        temp.next = None

        temp.next = next

# searching of element based on key
    def search(self,key):
        temp = self.head
        count=1

        while temp is not None:
            if temp.data == key:
                print(" {} is prsend at location {} ".format(key,count))
                return
            temp = temp.next
            count = count+1
            
            

        print("the given element is ot present in the list")
        


#printing of the Linked List
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
link.position(3)
link.keys(7)
link.print_node()
link.search(12)

