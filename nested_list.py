nes=[1,2,['a','b','c'],3,"Aiman",['d','e','f']]
print(nes)
#accessing individual elements of list
print("element at index 0 is ",nes[0]) 
print("element at index 2 is ",nes[2]) 
#accssesing nested list 
print("Element at nested list ",nes[2][0])
print("Element at nested list ",nes[2][1])
print("Element at nested list ",nes[2][2])
print("Element at nested list ",nes[5][0])
print("Element at nested list ",nes[5])
print("Before modifying a list ",nes)
#mofidying a nested list
print('------------mofidying a nested list-------')
print("Before changing nested list elemnts ",nes[2])
nes[2][0]='x'
print("After changing nested list elments ",nes[2])
nes[2][1]='y'
print("AFter changing another elements ",nes[2])
nes[3]='ansari'
print(nes)
nes[5].append('g')
print(nes[5])
nes[5]=[9,8,7,6]
print(nes[5])