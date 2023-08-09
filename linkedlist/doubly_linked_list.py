class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        new_node.prev = None
        
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node


    def printddl(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

if __name__ == "__main__":
    dd = DoublyLinkedList()
    # dd.head = Node(11)
    # n2 = Node(13)
    # dd.head.prev = None
    # dd.head.next = n2
    # n2.prev = dd.head
    # n3 = Node(154)
    # n3.prev = n2
    # n2.next = n3
    dd.push(89)
    dd.push(890)
    dd.printddl()