from stack import Stack_List
def sorted_stack(stack_list):
    hold_stack = Stack_List()
    while not stack_list.is_empty():
        temp = stack_list.pop()
        while not hold_stack.is_empty() and hold_stack.peek() > temp:
            stack_list.push(hold_stack.pop())
        hold_stack.push(temp)
    while not hold_stack.is_empty():
        stack_list.push(hold_stack.pop())
    return stack_list
