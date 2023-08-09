# Linked Linked list and all of its operations as well.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_front(self,data):
        if self.head:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = Node(data)
    
    def insert_back(self,data):
        temp = self.head
        if self.head:
            while(temp.next):
                temp = temp.next
        new_node = Node(data)
        temp.next = new_node
    
    def insert_after(self,prev_node,new_data):
        if prev_node is None:
            print("The given node must be in linked list")
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
    
    def delete_last_node(self):
        if self.head == None:
            return None
        if self.head.next == None:
            self.head = None
        second_last = self.head
        while(second_last.next.next):
            second_last = second_last.next
        second_last.next = None
    
    def delete_first_node(self):
        if self.head == None:
            return None
        if self.head.next == None:
            self.head = None
        self.head = self.head.next
    
    def delete_node_key(self, key):
        if self.head:
            temp = self.head
            while(temp.data != key):
                temp = temp.next
            temp.data = temp.next.data
            temp.next = temp.next.next

    def printll(self):
        if self.head:
            temp = self.head
            while(temp):
                print(temp.data)
                temp = temp.next

if __name__ == "__main__":
    lst = LinkedList()
    lst.head = Node(11)
    second = Node(12)
    third = Node(13)
    fourth = Node(14)
    lst.head.next = second
    second.next = third
    third.next = fourth
    lst.insert_front(100)
    lst.insert_front(200)
    lst.insert_front(300)
    lst.insert_back(900)
    lst.insert_back(800)
    lst.insert_after(third,99)
    lst.delete_last_node()
    lst.delete_first_node()
    lst.delete_first_node()
    lst.delete_node_key(99)
    lst.printll()
   

