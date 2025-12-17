def find_max_min(myList):
    if len(myList)==0:
        return None
    curr_min = myList[0]
    curr_max = myList[0]
    for i in myList[1:]:
        if i < curr_min:
            curr_min = i
        elif i > curr_max:
            curr_max = i
    return (curr_max,curr_min)
    
    


print( find_max_min([5, 3, 8, 1, 6, 9]) )


"""
    EXPECTED OUTPUT:
    ----------------
    (9, 1)
    
"""