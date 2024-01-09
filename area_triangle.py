base=float(input('Enter base '))
height=float(input('Enter height '))
area=0
if base<=0 and height<=0:
    print("Enter valid base and height ")
else:
    area=(base*height)/2
    print("Area of triangle is ",area)
