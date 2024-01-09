nes_tup=((1,2,3),(4,5,6),(7,8,9))
for i in nes_tup:
    for j in i:
        print(j)

'---- Accessing Nested tuple with different element in the tuple ----- '
tup=(1,2,3,(4,5,6),'aiman',16.7)
for i in range(len(tup)):
    if type(tup[i]) is tuple:
        if (len(tup[i])>1):
            l=len(tup[i])
            for j in range(l):
                print(tup[i][j])
    else:
        print(tup[i])
print()