Fruit = ("Apple")      # it is not consider as Tupple
print(type(Fruit))

#for convert to Tupple
Fruit = ("Apple",)
print(type(Fruit))
print(Fruit)

#method 2
# Fruit = ("Apples")              However, "Apple" is not treated as a tuple, but as a string. 
#                                 When you call tuple() on a string, 
#                                 it iterates over each character in the string and creates a tuple 
#                                 where each character becomes an element of the tuple. 
#                                 Since "Apple" is a string with multiple characters,
#                                 the resulting tuple will contain each character of the string as separate elements

Fruit = tuple(("Apple"))
print(type(Fruit))
print(Fruit)


#checking 
if "p" in Fruit:
    print("It is present.")
else:
    print("Not present.")

