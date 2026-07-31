# write a program to prompt user to enter user id and password. after verifying user id and password display a 4 digit random number and ask user to enter the same. if user enters the same number then show him success message otherwise failed. 

import random
user = input('enter a username:')
pwd = input('enter a password:')

if user == 'admin' and pwd == '12345':
    captcha = random.randint(1000,9999)
    print(f'captcha={captcha}')
    user = int(input('enter the captcha:'))
    if user == captcha :
        print('user login successfully.')
    else:
        print('invalid captcha.')
else:
    print('invalid user')