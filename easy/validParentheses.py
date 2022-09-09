input = input("enter parentheses: ")

def isValidParentheses(s):
    stack = []
    braces = {')':'(', ']':'[','}':'{'}
    openings = set(braces.values())

    for p in s:
        if (p in openings):
            stack.append(p)
        else:
            if not stack:
                return False
            top = stack.pop()
            if top != braces[p]:
                return False

    return not stack

isValidParentheses(input)
