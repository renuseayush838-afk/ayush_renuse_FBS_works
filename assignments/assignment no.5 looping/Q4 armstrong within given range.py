# 4. WAP to print Armstrong number within a given range

start = int(input('enter a starting number:'))
end = int(input('enter a ending number:'))

for num in range (start , end + 1):
    temp = num
    digits = len(str(num))
    total = 0

    while temp > 0 :
        digit = temp % 10
        total = total + digit ** digits
        temp = temp // 10
        if total == num:
            print(num)