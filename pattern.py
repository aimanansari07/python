#print pattren from 1 to 7
for i in range(1,7):
    for j in range(i):
        print(i,end=' ')
    print()

#print pattern by taking input from user
num=int(input("Enter number"))
for i in range(num):
    for j in range(i):
        print(i,end='')
    print()

#print in reverse
num=int(input("Enter number"))
for i in range(num,0,-1):
    for j in range(i):
        print(i,end='')
    print()