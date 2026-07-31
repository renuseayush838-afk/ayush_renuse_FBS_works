# write a program to find which number is divisible by 7 and multiple of 5 in given range

start = int(input('enter a starting number:'))
end = int(input('enter a ending number:'))

for i in range (start , end +1):
    if i % 7 == 0 and i % 5 == 0 :
        print(i)