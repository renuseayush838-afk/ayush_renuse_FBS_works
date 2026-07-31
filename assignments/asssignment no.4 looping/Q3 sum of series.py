# write a program to print sum of series up to n 

num = int(input('enter a number:'))

sum = 0

for i in range (1 , num+1):
    sum = sum + i
print('sum:',sum)