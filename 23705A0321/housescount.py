houses = list(map(int , input().split()))
persons = int(input("enter the number of persons = "))
kgs = int(input("enter the number of kgs = "))
target = persons * kgs
count = 0
bagweight = 0
for i in range(len(houses)):
    bagweight = bagweight + houses[i]
    count = count + 1
    if bagweight >= target:
        print(count)
        break