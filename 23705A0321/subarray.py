array = list(map(int , input().split()))
subarray = []
for left in range(len(array)):
    for right in range(left , len(array)):
        subarray.append(array[right])
        print(subarray)
    subarray = []