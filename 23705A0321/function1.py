def length(list):
    count = 0
    for i in list:
        count = count + 1
    return count
list = [10,20,30,40,50]
print("length of list = " , length(list))