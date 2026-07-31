# write a program to calculate factorial of a number 

n = int(input('enter a number:'))
fac = 1
for i in range (1,n+1):
    fac = fac * i
print('factorial is :',fac)