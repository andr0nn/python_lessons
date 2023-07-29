x = int(input("Введите четырехзначное число",end = " "),end = " ")
n1 = x%10
x = x//10
n2 = x%10
x = x//10
n3 = x%10
n4 = x//10
res = n1*1000+n2*10+n3*100+n4
print(res,end = " ")