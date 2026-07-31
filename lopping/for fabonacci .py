# write a program to print fabonacci number take nuber from user 

n = int(input(' how many fabonacci number you want to print:'))
a = -1
b = 1
for i in range(n):
    c = a + b
    print(c)
    a = b
    b = c