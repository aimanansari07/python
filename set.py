#declare set using set constructor
s=set([1,2,3,4,"aiman"])
print(type(s))
print(s)
#declare using {}
s1={1,2,3,4,5,6,"aiman"}
print(type(s1))
print(s1)
#uniqness of set
s3={11,1,2,2,3,3,4,4,5,5,6}
print(s3)
#empty set
s4=set()
print(s4)
s5={}
print(type(s5))
#accessing using for loop
s3={11,1,2,2,3,3,4,4,5,5,6}
for i in s3:
    print(i)