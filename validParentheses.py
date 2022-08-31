input = input("enter parentheses: ")

def isValidParentheses(s):
	stack = []

	for p in s:
		if (p == '(' or p == '[' or p == '{'):
			stack.append(p)
		else:
			if stack:
				top = stack[-1]
				if (p == ')' and top == '(' or p == ']' and top == '[' or p == '}' and top == '{'):
					stack.pop()
	if (not stack):
		print("invalid parentheses")	
		print(stack)
	print("valid parentheses")
		

isValidParentheses(input)
