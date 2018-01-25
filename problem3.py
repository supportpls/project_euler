#euler problem 3
#by dan ikonnikov

#What is the largest prime factor of the number 600851475143 ?

#first we set the basic problem constraints
q=600851475143
w=int(q**(0.5))

#here we define a prime test which we will call later
def isprime (s):
    print ("prime check")
    a=int(s**(0.5))
    for i in range(2,a):
        print ("checking if ", i, "is factor")
        if s%i==0:
            out='n'
            break #breaks when find a factory
        else:
            out='y' #otherwise returns y
    return out

#this is the main problem part where the
if q%w==0:
    print (w)
else:
    while True:
        w=w-1
        if q%w==0:
            print ("possibly", w)
            print ("testing ", w, " for prime")
            test_out=isprime (w)
            if test_out == 'y':
                print ("should be", w)
                break
