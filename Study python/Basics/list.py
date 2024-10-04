list = ["kiwi"]
print(type(list))

list = [1,2,3,4,5,6,"Mango","Kiwi"]

#for add element at end use " append()"
list.append("Apple")    # it only accepts one argument at a time.
list.append(1)
print(list)                          

#For insert element at position
list.insert(2,65)
print(list)

#For extend element at position
list.extend([5,6,7])
print(list)

#method 2
list = [1,2,3,4]
list2 = [5,6]
list.extend(list2)
print(list)

list = ["Shailesh"]
print(list)