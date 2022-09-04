input = input("enter parentheses: ")

def isValidParentheses(s):
	stack = []
	braces = {')':'(', ']':'[','}':'{'}

	for p in s:
		if (p == '(' or p == '[' or p == '{'):
			stack.append(p)
		else:
			if not stack:
				#print("invalid")
				return False
			if stack:
				top = stack[-1]
				if top == braces[p]:
					stack.pop()
				else:
					#print("invalid")
					return False
				
	if (not stack):
		#print("valid")
		return True
		

isValidParentheses(input)
