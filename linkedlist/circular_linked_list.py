class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_node_at_beg(self,data):
        if self.head:
            new_node = Node(data)
            self.head = new_node
            self.head.next = self.head


    def printcll(self):
        count = 0
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
            if temp == self.head:
                count = count + 1
                if count > 1:
                    break

if __name__ == "__main__":
    lst = LinkedList()
    lst.head = Node(11)
    second  = Node(12)
    third = Node(13)
    lst.head.next = second
    second.next = third
    third.next = lst.head
    lst.insert_node_at_beg(223)
    lst.printcll()