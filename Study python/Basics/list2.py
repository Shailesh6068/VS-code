newlist = []
list = [12,16,20,24,28,32,36,40]
for i in list:
    if i > 25:
        newlist.append(i)

print(newlist)

#Nested list
list = [1,2,3,4,[5,6,7],8]
print(list[4])
print(list[4][1])
print(list[4][2])

#concanited two or more list
list = [1,2,3]
list1 = [4,5,6]
list2 = [7,8]
#list3 =[]
list3 = list+list1+list2
print(list3)