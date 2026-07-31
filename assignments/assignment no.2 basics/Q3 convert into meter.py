# convert distance given in feet and inches into meter and centimeter. 

feet = float(input('enter feet:'))
inches = float(input('enter inches:'))

total_inches = feet * 12 + inches
m = total_inches * 0.0254
cm = total_inches * 2.54

print(f'meter{m}centimeter{cm}')