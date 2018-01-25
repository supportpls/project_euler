#problem7
#project euler
#algorythim by mary ngyuen
#testing by dan ikonnikov

setprime=list([2])
checkprime=3
while len(setprime)<10001:
    for prime in setprime:
        if checkprime%prime==0:
            print (checkprime,"not added to list")
            break
    if prime == max(setprime):
        setprime.append(checkprime)
        print (checkprime, "is added to the list")
    checkprime=checkprime+1
print ("final set is", setprime)
