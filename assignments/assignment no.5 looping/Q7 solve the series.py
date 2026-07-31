# 7. Write a program to solve the following series
# a. 1! + 2! + 3! +4! +... n!

n = int(input('enter number:'))

fact = 1
sum = 0

for i in range (1 , n + 1):
    fact = fact * i
    sum = sum + fact
print('sum=',sum)

# b. N+N^2+N^3+N^4+N^N (here means exponent)

n = int(input('enter a number:'))

sum = 0

for i in range(1 , n+1):
    sum = sum + n ** i
print('sum =',sum)

# c. Find the sum of a geometric series from 1 to n where the common ratio is 2.

n = int(input('enter a number:'))

term = 1
sum = 0

for i in range(n):
    sum = sum + term
    term = term * 2
print('sum =',sum)

# d. a+a2/2+a3/3+...+a10/10

a = int(input('enter a :'))
sum = 0

for i in range(1,11):
    sum = sum + (a ** i)/i
print('sum = ',sum)