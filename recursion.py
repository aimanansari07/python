#recursion using global keyword
i=1
def hello():
    global i
    i=i+1
    print("Hello Aiman ",i)
    hello()
hello()