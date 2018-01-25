#project euler problem 5

def isprime (s):
    print ("prime check ",s)
    for i in range(2,max(s,3)):
        #print ("checking if ", i, "is factor")
        if s%i==0:
            if s==i:
                out = 'y'# returns y when only divisible by itself
                break
            else:
                out='n'
                break #breaks when find a factor other itself
        else:
            out='y' #otherwise returns y when no factors found
    return out



prod=1

#test =isprime(prod)
#print (test)

for k in range(2,20):
    #print(k)
    #i=int(i)
    #prime_test=isprime(k)
    if isprime(k)== 'y':
        l=1
        while k**l <= 20:
            l=l+1
        print(l-1)
        prod = prod*(k**(l-1))
        print(prod)

print(prod)
