#create Dictionary
phones = {
    "John":45623,
    "Ria" :78956,
    "Joy" :78568
    }

#print Dictionary
print(phones)

#Error
#print(phones[45623])

#Type
print(type(phones))

#length
print(len(phones))

#access the phone
print(phones["John"])
print(phones.get("John"))
print(phones.keys())
print(phones.values())

#update phone number
phones["John"] = 969696
print(phones)

#add elemtnt
phones["Kia"] = 987867
print(phones)

#add another dictionary
more_phone = {
    "Dia":4566,
    "jia":7894
    }
phones.update(more_phone)
print(phones)

#remove 

phones.pop("John")
print(phones)

#remove last element
phones.popitem()
print(phones)

#Empty the dictionary
phones.clear()
print(phones)