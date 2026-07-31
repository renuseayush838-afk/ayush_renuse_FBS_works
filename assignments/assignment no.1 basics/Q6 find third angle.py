# write a program to input two angles from user and find third angle of the triangle. 

a = float(input('enter first angle:'))
b = float(input('enter second angle:'))

c = 180 - (a + b)

print(f'third angle of a traingle is{c}')