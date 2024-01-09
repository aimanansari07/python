#type conversion
#implicit
'''a=10
b="aiman"
c=10.45
print(a,b,c)
#explicit
x="10"
print(int(x))
print(type(x))
y=12.58
print(type(y))
z=int(y)
print(type(z))'''
#membership opt(in,not in)
'''l1=[1,2,3,4,5,"aiman"]
if "aiman"  in l1:#same for not in
    print("true")
else:
    print('false')
#identity opt(is ,isnot)
    
num=102
num1=10
print(num is num1)'''
#while loop
'''i=0
while(i<4):
    i+=1
    print(i)'''

'''i=0
while(i<5):
    
    print("inner loop ",i)
    i+=1
    j=1
    while(j<4):
        
        print("outer loop ",j)
        j+=1'''

#range function

'''for i in range(10,1,-1):
    print(i)'''

'''for i in range(2,8):
    print(i)
'''
#nested fro loop
'''for i in range(0,3):
    print('inner loop ',i)
    for J in range(1,3):
        print('outer loop ',J)'''

#string methods
'''str="hello,Aiman-Ansari"
print("Find method ",str.find("z"))
print("index method ",str.index("a"))
print("Count",str.count("a"))
print(str.split(","))
print(str.split("-"))
words=["Aiman","Ansari","develper"]
res="Hello".join(words)
res=" ".join(words)
print(res)'''
'''#list method

l=[1,2,3,4,5,6,7]
l.insert(0,0)
print(l)
l.pop(5)
print(l)
l.pop()
print(l)
print("index of 1 is ",l.index(1))
print("lenght of list is  ",len(l))
print(l)
print(l[5])
#creating list from userinput
num=int(input('Enter number of elments '))
l1=[]
for i in range(num):
    l1.append(input("Enter elements:"))
print("elements are ")
for j in (l1):
    print(j)'''

#aliases of list
og_list=[1,2,3,4,5,6]
alias=og_list
print("Alias list ",alias)
print("original list ",og_list)
alias.append(7)
print("alias",alias)
print('original list ',og_list)

#nested list
'''nes=[[1,2,3,4],[5,6,7],[8,9,0]]
for i in nes:
    for j in i:
        print(j)'''

#set
'''s={1,2,3,4,5,5,6,6,7,7}
s1=set()#for creating the empty set usig set constructor
print(s)
print(s1)
'''
#set operation
'''s1={1,2,3,4,5}
s2={4,5,6,7,8,9}
print('union operation',s1.union(s2))
print('intersaction ',s1.intersection(s2))
print('intersaction update ',s1.intersection_update(s2))
print('After intersaction update',s1)
print(s2)
s1.clear()
print(s1)
'''
#difference and difference update
'''s1={1,2,3,4,5}
s2={4,5,6,7,8,9}
print("Differnce",s1.difference(s2))
print("Differnce update",s1.difference_update(s2))
print(s1)'''
#symmetric difference( dono list me jo common elemnts hai usko chod ke sab elemnts ko combine krke deta hai)
'''s1={1,2,3,4,5}
s2={4,5,6,7,8,9}
print(s1.symmetric_difference(s2))
print(s1)
print(s2)
print(s1.symmetric_difference_update(s2))
print('---------After symmetric diff update-------')
print(s1)
print(s2)'''
#subset(if elemnts of set a presnt in set b then set a is subset )
'''a={1,2,3}
b={1,2,3,4,5,6,7}
print(a.issubset(b))'''
'''#superset(if set a contains the elemnts of setb and also conatins more elemnts then set a is super set)'''
'''a={1,2,3,4,5,6,7,8,9}
b={4,5,6,7,8}
print(a.issuperset(b))'''
#disjoint set(if there is no match in both sets then it called disjoint)
'''a={1,2,3,4}
b={5,6,7,8}
print(a.isdisjoint(b))
print()'''
#set methds
'''s={1,2,3,4,5,6,7,8,9}
s.add(9)
s.discard(0)
#s.remove(0) it generate error if the value is not present in the set
print(s)
s.pop()
print(s)
s.pop()
print(s)
s.update([1,2])
print(s)'''
#creating set using user input
'''num=int(input('Enter number of elemnts wants to enter '))
s=set()
for i in range(num):
    s.update(input('Enter elemnts '))
print("elemnts are ",s)'''


#Dictionary
'''d1=dict()
print(d1)'''#blank dict

'''d={"name":'Aiman',"age":22,"Gender":"male"}
print(d["name"])#access dictionary item using keys'''

#dict methods
# fromkeys() method returns a dictionary with the specified keys and the specified value.
'''dic={"Car":"Supraa","price":120000,"power":'7000hp'}
x=0
print(dic.fromkeys(dic,x))
print(dic)'''
#get() method returns the value of the item with the specified key.
dic={"Car":"Supraa","price":120000,"power":'7000hp'}
print(dic.get("Car"))
print(dic.get("color","Black"))#return value that not present in the dic
print(dic.get("color",0))
print(dic.items())
print("All keys ",dic.keys())
print("All Values ",dic.values())
dic.pop("power")
print("after pop ",dic)
print(dic.popitem())
'''The popitem() method removes and returns the last key-value pair
from the dictionary as a tuple'''
print(dic)
#The setdefault() method returns the value of the item with the specified key.
#If the key does not exist, insert the key, with the specified value,
dic1={"Car":"Supraa","price":120000,"power":'7000hp'}
print(dic1.setdefault("Car"))
print(dic1.setdefault("color","Black"))
#update() it will update dict with specific value
print("before update ",dic1)
print("---------After update--------- ")
dic1.update({"Color":"Whilte"})
print(dic1)
