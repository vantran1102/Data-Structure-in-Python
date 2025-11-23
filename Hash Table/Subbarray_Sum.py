def subarray_sum(arr, target):
    """
    Finds all subarrays in the given array that sum up to the target_sum.

    Parameters:
    arr (list of int): The input array of integers.
    target_sum (int): The target sum for the subarrays.

    Returns:
    list of tuples: A list of tuples where each tuple contains the start and end indices of a subarray that sums to target_sum.
    """
#-------------Option 1-------------*/   
    # n = len(arr)
    # for start in range(n):
    #     current_sum = 0
    #     for end in range (start,n):
    #         current_sum += arr[end]
    #         if current_sum == target:
    #             return [start,end]
    # return []
#-------------Option 2-------------*/
    # sum_index = {0:-1}
    # current_sum = 0
    # for i, num in enumerate(arr):
    #     current_sum += num
    #     if current_sum - target in sum_index:
    #         return [sum_index[current_sum-target]+1,i]
    #     sum_index[current_sum] = i
    # return []
#-------------Option 3-------------*/
    if not arr:
        return []
    start = 0
    end = 0
    current_sum = arr[0]
    while start < len(arr) and end < len(arr):
        if current_sum == target:
            return [start,end]
        elif current_sum < target:
            end += 1
            if end == len(arr):
                break
            current_sum += arr[end]
        else:
            current_sum -= arr[start]
            start += 1
            if start > end and start < len(arr):
                end = start
                current_sum = arr[start]
    return []