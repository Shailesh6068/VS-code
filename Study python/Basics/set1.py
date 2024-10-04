#Unordered          : Pratyek print la vegalya order ne print hote
set = {"Raj","Yash","Ram","piyus"}
print(set)

#Accesing the Items
for i in set:
    print(i)

#check item in set
if "Raj" in set:
    print("Raj in Set.")

#add element in set
set.add("Ganesh")
print(set)

#add another sequence in set
list = ["Om","Vikram","Abhay"]         #also use tupple
set.update(list)
print(set)       

#add set
set = {"Raj","Ram","Ban"}
set1 = {"Man","Girl","Boy"}
set.update(set1)
print(set)

#Duplicate not allowed
set={1,1,2,3,5,2,5,2,5,25,25,2,5}
print(set)
