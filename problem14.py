#project euler problem 14
#by dan ikonnikov
#n → n/2 (n is even)
#n → 3n + 1 (n is odd)

step_count={1:1}

def next_chain_val(n):
    if n%2==0:
        n=int(n/2)
    else:
        n=int(3*n+1)
    return (n)

def valuator (n):
    counter = 0
    start_val=n
    temp = [] #MN
    print (n)
    while n not in step_count.keys():
        #print ("starting with", n)
        n=next_chain_val(n)
        temp.append(n) # MN
        #print (temp)
        counter=counter+1
        #print (counter)
    #print (step_count[n])
    step_count[start_val]=counter+step_count[n]
    for i in range (0,len(temp)):
        #print (temp[i])
        if temp[i] not in step_count.keys():
            step_count[temp[i]]=step_count[start_val]-i-1
    #print (step_count)
    #print(temp)


for i in range (1,1000000):
    if i not in step_count.keys():
        valuator (i)
#print(max(step_count.values()))
maximum = max(step_count, key=step_count.get)
print(maximum, step_count[maximum])
