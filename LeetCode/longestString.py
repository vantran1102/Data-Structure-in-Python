def find_longest_string(myList):
    if len(myList)==0:
        return ''
    curr_longest=myList[0]
    curr_length=len(curr_longest)
    for i in myList[1:]:
        if len(i)>curr_length:
            curr_length=len(i)
            curr_longest=i
    return curr_longest


string_list = ['apple', 'banana', 'kiwi', 'pear']
longest = find_longest_string(string_list)
print(longest)  


"""
    EXPECTED OUTPUT:
    ----------------
    banana
    
"""