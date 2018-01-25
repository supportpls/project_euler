 #proejct euler problem 12
 #triangle number
 #by dan ikonnikov & mary nguyen

x=1
y=2
factor_test=True

def factors_num(x):
    #initialise the test values
    a = 1
    b = int(x/2)+ 1#control for outside case
    end = True
    factors = []
    while end:
        for i in range (a,b):
            if x % i == 0:
                a = int(i) + 1#modify future range value
                b = int(x/i)#modify future range value
                if i == b:
                    factors.append(i)
                    end = False
                    print ("1", factors)
                else:
                    factors.append(i)
                    factors.append(int(x/i))
                break
            else:
                if i==b-1:
                    end=False
                    print ("2", factors)
        if a==b:
            end = False
            print ("3", factors)
    return (len(factors))

while factor_test:
    print (x)
    if factors_num(x) > 500:
        factor_test=False
    x=x+y
    y=y+1
