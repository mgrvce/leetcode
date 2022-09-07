input = input("enter strings separated by space: ")
inputList = input.split()

def longestCommonPrefix(strs):
    if len(strs) == 0:
        return "" 

    prefix = ''
    minLen = min(len(x) for x in strs)
    i = 0


    for i in range(minLen):
        curr = strs[0][i]
        for j in range(len(strs)):
            if strs[j][i] != curr:
                return prefix
        prefix += curr

    return prefix
'''
    for i in range(len(strs)-1):
        curr = ''
        for j in range(min(len(strs[i]), len(strs[i+1]))):
            if strs[i][0] != strs[i+1][0]:
                prefix = ''
                return prefix
            elif strs[i][j] == strs[i+1][j]:
                curr += strs[i][j]
                prefix = curr
            else:
                break

    print("lcp: "+prefix)
    return prefix
    '''

longestCommonPrefix(inputList)
	
	
