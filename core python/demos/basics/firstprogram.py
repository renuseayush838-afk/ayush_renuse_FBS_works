sub1 = int(input("Enter subject 1 marks: "))
sub2 = int(input("Enter subject 2 marks: "))
sub3 = int(input("Enter subject 3 marks: "))
sub4 = int(input("Enter subject 4 marks: "))
sub5 = int(input("Enter subject 5 marks: "))

total_marks = 500
all_marks = sub1 + sub2 + sub3 + sub4 + sub5
percentage = (all_marks / total_marks) * 100

print(percentage)