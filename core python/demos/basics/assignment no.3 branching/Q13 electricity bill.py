# write a program to input electricity charges and calculate total electricity bill according to th given condition
# for first 50 units rupees 0.50 per unit
# for next 100 units rupees 0.75 per unit
# for next 100 units rupees 1.20 per unit
# for unit above 250 units rupees 1.50 per unit
# and additional subcharge 20% added to the bill

units = int(input('enter units :'))

if (units <= 50):
    bill = units * 0.50
elif (units <= 150):
    bill = 50 * 0.50 + (units - 50) * 0.75
elif (units <= 250):
    bill = 50 * 0.50 + 100 * 0.75 + (units - 150) * 1.20
else:
    bill = 50 * 0.50 + 100 * 0.75 + 100 * 1.20 + (units - 50) * 100 * 1.50

    bill = bill + bill * 0.20
    print('total electricity bill is :',bill)