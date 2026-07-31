# write a program to cheack if person is eligible to marry or not .  

gender = input('enter your gender male/female:')
age = int(input('enter your age:'))

if ('gender' == 'male' and age >= '21' , 'gender' == 'female' and age >= '18'):
    print('you are eligible for marriage.')
else:
    print('you are not eligible.')
