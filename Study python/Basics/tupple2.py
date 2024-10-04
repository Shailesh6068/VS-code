#traverse the Tupple
tuple = ("Apple",1,2,"Mangoe")
for i in tuple:
    print(i)

#contaminate The tupple
tuple1 = (1,2,3)
tuple2 = (4,5,6)
tuple1 = tuple1+tuple2
print(tuple1)

#Unpacking Tupple
colour = ("Orange","Green","Yellow","Blue")  
#  colour = colour1,colour2,colour3,colour4      "" this is wrong ""
colour1,colour2,colour3,colour4 = colour 
print(colour1,colour2,colour3,colour4)