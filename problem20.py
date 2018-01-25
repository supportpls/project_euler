#problem 20

'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

startdigit=100
sumdigit=0
proddigit=1

while startdigit >0:
    proddigit=proddigit*startdigit
    startdigit=startdigit-1
    print (proddigit)

prodstr=str(proddigit)

lenprod=len(prodstr)

for i in range (0,lenprod):
    sumdigit=sumdigit+int(prodstr[i])


print ("sumdigit")
print (sumdigit)
