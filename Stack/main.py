from stack import Stack_List
from sort_stack import sorted_stack


my_stack = Stack_List()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)
print("Print Before Sort Stack")
my_stack.print_stack()
sorted_stack(my_stack)
print("Print After Sorted Stack")
my_stack.print_stack()

