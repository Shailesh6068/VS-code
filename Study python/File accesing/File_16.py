with open("practice.txt","r") as f:
    data = f.read()
    
New_data = data.replace("Python","Java")
print(New_data)

