# write a program to swap two variables without using third variables. 

a = int(input('enter first value:'))
b = int(input('enter second value:'))

a , b = b , a

print(f'after swapping {a}{b}')