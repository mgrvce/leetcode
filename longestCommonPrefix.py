input = input("enter strings separated by space: ")
inputList = input.split()

def longestCommonPrefix(strs):
    prefix = ''
    if len(strs) == 1:
        return strs[0]

    for i in range(len(strs)-1):
        curr = ''
        for j in range(min(len(strs[i]), len(strs[i+1]))):
            if (strs[i][0] == strs[i+1][0] and strs[i][j] == strs[i+1][j]):
                curr += strs[i][j]
        prefix = curr

    print("lcp: "+prefix)
    return prefix

longestCommonPrefix(inputList)
	
	
