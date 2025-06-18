string = input("Enter string = ")
stack = []
for char in string:
    if len(stack) == 0:
        stack.append(char)
    elif char != stack[-1]:
        stack.append(char)
    elif char == stack[-1]:
        stack.pop()
print(stack)