set1 = {1,2,3}
set2 = {4,5,6}
set={1,1,2,3,5,2,5,2,5,25,25,2,5}
print(set)

#Joining two sets
#set3 = set1+set2          this is wrong
# Method 1
print(set1,set2)

#Method 2
set1.update(set2)
print(set1)

#method 3
set1 = {1,2,3,4}
set2 = {4,5,6,6}
set3 = set1.union(set2)
print(set3)

#INTERSECTION
#Method 1                                keep duplicate
set1 = {1,2,3,4,5,6}
set2 = {2,3,4,5}
set1.intersection_update(set2)
print(set1)

#Method2
set1 = {1,2,3}
set2 = {2,3,4,5}
set3=set1.intersection(set2)
print(set3)

#Keep all values except duplicate
set1 = {1,2,3,4,5,6}
set2 = {2,3,4,5}
set1.symmetric_difference_update(set2)
print(set1)

#This code will remove all elements from set1 that are also present in set2, and then print the updated set1  
#( set1 - set2 )
set1 = {1,2,3}
set2 = {2,3,4,5}
set1.difference_update(set2)
print(set1)


