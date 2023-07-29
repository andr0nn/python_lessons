a = int(input("a = ",end = " "),end = " ")
b = int(input("b = ",end = " "),end = " ")
c = int(input("c = ",end = " "),end = " ")
if a>1000 and a<5000 or b>1000 and b<5000 or c>1000 and c<5000:
    a=a/2
    b=b/2
    c=c/2
    print(a,b,c,end = " ")
else:
    print("-",end = " ")