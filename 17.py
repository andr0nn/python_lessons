a = int(input('a = '))
b = int(input('b = '))
if a<b:
    for i in range(a,b+1):
        print(i,end=" ")
elif a>b:
    for i in range(a,b-1,2-1):
        print(i,end=" ")
else:
    print(a)