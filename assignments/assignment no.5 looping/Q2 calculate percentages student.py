# 2. Enter number of students from user. 
# For those many students accept marks are subject marks from user and calculate percentage.
# Display all percentage and average percentage of students.

n = int(input('enter number of a students:'))
total_percentage = 0

for i in range (n):
    total = 0

    for j in range (5):
        marks = float(input('enter a marks:'))
        total = total + marks
        percentage = total / 5
        print('percentage:',percentage,'%')
        total_percentage = total_percentage + percentage
        average = total_percentage / n
        print('average percentage:',average,'%')