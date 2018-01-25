#project euler problem 5
#by mary ngueyn
#edited by dan ikonikov

def isprime_large (s):
    print ("prime check", s)
    a=int(s**(0.5))
    print (a)
    for i in range(2,a):
        if s%i==0:
            out='n'
            print("is not prime")
            break #breaks when find a factor
        else:
            out='y' #otherwise returns y
            print("is prime")
            break
    return out

def isprime_small (s):
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

for k in range(2,20):
    if k < 10:
        if isprime_small(k)== 'y':
            l=1
            while k**l <= 20:
                l=l+1
            print(l-1)
            prod = prod*(k**(l-1))
            print(prod)
    else:
    #elif k >= 10:
        if isprime_large(k)== 'y':
            l=1
            while k**l <= 20:
                l=l+1
            print(l-1)
            prod = prod*(k**(l-1))
            print(prod)

print(prod)
