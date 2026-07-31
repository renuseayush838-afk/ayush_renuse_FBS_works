# for loop

# for i in range(1,11):
# for i in range(2,21,2):
# for i in range (5,0,-1):
# for i in range (20,1,-2):

# num = int(input('enter a number:'))         # multiplication table
# for i in range(num , num*10+1 , num):

num = int(input('enter a number:'))
for i in range(num*10 , num-1 ,-num):
    print(i)