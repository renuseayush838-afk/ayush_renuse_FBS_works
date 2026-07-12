# write a program to convert days into yeras , weeks and days. 

days = int(input('enter days:'))

years = days // 360
days = days % 360
weeks = days // 7
days = days % 7

print(f'years{years} weeks{weeks} days{days}')