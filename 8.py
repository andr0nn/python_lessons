x = int(input('Введите число от 1 до 9999: '))
if x<1 or x>9999:
    print('Вы ввели некорректное значение')
else:
    print('Вы ввели: ')
    if x//1000==1:
        print('Одна тысяча',end = " ")
        x = x%1000
    elif x//1000==2:
        print('Две тысячи',end = " ")
        x = x%1000
    elif x//1000==3:
        print('Три тысячи',end = " ")
        x = x%1000
    elif x//1000==4:
        print('Четыре тысячи',end = " ")
        x = x%1000
    elif x//1000==5:
        print('Пять тысяч',end = " ")
        x = x%1000
    elif x//1000==6:
        print('Шесть тысяч',end = " ")
        x = x%1000
    elif x//1000==7:
        print('Семь тысяч',end = " ")
        x = x%1000
    elif x//1000==8:
        print('Восемь тысяч',end = " ")
        x = x%1000
    elif x//1000==9:
        print('Девять тысяч',end = " ")
        x = x%1000

    #Работаем с сотнями


    if x//100==1:
        print('сто',end = " ")
        x = x%100
    elif x//100==2:
        print('двести',end = " ")
        x = x%100
    elif x//100==3:
        print('триста',end = " ")
        x = x%100
    elif x//100==4:
        print('четыреста',end = " ")
        x = x%100
    elif x//100==5:
        print('пятьсот ',end = " ")
        x = x%100
    elif x//100==6:
        print('шестьсот',end = " ")
        x = x%100
    elif x//100==7:
        print('семьсот',end = " ")
        x = x%100
    elif x//100==8:
        print('восемьсот',end = " ")
        x = x%100
    elif x//100==9:
        print('девятьсот',end = " ")
        x = x%100

    #Работаем с десятками

    if (x//10)%10==1:
        if x % 10 == 0:
            print('десять долларов',end = " ")
        elif x%10==1:
            print('одиннадцать долларов',end = " ")
        elif x%10==2:
            print('двенадцать долларов',end = " ")
        elif x%10==3:
            print('тринадцать долларов',end = " ")
        elif x%10==4:
            print('четырнадцать долларов',end = " ")
        elif x%10==5:
            print('пятнадцать долларов',end = " ")
        elif x%10==6:
            print('шестнадцать долларов',end = " ")
        elif x%10==7:
            print('семнадцать долларов',end = " ")
        elif x%10==8:
            print('восемнадцать долларов',end = " ")
        elif x%10==9:
            print('девятнадцать долларов',end = " ")
        #Работаем с десятками
if (x//10)%10 !=1:
    if x//10==2:
        print('двадцать',end = " ")
        x = x%10
    elif x//10==3:
        print('тридцать',end = " ")
        x = x%10
    elif x//10==4:
        print('сорок',end = " ")
        x = x%10
    elif x//10==5:
        print('пятьдесят',end = " ")
        x = x%10
    elif x//10==6:
        print('шестьдесят',end = " ")
        x = x%10
    elif x//10==7:
        print('семьдесят',end = " ")
        x = x%10
    elif x//10==8:
        print('восемьдесят',end = " ")
        x = x%10
    elif x//10==9:
        print('девятьсот',end = " ")
        x = x%10



    if x % 10 == 0:
        print('долларов',end = " ")
    elif x%10==1:
        print('один доллар',end = " ")
    elif x%10==2:
        print('два доллара',end = " ")
    elif x%10==3:
        print('три доллара',end = " ")
    elif x%10==4:
        print('четыре доллара',end = " ")
    elif x%10==5:
        print('пять долларов',end = " ")
    elif x%10==6:
        print('шесть долларов',end = " ")
    elif x%10==7:
        print('семь долларов',end = " ")
    elif x%10==8:
        print('восемь долларов',end = " ")
    elif x%10==9:
        print('девять долларов',end = " ")