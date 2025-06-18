rows = int(input("enter number of rows = "))
spaces = rows - 1

# Upper half
for row in range(1 , rows + 1):
    for space in range(1 , spaces + 1):
        print(" ", end = "")
    for star in range(1, row + 1):
        print("*", end = " ")
    spaces = spaces - 1
    print()

# Lower half
spaces = 1
for row in range(rows - 1, 0, -1):
    for space in range(1 , spaces + 1):
        print(" ", end = "")
    for star in range(1, row + 1):
        print("*", end = " ")
    spaces = spaces + 1
    print()