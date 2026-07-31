#  Accept age of five people and also per person ticket amount and then calculate total amount to ticket to travel for all of them based on following condition:
# Children below 12 = 30% discount
# Senior citizen (above 59) = 50% discount
# others need to pay full.

age = int(input('enter age of person 1:'))
amt1 = float(input('enter ticket amount 1:'))
age = int(input('enter age of person 2:'))
amt2 = float(input('enter ticket amount 2:'))
age = int(input('enter age of person 3:'))
amt3 = float(input('enter ticket amount 3:'))
age = int(input('enter age of person 4:'))
amt4 = float(input('enter ticket amount 4:'))
age = int(input('enter age of person 5:'))
amt5 = float(input('enter ticket amount 5:'))

total = amt1+amt2+amt3+amt4+amt5

if ( age < 12):
    total = total - total * 0.30
elif( age >= 59):
    total = total - total * 0.50
    print(f'total amount {total}')
else:
    print(f'total')
