numbers = [1, 2, 3, 4, 5]

def oddEven(nums):
    even = 0
    odd = 0

    for i in range(len(nums)):
        if i % 2 == 0:
            even += nums[i]
        else:
            odd += nums[i]

    if even < odd:
        return "odd"
    elif odd < even:
        return "even"
    else:
        return "equal"

print(oddEven(numbers))