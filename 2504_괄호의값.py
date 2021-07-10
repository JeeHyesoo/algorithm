def solution(s):
    stack = []
    for c in s:
        if c == ')':
            t = 0
            while stack:
                top = stack.pop()
                if top == '(':
                    stack.append(2 if t == 0 else t*2)
                    break
                elif top == '[':
                    return 0
                else:
                    t += top
        elif c == ']':
            t = 0
            while stack:
                top = stack.pop()
                if top == '[':
                    stack.append(3 if t == 0 else t*3)
                    break
                elif top == '(':
                    return 0
                else:
                    t += top
        else:
            stack.append(c)
        
    return stack

s = input()
stack = solution(s) 
if stack == 0:
    stack = []
print(0 if '(' in stack or '[' in stack else sum(stack))