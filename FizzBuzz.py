# FizzBuzz generator
# smcclennon.github.io

turns = 100

for num in range(1, turns + 1):
    string = ''
    if num % 3 == 0:
        string += 'Fizz'
    if num % 5 == 0:
        string += 'Buzz'
    if not string:
        string = num
    print(string)
input()