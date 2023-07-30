t=0
s=0
n=-1
while n!=0:
    t=0
    n=int(input('Введите число'))
    x=n
    while x>0:
        x=x//10
        t+=1
    s=s+t
print(s)
    