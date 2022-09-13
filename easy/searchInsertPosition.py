testNums = [1, 3, 5, 6]

def searchInsert(nums, target):
    if target in nums:
        return nums.index(target)
    
    for i in range(len(nums)):
        if target < nums[i]:
            return i
    
    return len(nums)

print(searchInsert(testNums, 5))
print(searchInsert(testNums, 2))
print(searchInsert(testNums, 7))