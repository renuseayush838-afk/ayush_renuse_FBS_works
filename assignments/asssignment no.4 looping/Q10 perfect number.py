# write a program to cheack given number is a perfect number 

num = int(input('enter a number:'))
sum = 0

for i in range (1 , num):
    if num % i == 0:
        sum = sum + i
if sum == num:
    print('perfect number')
else:
    ('not a perfect number')