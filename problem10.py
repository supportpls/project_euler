#project euler problem 10

setprime=list([2])
checkprime=3
while max(setprime)<2000000:
    for prime in setprime:
        if checkprime%prime==0:
#            print (checkprime,"not added to list")
            break
    if prime == max(setprime):
        setprime.append(checkprime)
        print (checkprime, "is added to the list")
    checkprime=checkprime+1

final=setprime[:-1]
print ("final list is", final)
print ("final sum is", sum(final))
