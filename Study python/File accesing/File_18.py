def check_for_word():
    word = "learning"
    f = open("practice.txt","r")
    data = f.read()                            
    if(data.find(word) == -1):
        print(f"'{word}'is not found.")
    else:
        print(f"'{word}'is found.")

def check_for_line():
    word = "learning"
    with open("practice.txt","r") as f:
        data = True
        line_no = 1
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
                return
            line_no += 1

    return -1

check_for_word()
check_for_line()
            

            
        