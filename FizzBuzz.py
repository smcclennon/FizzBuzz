# FizzBuzz generator
# smcclennon.github.io

turns = 100

# Rules:
# Multiple of 3: Fizz
# Multiple of 5: Buzz
# Multiple of both: FizzBuzz
# Neither: Keep counting

num = 1
while num <= turns:
    string = ''
    if num % 3 == 0:
        string += 'Fizz'
    if num % 5 == 0:
        string += 'Buzz'
    if string == '':
        string = num
    print(string)
    num+=1
input()