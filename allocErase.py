m = [0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1]
q = [[0, 2], [0, 1], [0, 3], [1, 2], [1, 1]]

# if queries[i][0] = 0 alloc, if equals 1 then erase
# queries [0, 2] aka alloc 2, where x = 2
# queries [1, 1] aka erase 1 where index = 1

def allocErase(memory, queries):
