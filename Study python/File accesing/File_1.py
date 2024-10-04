f = open("E:\shailesh.txt","r")         #if the file present in laptop tar rquired to copy 
data = f.read()                         #and full path of that file
print(data)
print(type(f))
print(type(data))
f.close()