test1 = [3, 2, 2, 3]
test2 = [0, 1, 2, 2, 3, 0, 4, 2]

def removeElem(nums, val):
    count = 0
    remaining = 0

    for i in range(len(nums)):
        if nums[i] == val:
            count += 1
        else:
            nums[i-count] = nums[i]
            remaining += 1
    
    print(nums)
    return remaining

print(removeElem(test1, 3))
print(removeElem(test2, 2))