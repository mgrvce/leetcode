test1 = [1, 1, 2]
test2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

def removeDupes(nums):
    if not nums:
        return 0
    
    uniqueElems = []
    count = 0

    for i in range(len(nums)):
        if nums[i] not in uniqueElems:
            uniqueElems.append(nums[i])
            nums[i-count] = nums[i]
        else:
            count += 1


    print(nums)

    return len(uniqueElems)

'''
# brute force

def removeDupes(nums):
    if not nums:
        return 0

    seen = []

    for i in range(len(nums)):
        if nums[i] not in seen:
            seen.append(nums[i])

    for i in range(len(seen)):
        nums[i] = seen[i]

    print(nums)
    return len(seen)

'''

print(removeDupes(test1))
print(removeDupes(test2))
