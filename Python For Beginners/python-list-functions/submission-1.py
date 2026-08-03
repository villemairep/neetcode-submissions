from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    pass

    sumtrack = 0
    length = len(nums)
    for i in range(0,length):
        sumtrack = sumtrack + nums[i]

    return sumtrack

def get_min(nums: List[int]) -> int:
    pass

    mintrack = nums[0]
    length = len(nums)
    for i in range(0,length):
        if nums[i] < mintrack:
            mintrack = nums[i]

    return mintrack

def get_max(nums: List[int]) -> int:
    pass
    
    maxtrack = nums[0]
    length = len(nums)
    for i in range(0,length):
        if nums[i] > maxtrack:
            maxtrack = nums[i]

    return maxtrack

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
