def singleNumber(self, nums: List[int]) -> int:
    seen = {}
    for num in nums:
        if num in seen:
            seen[num]+=1
        else:
            seen[num]=1
    count=0
    for key,value in seen.items():
        if value==1:
            count=key
    return count