f=open("new.txt","r")
r=f.read()
print(r)
f.close()

f=open("new.txt","w")
write=f.write("python program")
f.close()

f=open("new.txt")
read=f.read()
#print(read)

with open("new.txt","a") as n:#other method to write a data into a file it doesnt required to close
    n.write("\ntext using with open method ")

#print(read)

print(read)