# write a program to input angles of a traingle and cheack whether the traingle is valid or not. 

a = int(input('enter first angle:'))
b = int(input('enter second angle:'))
c = int(input('enter third angle:'))

if a + b + c == '180' :
    print('it is a valid traingle.')
else:
    print('it is a invalid traingle.')