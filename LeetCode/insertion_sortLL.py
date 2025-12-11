class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
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
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insertion_sort(self):
        if self.length < 2 or self.head is None:
            return 
        sorted_head = self.head
        sorted_tail = sorted_head
        cur = sorted_head.next
        sorted_tail.next = None
        while cur is not None:
            next_node = cur.next
            if cur.value <= sorted_head.value:#insert beginning
                cur.next = sorted_head
                sorted_head = cur
            else:
                prev = sorted_head
                node = sorted_head.next
                while node is not None and node.value < cur.value:
                    prev = node
                    node = node.next
                #insert between
                prev.next = cur
                cur.next = node
                if node is None:
                    sorted_tail = cur
            cur = next_node
        self.head = sorted_head
        self.tail = sorted_tail
            
                    
                
            
                
                
                
                

            



my_linked_list = LinkedList(4)
my_linked_list.append(2)
my_linked_list.append(6)
my_linked_list.append(5)
my_linked_list.append(1)
my_linked_list.append(3)

print("Linked List Before Sort:")
my_linked_list.print_list()

my_linked_list.insertion_sort()

print("\nSorted Linked List:")
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Linked List Before Sort:
    4
    2
    6
    5
    1
    3

    Sorted Linked List:
    1
    2
    3
    4
    5
    6

"""

