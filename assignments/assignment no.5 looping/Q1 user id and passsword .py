# 1. Write a program to prompt user to enter userid and password. 
# If Id and password is incorrect give him chance to re-enter the credentials.
# Let him try 3 times. After that program to terminate.

user_id = "admin"
password = "1234"

for i in range (3):
    userid = input('enter user id:')
    password = input('enter a password:')
    if userid == user_id and password == password:
        print('login successful')
    else :
        print('invalid user id and password')
else :
    print('3 attempts completed')