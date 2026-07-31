# input 5 subject marks from user and display grade. 

s1 = int(input('enter sub 1 marks:'))
s2 = int(input('enter sub 2 marks:'))
s3 = int(input('enter sub 3 marks:'))
s4 = int(input('enter sub 4 marks:'))
s5 = int(input('enter sub 5 marks:'))

total_marks = s1+s2+s3+s4+s5
per = total_marks/5
print(per)

if (per >= 60):
    print('you are pass with first class.')
elif(per >= 50):
    print('you are pass with second class.')
elif(per >= 35):
    print('you are pass.')
else:
    print('you are fail.')