import sys


q=range(1,1001)
q_sqr=list()
e=1000

for i in q:
    i=i*i
    q_sqr.append(i)

def sum_test(num):
    for i in q_sqr:
        if num + i in q_sqr:
            a=int(num**0.5)
            b=int(i**0.5)
            c=int((num+i)**0.5)
            if a+b+c==1000:
                print (a,b, c, "are are the answer")
                print ("product is",a*b*c)
                break

for i in q_sqr:
    sum_test (i)
