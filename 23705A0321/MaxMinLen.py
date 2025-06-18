def length(list):
    count = 0
    for i in list:
        count = count + 1
    return count
def minimum(list):
    mini = list[0]
    for index in range(1 , len(list)):
        if list[index] < mini:
            mini = list[index]
    return mini
def maximum(list):
    maxi = list[0]
    for index in range(1 , len(list)):
        if list[index] > maxi:
            maxi = list[index]
        return maxi
list1 = list(map(int , input().split()))
print(length(list1))
print(minimum(list1))
print(maximum(list1))