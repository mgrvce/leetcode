input = input("enter strings separated by space: ")
inputList = input.split()

def longestCommonPrefix(strs):
	prefix = []

	for i in range(len(strs)):
		for j in range(len(strs[i])):
			prefix.append(j)
		

longestCommonPrefix(inputList)
	
	
