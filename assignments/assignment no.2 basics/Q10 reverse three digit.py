# write a program to reverse three digits numbers. 

num = int(input('enter a 3 digits number:'))

rev = (num % 10) * 100 + ((num // 10 % 10) * 10 + (num // 100))

print(f'reverse number{rev}')