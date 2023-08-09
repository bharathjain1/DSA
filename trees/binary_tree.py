'''
Binary search tree(BST)
-->  BST INSERT
-->  BST DELETE
-->  BST SEARCH
'''
class BST:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
    
    def insert(self,val):
        if val < self.data:
            if self.left_child:
                self.left_child.insert(val)
            else:
                self.left_child = BST(val)
                return
        else:
            if self.right_child:
                self.right_child.insert(val)
            else:
                self.right_child = BST(val)
                return
            
    def search(self,key):
        if key == self.data:
            return f" element found {key} "
        elif key < self.data:
            if self.left_child:
                return self.left_child.search(key)
            else:
                return "value not found "
        else:
            if self.right_child:
                return self.right_child.search(key)
            else:
                return "value not found " 
    
    def delete_node(self,key):
        if root is None:
            return root
        
        if key < self.data:
            self.left_child = self.left_child.delete_node(key)
            return self.data

        elif key >= self.data:
            self.right_child = self.right_child.delete_node(key)
            return self.data
        
        if self.left_child is None:
            temp = self.right_child
            del self.data
            return temp
        
        elif self.right_child is None:
            temp = self.left_child
            del self.data
            return temp
        
        else:
            succParent = self.data
            succ = self.right_child
            while self.left_child is not None:
                succParent = succ
                succ = succ.left_child
            
            if succParent != self.data:
                succParent.left_child = succ.right_child
            else:
                succParent.right_child = succ.right_child
            
            del succ
            return self.data




    def printree(self):
        if self.left_child:
            self.left_child.printree()
        print(self.data,end=" ")
        if self.right_child:
            self.right_child.printree()

if __name__ == "__main__":
    root = BST(11)
    n = int(input(" Enter the number of elements "))
    for i in range(n):
        k = int(input())
        root.insert(k)
    root.printree()
