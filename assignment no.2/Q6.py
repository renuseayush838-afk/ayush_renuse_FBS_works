# write prgram to calculate total salary of a employee based on basic da = 10% basic, ta = 12% basic, hra = 15% of basic . 

basic = float(input('enter basic salary:'))

da = basic * 0.10
hra = basic * 0.15
ta = basic * 0.12

total = basic + da + hra + ta

print(f'total salary of a employee is {total}')