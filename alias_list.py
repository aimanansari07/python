
list=[1,2,3,4,5,"Aiman",7.7]
print("original list ",list)

alias=list

print("duplicate list ",alias)
alias.append(100)#it wil reflect on both list orignal and duplicate
print("original list ",list)

print("duplicate list ",alias)
