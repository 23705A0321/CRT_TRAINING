def reverse(left , right , array):
    if left>=right:
        return array
    temp = array[left]
    array[left]=array[right]
    array[right]=temp
    left = left + 1
    right = right - 1
    return reverse(left , right , array)
array = [10 , 20 , 30 , 40 , 50]
left = 0
right = len(array) - 1
print(reverse(left , right , array))