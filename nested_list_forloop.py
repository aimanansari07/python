#accsessing nested list using for loop 
'''list=[[1,2,3,],[4,5,6,],[7,8,9]]
for i in list:
    for j in i:
        print(j,end=" ")'''
#using while loop
'''list=[[1,2,3,],[4,5,6,],[7,8,9]]
i=0
while i<len(list):
  j=0
  while j<len(list[i]):
    print(list[j])
    j=j+1
  i=i+1'''
print('---- Accessing List Using While Loop ----')
# Nested list
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Using a while loop to access elements in the nested list
i = 0
while i < len(nested_list):
    j = 0
    while j < len(nested_list[i]):
        print(f"Index [{i}] [{j}] :",nested_list[i][j], end=' ')
        j += 1
    print()  # Move to the next line for the next inner list
    i+= 1

print()