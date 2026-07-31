# convert the time hh , min and sec into seconds .

hours = int(input('enter hours:'))
minute = int(input('enter minutes:'))
second = int(input('enter seconds:'))

total = hours * 3600 + minute * 60 + second
print(f'converted into seconds {total}')