phones = {
    "John":45623,
    "Ria" :78956,
    "Joy" :78568
    }

#give all key 
for x in phones:
    print(x)

#give values
for x in phones:
    print(phones[x]) 

#give key + value
for x in phones.items():
    print(x)

#for differrnt
for x,y in phones.items():
    print(x,y)

#nested dictionary
phone= {
    "Area 1" : {
        "a" :12,
        "b" :13,
        "c" :14
        },
    "Area2":{
        "a":14,
        "e":56,
        "f":43
    }
}
print(phone["Area 1"]["a"])
print(phone["Area2"]["a"])
print(phone["Area2"]["e"])