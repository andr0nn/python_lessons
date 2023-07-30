import random
atk1=100
atk2=80
helth1=350
helth2=420
t=0
while t<10:
    crit1=random.randint(1,20)
    crit2=random.randint(1,100)
    if crit1==5:
        print('crit1+')
    else:
        print('crit1-')
    if crit2>=7 and crit2<=14:
        print('crit2+')
    else:
        print('crit2-')
    t+=1
    
