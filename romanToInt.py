ins = input("enter roman numeral: ")

def romanToInt(s):
    romanNumerals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    conversion = 0
    i = 0

    while (i < len(s)):
        if (i != len(s)-1 and romanNumerals[s[i]] < romanNumerals[s[i+1]]):
            conversion += romanNumerals[s[i+1]] - romanNumerals[s[i]]
            i += 2
        else:
            conversion += romanNumerals[s[i]]
            i += 1
    return conversion

print(romanToInt(ins))
