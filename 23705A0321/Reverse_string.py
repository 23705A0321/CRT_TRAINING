def reverse_string(input_string):
    stack = []
    for char in input_string:
        stack.append(char)   
    reversed_string = "" 
    while len(stack) > 0:
        reversed_string += stack.pop()  
    return reversed_string
original = input("Enter string = ")
#print("Original string:", original)
print("Reversed string:", reverse_string(original))