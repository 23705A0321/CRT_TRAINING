data_base = {}
for i in range (2):
    roll_no =int(input("Enter roll no = "))
    list=[]
    name = input("enter name = ")
    branch = input("enter branch = ")
    year = int(input("enter year = "))
    list.append(name)
    list.append(branch)
    list.append(year)
    data_base[roll_no] = list
print(data_base)
search_name = int(input("enter roll number = "))
if(search_name in data_base):
    print(data_base[search_name])
else:
    print("student not found")