input = input("enter strings separated by space: ")
inputList = input.split()

def longestCommonPrefix(strs):
    prefix = ''

    for i in range(len(strs)):
        for j in range(len(strs[i])):
            if (i < len(strs)-1 and strs[i][j] == strs[i+1][j]):
                print("i: "+str(i))
                print("j: "+str(j))
                curr = ''
                curr += strs[i][j]
                if curr not in prefix:
                    prefix += curr
                    print(prefix)

    print(prefix)

longestCommonPrefix(inputList)
	
	
