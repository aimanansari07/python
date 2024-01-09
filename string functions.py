text1='AIMAN ANSARI'
text2='i am a python developer'
#string concatination
print(text1 + text2)
#length
print(len(text1))
#uppercase
print(text2.upper())
#lowercase
print(text1.lower())
#casefold(it also converts in lower)
print(text2.casefold())
#capitalized(Converts the first letter of string only if we put space in string it doesnt do)
print(text2.capitalize())
#title (it converts only first letter)
print(text2.title)
#----------Strip method------------
print("------------Strip method--------------")
text3='      Hello        '
print(text3.strip())
print(text3.lstrip())
print(text3.rstrip())
#--------removing specific elements from string---------
text4='qwepython is goodiop'
print(text4)
print(text4.lstrip('qwe'))
print(text4.rstrip('iop'),text4.lstrip('qwe'))

#---------------start with ,end with,and replace-----------------
print("---------------start with ,end with,and replace function-----------------")
text1='AIMAN ANSARI'
text2='i am a python developer'
print(text1.startswith('ai'))
print(text1.startswith('AI'))
print(text1.endswith('RI'))
print(text2)
print(text2.replace('python','java'))
#------------slice function---------
text1='AIMAN ANSARI'
print(text1[3:10:2])
#reverse of string
print(text1[::-1])
print(text1[:5])
print(text1[-3:-1])
#------------Count method------------
#The count() method returns the number of times a specified value appears in the string.
print(text2)

print(text2.count(''))
print(text2.count('e'))

#---------Find and index method---
'''The find() method finds the first occurrence of the specified value.

The find() method returns -1 if the value is not found.

The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)'''

text1='AIMAN ANSARI'
text2='i am a python developer'
print(text2.find('d'))
print(text2.find('z'))
#print(text2.index('z'))

#rfind,rindex
print("-----------Rfind,rindex-----------")
print('rfind ',text2.rfind('e'))
print('rindex',text2.rindex('e'))

#-------string split-----------
print("-------string split-----------")
text5="welcome ,to split ,function"
print(text5.split())
print(text5.split(','))
print(text5.split(',',1))
text6='Python- is -powerfull language'
print(text6.split('-',1))
text7='Python developement is good'
print(text7.split(" ",1))

#------------join method---------
print("------------join method---------")
fruits=('mango','banana','apple','graphes')
result="#@#@#".join(fruits)
print(result)
result=" * & @ ".join(fruits)
print(result)

#------------------string check methods(is wala)
print("------------string check methods(is wala)----------")
text8='1234567'
text9='Aiman12133'
text10='AIMAN'
text11='aiman'
print(text8.isdigit())
print(text10.isalpha())
print(text9.isalnum())
print(text10.isupper())
print(text11.islower())

#---------Swapecase(Make the lower case letters upper case and the upper case letters lower case:)
print("----------------swapecase method------")
print(text11.swapcase())
print(text1.swapcase())

