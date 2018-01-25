#project euler problem 6

i = range(1,101)
print (i)

b=sum(i)
b=b*b
print (b)

d=list()

for i in i:
    c=i*i
    d.insert(i,c)
    print (c)

f=sum(d)
print (f)

g=b-f

print (g)
