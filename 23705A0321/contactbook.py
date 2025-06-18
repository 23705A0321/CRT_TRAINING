contactbook = {}
for i in range(3):
    name = input("enter the name = ")
    phNo = int(input())
    contactbook[name] = phNo
searchname = input( "enter the name you need to search = ")
if searchname in contactbook:
    print(contactbook[searchname])
else:
    print("contact not found")