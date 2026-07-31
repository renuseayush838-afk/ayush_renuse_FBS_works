# write a program to print fibonacci number upto n numbers

num = int(input('enter a number:'))

a = 0
b = 1

for i in range (num):
    print(a)
    c = a + b
    a = b
    b = c 
