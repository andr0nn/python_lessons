x=int(input('x = '))
for i in range(10):
    for j in range(10):
        for k in range(10):
            for h in range(10):
                if i+j+k+h == x:
                    print(i,j,k,h)