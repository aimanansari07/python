def outer():
    def inner():
        print("inner funtion")
    print("outer funtion")
    inner()
outer()