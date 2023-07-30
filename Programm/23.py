import random
res=1
x1=0
x2=0
x3=0
t=0
for i in range(0,10):
    x1=0
    x2=0
    x3=0
    t=0
    while x1!=7 or x2!=7 or x3!=7:
        x1=random.randint(1,7)
        x2=random.randint(1,7)
        x3=random.randint(1,7)
        t+=1
        print(x1,x2,x3)
    print(t)
    res=res*(1/t)
print(res)
