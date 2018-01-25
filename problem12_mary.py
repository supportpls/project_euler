 #proejct euler problem 12
 #triangle number
 #by dan ikonnikov & mary nguyen

x=1
y=2
factor_test=True

def factors_num(x):
    a = 1
    b = int(x/2)+ 1
    dummyv= 0
    end = True

    factors = []

    while end:
        for i in range (a,b):
            if x % i == 0:
                a = int(i) +  1
                b = int(x/i)
                if i == b:
                    factors.append(i)
                    end = False
                else:
                    factors.append(i)
                    factors.append(int(x/i))

                break
            else:
                if i==b-1:
                    end=False
        if a==b:
            end = False
    return (len(factors))

while factor_test:
    if x % 2 == 0:
        print (x, ": ", factors_num(x))
        if factors_num(x) > 500:
            factor_test=False
    x=x+y
    y=y+1
