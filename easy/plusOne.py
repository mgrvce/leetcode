in1 = [1,2,3] 
in2 = [4,3,2,1]
in3 = [9]
in4 = [3,2,9]

def plusOne(digits):
    i = -1
    d = digits[i]
    if d == 9:
        while digits[i] == 9:
            digits[i] = 0
            print(i)
            if len(digits) == 1 or i == 0:
                digits.insert(0, 1)
            i -= 1
    else:
        digits[i] += 1

    return digits

    # if d == 9 and len(digits) == 1:
    #     digits[i] = 0
    #     digits.insert(0, 1)
    # elif d == 9 and len(digits) > 1:
    #     digits[-1] = 0
    #     i = -2
    #     while digits[i] == 9:
    #         digits[i] = 0
    #         i -= 1
    #     if i == 0:
    #         digits.insert(0, 1)
    # digits[i] += 1


print(plusOne(in1))
print(plusOne(in2))
print(plusOne(in3))
print(plusOne(in4))