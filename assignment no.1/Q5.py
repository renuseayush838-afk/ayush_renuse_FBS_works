# write a program to enter P T R and calculate compound intrest.

p = float(input('enter principal:'))
t = float(input('enter time'))
r = float(input('enter rate'))

amount = p * (1 + r / 100) ** t
ci = amount - p

print(f'compound interest is{ci}')