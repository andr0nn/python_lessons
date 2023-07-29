for a in range(1,101):
    for b in range(a,101):
        c_q=a**2+b**2
        c=int(c_q**0.5)
        if c_q==c**2:
            print(a,b,c)