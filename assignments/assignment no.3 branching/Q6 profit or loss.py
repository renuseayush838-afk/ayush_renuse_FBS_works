# write a program to calculate profit or loss. 

cp = float(input('enter a cost price:'))
sp = float(input('enter a selling price:'))

if sp > cp :
    print('profit')
elif cp > sp :
    print('loss')
else:
    print('no profit no loss')