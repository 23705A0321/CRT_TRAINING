database = {}
for i in range(3):
    rollno = int(input("enter roll number = "))
    list = []
    name = input("enter name = ")
    dept = input("enter dept = ")
    year = int(input("enter year = "))
    list.append(name)
    list.append(dept)
    list.append(year)
    database[rollno] = list
searchrollnumber = int(input("enter search roll number = "))
if searchrollnumber in database:
    print(database[searchrollnumber])
else:
    print("student not found")