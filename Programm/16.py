a=int(input('Введите начало диапазона'))
b=int(input('Введите конец диапазона'))
for i in range(a,b+1):
    twin=i+2
    if twin<=b:
        print(i,twin)