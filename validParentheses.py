input = input("enter parentheses: ")

def isValidParentheses(s):
	stack = []

	for p in s:
		if (p == '(' or p == '[' or p == '{'):
			stack.append(p)
		else:
			top = stack[-1]
			if (p == ')' and top == '(' or p == ']' and top == '[' or p == '}' and top == '{'):
				stack.pop()
				print("invalid parentheses")
		

isValidParentheses(input)
