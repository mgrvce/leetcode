in1 = "Hello World"
in2 = "   fly me   to   the moon  "
in3 = "luffy is still joyboy"

def lengthOfLastWord(s):
    s = s.strip().split(" ")

    return len(s[-1])



print(lengthOfLastWord(in1))
print(lengthOfLastWord(in2))
print(lengthOfLastWord(in3))
