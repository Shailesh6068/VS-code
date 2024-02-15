def minimum(lis):
    m = lis[0]
    for i in range(0,len(lis)):
        if m > lis[i]:
            m = lis[i]
    print("The minimum value is:",m)

def maximum(lis):
    m = lis[0]
    for i in range(0,len(lis)):
        if m < lis[i]:
            m = lis[i]
    print("The maximum value is:",m)

    
def mean(lis):
    sum = 0
    for i in range(0,len(lis)):
        sum = sum + lis[i]
    print("The mean of number is: ",sum/len(lis))
    
lis = list(map(int,input().split()))    
minimum(lis)
maximum(lis)
mean(lis)