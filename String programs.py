#1.Write a Python program that prints the length of a string s.
str=input('Enter String ')
a=len(str)
print('lenght of string is ',a)

'''2.Write a Python program that prints the character at index i in the string s.

If the index is out of range, the program should print "i is out of range"

If the string is empty, the program should print "Empty String"'''

str=input(' enter string ')
i=int(input(" enter index "))
if(len(str)==0):
    print('Empty string')
    
elif(i>len(str)):
    print("out of index")
else:
    print('character at index',i ,'is',str[i])
        

'''3.Write a Python program that prints the first and last three characters of the string s as a single string.

If the string has less than six characters, print an empty string (blank output)'''

str=input('Enter String ')
if(len(str)<6):
    print("")
else:
    start=str[:3]
    print('start 3 character is ',start)
    end=str[-3:]
    print('end 3 character is ',end)
    
'''4.Write a Python Program that prints the reversed version of a string.

The program must preserve uppercase and lowercase letters.

If the string is empty, print it intact.'''

str=input("Enter string ")
if(len(str)==0):
    print("empty string")
else:
 print('reverse version of string is ',str[::-1])  
 
'''5.Write a Python program that prints the string s without the characters located at even indices.

If the string is empty or only has one character, print it intact'''

str=input("enter string  ")
if(len(str)==-1 and len(str)==0):
    print()
else:
    print(str[1::2])

#If the string is empty or only has one character, print it intact using for loop'''

str=input("enter string  ")
len=len(str)
for i in range(1,len,2):
  print(str[i],end=' ')

    
    
