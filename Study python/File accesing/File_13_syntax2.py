with open("Sample5.txt","r") as f:
    data = f.read()
    print(data)

with open("Sample5.txt","w") as f:
    f.write("I am new syntax after write.")
    f.close()