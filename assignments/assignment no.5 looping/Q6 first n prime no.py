# write a program to print first n prime numbers. 

start = int(input('enter a starting number:'))
end = int(input('enter a ending number:'))

for num in range ( start , end + 1):
    count = 0
    for i in range(1 , num + 1):
        if num % i == 0:
            count = count + 1
    if count == 2:
        print(num)