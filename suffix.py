str=input("Enter String: ")
suffix=input("Enter Suffix: ")
if(str.endswith(suffix)):
    print("True")
elif(suffix>str):
    print("false")