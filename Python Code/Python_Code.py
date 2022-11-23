x=input().split(",")
k=[]
for i in range(len(x)):
    k.append(x[-1])
    x.remove(x[-1])
for j in k:  
    if j!=k[-1]:
        print(j, end=',')
    else:
        print(j)

    


