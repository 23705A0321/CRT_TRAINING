string = input()
newstring = ""
for i in range(len(string) -1):
    if string[i] != string[i + 1]:
        newstring = newstring + string[i]
print(newstring + string[-1])