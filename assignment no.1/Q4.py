# write a program to enter P T R and and calculate simple interest

p = float(input('enter principal:'))
t = float(input('enter time:'))
r = float(input('enter rate:'))

si = (p * t * r) / 100
print(f'simple interest is {si}')