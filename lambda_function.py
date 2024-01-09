#addtion of two numbers using lambda
lam=lambda x,y:x+y
print("addtion of two  numbers is  ",lam(5,3))

#calculation using lambda
cal=lambda a,b:(a+b,a-b,a*b)
print("calculation is ",cal(10,5))

#storing every result in variable
calculate=lambda c,d:(c+d,c-d,c*d)
a,s,m=calculate(10,5)
print("Addtion is ",a)
print("Subtraction is",s)
print("Multiplicaton is ",m)

