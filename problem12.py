 #proejct euler problem 12
 #triangle number
 #by dan ikonnikov & mary nguyen

x=1
y=2
factor_test=True

def factors_num(x):
    q=int(x/2)+1
    factors = []
    for i in range (1,max(2,q)):
        if x % i == 0:
            factors.append(i)
    return (len(factors))

while factor_test:
    if x % 4 == 0:
        print (x, ": ", factors_num(x))
        if factors_num(x) > 500:
            factor_test=False
    x=x+y
    y=y+1
