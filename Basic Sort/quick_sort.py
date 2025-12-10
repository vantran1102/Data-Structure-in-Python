def swap(list,index1,index2):
    temp = list[index1]
    list[index1]=list[index2]
    list[index2]=temp
def pivot(list, pivot, end):
    swap_index = pivot
    for i in range(pivot+1,end+1):
        if list[i]<list[pivot]:
            swap_index+=1
            swap(list,swap_index,i)
    swap(list,pivot,swap_index)
    return swap_index
def quick_sort(list):
    quick_sort_helper(list,0,len(list)-1)
    return list

def quick_sort_helper(list,left,right):
    if left<right:
        pivot_index = pivot(list,left,right)
        quick_sort_helper(list,left,pivot_index-1)
        quick_sort_helper(list,pivot_index+1,right)
    return list

my_list = [38,27,43,3,9,82,10]
print("unsorted list:", my_list)
sorted_list = quick_sort(my_list)
print("sorted list:", sorted_list)
