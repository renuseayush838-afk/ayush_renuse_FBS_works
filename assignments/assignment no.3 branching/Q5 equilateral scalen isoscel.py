# write a program to cheack traingle is equilateral , isosceles or scalen traingle. 

a = int(input('enter first angle:'))
b = int(input('enter second angle:'))
c = int(input('enter third angle:'))

if a == b == c:
    print('equilateral traingel')
elif a == b or b == c or a == c:
    print('isosceles traingle')
else:
    print('scalen traingle')