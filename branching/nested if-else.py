gender = input('enter gender (male/female)')
age = int(input('enter age:'))

if(gender == 'female'):
    if(age >= 18):
        print('girl is eligible.')
    else:
        print('girl is not eligible.')
else:
    if(age>=21):
        print('boy is eligible.')
    else:
        print('boy is not eligible.')