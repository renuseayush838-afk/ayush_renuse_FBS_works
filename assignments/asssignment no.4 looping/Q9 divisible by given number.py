# write a program to print all numbers in range divisible by a given number

start = int(input('enter a starting number:'))
end = int(input('enter a ending number:'))
n = int(input('enter a number:'))

for i in range ( start , end + 1) :
    if i % n == 0 :
        print(i)