# write a program to calculate selling price of book based on cost price and discount .  

cp = float(input('enter cost price:'))
discount = float(input('enter a discount:'))

sp = cp - (cp * discount / 100)

print(f'selling price of a book is {sp}')