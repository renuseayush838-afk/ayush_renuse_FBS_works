# write a program to swap two numbers using third variable .  

a = int(input('entre first number:'))
b = int(input('enter second number:'))

temp = a
a = b
b = temp

print(f'after swapping a{a} b{b}')