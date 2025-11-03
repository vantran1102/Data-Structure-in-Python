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
    def is_Palindrome(self):
        if self.length <= 1:
            return True
        forward = self.head
        backward = self.tail
        for _ in range(self.length //2):
            if forward.value != backward.value:
                return False
            forward = forward.next
            backward = backward.prev
        return True
    
my_list = DoublyLinkedList(1)
my_list.append(1)
my_list.append(3)
my_list.append(1)
my_list.append(1)
print(my_list.is_Palindrome())
