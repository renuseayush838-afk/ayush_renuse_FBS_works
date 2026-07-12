# find the sum of three digits numbers. 

num = int(input('enter a 3 digit number:'))

a = num % 10
num = num // 10

b = num % 10
num = num //10

c = num % 10
num = num // 10


sum = a + b + c

print(f'sum of three digits number {sum}')