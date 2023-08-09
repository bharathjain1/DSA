class Node:
    def __init__(self, data):
        self.data = data 
        self.right_child = None
        self.left_child = None
    
    def insert(self, data):
        if data < self.data:
            if self.left_child:
                self.left_child.insert(data)
            else:
                self.left_child = Node(data)
                return
        else:
            if self.right_child:
                self.right_child.insert(data)
            else:
                self.right_child = Node(data)
                return

    def printtree(self):
        if self.left_child:
            self.left_child.printtree()
        print(self.data)
        if self.right_child:
            self.right_child.printtree()

    def printpostorder(self):
        if self.left_child:
            self.left_child.printpostorder()
        if self.right_child:
            self.right_child.printpostorder()
        print(self.data)
    
    def printpreorder(self):
        print(self.data)
        if self.left_child:
            self.left_child.printpreorder()
        if self.right_child:
            self.right_child.printpreorder()
    
    def inorder(self):
        if self.left_child:
            self.left_child.inorder()
        print(self.data)
        if self.right_child:
            self.right_child.inorder()
        


if __name__ == "__main__":
    # node1 = Node(11)
    # node2 = Node(12)
    # node3 = Node(13)
    # node4 = Node(14)
    # node5 = Node(15)
    # node6 = Node(16)
    # node7 = Node(17)

    # node1.left_child = node2
    # node1.right_child = node3
    # node2.left_child = node4
    # node2.right_child = node5
    # node3.left_child = node6
    # node3.right_child = node7

    root = Node(27)
    root.insert(14)
    root.insert(35)
    root.insert(31)
    root.insert(10)
    root.insert(19)
    root.printpostorder()
    # root.printpreorder() 
    # root.inorder()
    # root.printtree()
    