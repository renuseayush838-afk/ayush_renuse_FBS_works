# write a program to cheack given 3 digit number is pallindrome or not . 

num = int(input('enter a 3 digit number:'))

temp = num
rev = 0
while (num>0):
    d = num % 10
    num = num // 10
    rev = rev * 10 + d
if ( num == rev):
    print('it is a pallindrome number.')
else:
    print('not a pallindrome number.')