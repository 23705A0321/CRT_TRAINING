n = int(input("Enter the total number of candies: "))
candies = [0, 0, 0] 
for i in range(n):
    person = i % 3
    candies[person] += 1
print("Candies distributed to the first person:", candies[0])