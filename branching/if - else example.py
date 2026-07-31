num = int(input('enter number:'))
if (num > 0):
    if (num > 50):
        if (num > 100):
            if (num > 150):
                if (num > 250):
                    print('the number is greater than 250')
                else:
                    print('the number is between 150 - 250')
            else:
                print('the number is between 100 - 150')
        else:
            print('the number is between 50 - 100')
    else:
        print('the number is between 0 - 50')
else:
    print('the number is less than 0')
