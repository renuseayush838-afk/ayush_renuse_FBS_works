# write a program to cheack if user has enterd correct userid and password. 

user = input('enter a username:')
pwd = input('enter a password:')

if user == 'admin' and pwd == '12345':
    print('login successfully')
else:
    print('invalid username or password')