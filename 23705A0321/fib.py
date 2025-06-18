def fib(number):
    if number <= 1:
        return number
    first = fib(number - 1)
    second = fib(number - 2)
    return first + second
print(fib(6))