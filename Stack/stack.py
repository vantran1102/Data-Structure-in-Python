class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp:
            print(temp.value)
            temp = temp.next

    def push(self,value):
        new_node = Node(value)
        if self.height == 0:
            new_node.next = self.top
        else:
            new_node.next = self.top
            self.top = new_node
        self.height +=1
    
    def pop(self):
        temp = self.top
        if self.height == 0:
            return None
        else:
            self.top = self.top.next
            temp.next = None
        self.height -= 1
        return temp
class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.height = 1
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def enqueue(self,value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.height += 1
        return True
    def dequeue(self):
        temp = self.first
        
        if self.height == 0:
            return None
        if self.height == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.height -= 1
        return temp


my_string = "hello"
char_array = list(my_string)
myString = Stack(char_array)
print(char_array)
myString.print_stack()

mystack = Stack(3)
mystack.print_stack()
mystack.push(4)
mystack.push(5)
print("Print After Push")
mystack.print_stack()
mystack.pop()
print("Print After Pop")
mystack.print_stack()

myqueue = Queue(23)
print("Print Queue")
myqueue.print_queue()
myqueue.enqueue(24)
myqueue.enqueue(25)
print("Print Queue after Enqueue")
myqueue.print_queue()
myqueue.dequeue()
print("Print Queue after Dequeue")
myqueue.print_queue()

