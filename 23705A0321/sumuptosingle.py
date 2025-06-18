number = int(input("Enter a Number = "))
sum = 0
while(number != 0):
    remainder = number % 10
    sum = sum + remainder
    number = number // 10
    if number == 0 and sum > 9:
        number = sum
        sum=0
    if number == 0 and sum < 10:
        print(sum)
        break