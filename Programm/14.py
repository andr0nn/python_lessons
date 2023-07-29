t=0
for j in range(1,1001):
    t=0
    for i in range(2,1001):
        if j%i==0:
            t+=1
    if t<=1:
        print(j,end=" ")

    