ex1 = 121
ex2 = -121
ex3 = 10

def isPalindrome(x):
    num = str(x)
    reversed = num[::-1]
    # print(num)
    # print(reversed)

    return num == reversed

print(isPalindrome(ex1))
print(isPalindrome(ex2))
print(isPalindrome(ex3))