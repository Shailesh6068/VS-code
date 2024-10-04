#For Remove Element From list
#method 1
list = [1,2,3,4,5]
list.remove(5)
print(list)
 
#method 2 : Remove item from index
list = [1,2,3,4,5]
list.pop(0) 
print(list) 

#CHANGING ITEM FROM LIST
list = [1,2,3,4,5]
list[0] = 0
print(list)

#IN RANGE
list = [1,2,3,4,5]
list[1:4] = [7,8,9]       #[1,4)
print(list)               #[1, 7, 8, 9, 5]

list = [1,2,3,4,5]
list[1:4] = [7,8,9,10,12]
print(list)
print(len(list))            #[1, 7, 8, 9, 10, 12, 5] list adjust their size

#for string
list=[1,2,3,4,5]
list[1:3]="Shailesh"   # list[n:m] = [n,m) indexed elements are replaced
print(list) 

#sorting the list
#Ascending
list = [4,6,7,25,63,98,45]
list.sort()                   #For sort list
print(list)

#for reverse list
list = [1,2,3,4,5]
list.reverse()
print(list)

#Descending
list = [4, 6, 7, 25, 45, 63, 98]
list.sort(reverse=True)
print(list)