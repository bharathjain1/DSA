class Node:
    def __init__(self, data):
        self.data = data
        self.left_child  =  None
        self.right_child  =  None
    
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
    
    def printree(self):
        if self.left_child:
            self.left_child.printree()
        print(self.data)
        if self.right_child:
            self.right_child.printree()
          
if __name__ == "__main__":
    root = Node(11)
    root.insert(9)
    root.insert(900)
    root.insert(8)
    root.insert(800)
    root.insert(799)
    root.insert(7)
    root.insert(3)
    root.insert(399)
    root.insert(2)
    root.insert(230)
    root.printree()
