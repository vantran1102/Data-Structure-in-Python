class Stack:
    def __init__(self):
        self.stack_list = []
    def push(self, value):
        self.stack_list.append(value)
    def print_list(self):
        for i in range(len(self.stack_list)-1, -1, -1):
            print(self.stack_list[i])
    def pop(self):
        if self.stack_list is None:
            return None
        else:
            self.stack_list.pop()
    def peek(self):
        if self.stack_list is None:
            return None
        else:
            return self.stack_list[-1]

my_list = Stack()
my_list.push(5)
my_list.push(6)
my_list.push(7)
my_list.push(8)
print("Print after push")
my_list.print_list()
my_list.pop()
print("Print after pop")
my_list.print_list()
my_list.peek()
print("Print after peek")
my_list.print_list()