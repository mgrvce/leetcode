input = input("enter strings separated by space: ")
inputList = input.split()

def longestCommonPrefix(strs):
	prefix = []

	for i in range(len(strs)):
		for j in range(len(strs[i])):
			if (i < len(strs)-1 and strs[i][j] == strs[i+1][j]):
				prefix.append(strs[i][j])
				print(prefix)
	print(prefix)	

longestCommonPrefix(inputList)
	
	
