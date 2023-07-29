x = int(input("Введите трехзначное число",end = " "),end = " ")
n1 = x%10
x = x//10
n2 = x%10
n3 = x//10
print(n1+n2+n3,end = " ")