class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    
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
    
    def search(self, element):
        if element == self.data:
            return f" Element found {element} "
        elif element < self.data:
            if self.left_child:
                return self.left_child.search(element)
            else:
                return "value not found"
        else:
            if self.right_child:
                return self.right_child.search(element)
            else:
                return "value not found"
        
    
    def printree(self):
        if self.left_child:
            self.left_child.printree()
        print(self.data)
        if self.right_child:
            self.right_child.printree()
            
if __name__ == "__main__":
    root = Node(11)
    root.insert(100)
    root.insert(101)
    root.insert(102)
    root.insert(103)
    root.insert(1)
    root.insert(2)
    root.insert(3)
    root.insert(4)
    root.insert(3)
    # print(root.search(1031))
    root.printree()

