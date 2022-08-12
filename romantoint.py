s = input("enter roman numeral: ")

def romanToInt(r):
	romanNumerals = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
	conversion = 0
	i = 0

	while (i < len(r)):
		if (i != len(r)-1 and romanNumerals[r[i]] < romanNumerals[r[i+1]]):
			conversion += romanNumerals[r[i+1]] - romanNumerals[r[i]]
			i+=2
		else:
			conversion += romanNumerals[r[i]]
			i += 1
	return conversion
	


print(romanToInt(s))
