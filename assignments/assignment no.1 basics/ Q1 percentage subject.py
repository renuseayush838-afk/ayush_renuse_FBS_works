s1 = int(input('entr sub1 marks:'))
s2 = int(input('entr sub2 marks:'))
s3 = int(input('entr sub3 marks:'))
s4 = int(input('entr sub4 marks:'))
s5 = int(input('entr sub5 marks:'))

total_marks = 500
all_marks = s1+s2+s3+s4+s5
percentage = (all_marks / total_marks) * 100

print(f'you got {percentage} %')