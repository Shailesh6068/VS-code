word = "show"                                       # jar word present nasel tar -1 print hote
word1 = "everyone"                                  # word che pahile akshar kiti number la aahe te prink karate.
word2 = "o"                                         # character kiti number la aahe te print karate.
with open("practice.txt","r") as f:
    data = f.read()
    print(data.find(word))
    print(data.find(word1))
print(data.find(word2))
    

