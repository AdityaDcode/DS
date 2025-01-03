f =open("file.txt")
data =f.read()
print(data)
f.close()

f=open("file.txt","w")
f.write(data)
f.close()