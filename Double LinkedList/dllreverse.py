class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True
    
    def reverse(self):
        if not self.head or not self.head.next:
            return
        cur = self.head
        temp = None
        while cur:
            temp = cur.prev
            cur.prev = cur.next
            cur.next = temp
            cur = cur.prev
        temp = self.head
        self.head = self.tail
        self.tail = temp
        
    
my_list = DoublyLinkedList(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
print("Print list")
my_list.print_list()
print("Print reverse list")
my_list.reverse()
my_list.print_list()

