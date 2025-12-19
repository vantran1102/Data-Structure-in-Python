def rotate(nums,k):
    k = k%len(nums)
    nums[:]= nums[-k:]+nums[:-k]

# def reverse(nums,start,end):
#     while start < end:
#         nums[start],nums[end]= nums[end],nums[start]
#         start+=1
#         end-=1
        
# def rotate(nums,k):
#     n = len(nums)
#     if n == 0:
#         return
#     k = k%n
#     if k == 0:
#         return
#     reverse(nums,0,n-1)
#     reverse(nums,0,k-1)
#     reverse(nums,k,n-1)

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate(nums, k)
print("Rotated array:", nums)


"""
    EXPECTED OUTPUT:
    ----------------
    Rotated array: [5, 6, 7, 1, 2, 3, 4]

"""