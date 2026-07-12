# program to find roots of a quadratic equation. 

a = float(input('enter a:'))
b = float(input('enter b:'))
c = float(input('enter c:'))
d = b ** 2 - 4 * a * c

r1 = (-b + (d ** 0.5)) / (2 * a)
r2 = (-b - (d ** 0.5)) / (2 * a)

print(f'root1{r1}root2{r2}')
