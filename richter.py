mag=float(input("Enter Richter Magnitude Value "))
if mag>1.0 and mag<2.0:
    print("Microearthquakes not felt or rarely felt")
elif mag> 2.0 and mag< 4.0:
    print("Very rarely causes damage") 
elif mag> 4.0 and mag< 5.0:
    print("Damage done to weak building") 
elif mag> 5.0 and mag< 6.0:
    print("Cause damage to the poorly constructed building") 
elif mag> 6.0 and mag< 7.0:
    print("Causes damage to well-built structures") 
elif mag> 7.0 and mag< 8.0:
    print("Causes damage to most buildings")
elif mag> 8.0 and mag< 9.0:
    print("Causes major destruction")
else:
    print("Causes unbelievable damage")