with open("demo.txt","r") as f:
    data = f.read()
    words = data.split()

for word in words:
    if word:
        print(f"first character of word '{word}':{word[0]}")
        print(f"last character of word '{word}':{word[-1]}")
    